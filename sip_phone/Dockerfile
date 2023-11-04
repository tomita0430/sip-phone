# 使用するベースイメージを指定
FROM ubuntu:latest

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    build-essential \
    libasound2-dev

# PJSIP ライブラリをダウンロード、ビルド、インストール
RUN apt-get install -y wget && \
    wget https://www.pjsip.org/release/2.10/pjproject-2.10.tar.bz2 && \
    tar -xjf pjproject-2.10.tar.bz2 && \
    cd pjproject-2.10 && \
    ./configure && make dep && make && make install && \
    cd .. && rm -rf pjproject-2.10 pjproject-2.10.tar.bz2

# アプリケーションのコードと依存関係をコピー
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

# アプリケーションを実行
CMD ["python3", "app.py"]
