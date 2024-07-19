import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('火星隕石のスペクトルデータの可視化')

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    # CSVファイルをデータフレームとして読み込む
    df = pd.read_csv(uploaded_file)
    # データフレームを表示
    st.write(df)

    # 描画対象の選択
    # 最初の列は通常インデックスやIDなので除外し、それ以外の列を選択肢にする
    # デフォルトで最初の列（スペクトルデータ）を選択
    options = st.multiselect(
        '表示するスペクトルを選択してください',
        df.columns[1:],  # 最初の列を除外
        default=df.columns[1]  # デフォルトで最初の列を選択
    )

    if options:
        # グラフの作成
        fig, ax = plt.subplots()
        # 選択された各列に対してプロットを作成
        for column in options:
            ax.plot(df[df.columns[0]], df[column], label=column)
        
        # グラフのラベル設定
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel('Reflectance')
        # 凡例を追加
        ax.legend()
        # グラフをStreamlitに表示
        st.pyplot(fig)
    else:
        # 何も選択されていない場合のメッセージ
        st.write("少なくとも一つの列を選択してください。")
