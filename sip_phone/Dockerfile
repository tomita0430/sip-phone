# Python環境のベースイメージを使用
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev-is-python3 \
    # libpjsua2 をビルドするための依存関係をインストール
    libssl-dev \
    libasound2-dev

# PJSIP をビルドしてインストール
RUN wget https://github.com/pjsip/pjproject/archive/refs/tags/2.14.tar.gz && \
    tar -xzf 2.14.tar.gz && \
    cd pjproject-2.14 && \
    ./configure && \
    make dep && make && make install

# Pythonの依存関係をインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY src/ .

# アプリケーションを実行
#CMD [ "python", "./app.py" ]