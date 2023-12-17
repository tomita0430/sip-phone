# ベースイメージとしてUbuntuを使用
FROM ubuntu:20.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    asterisk \
    && rm -rf /var/lib/apt/lists/*

# Asterisk設定ファイルのコピー
COPY config/pjsip.conf /etc/asterisk/pjsip.conf
COPY config/extensions.conf /etc/asterisk/extensions.conf
COPY config/manager.conf /etc/asterisk/manager.conf


# 使用するポートを公開
EXPOSE 5060
EXPOSE 10000-10010

# Asteriskをフォアグラウンドで実行
CMD ["asterisk", "-vvvvv", "-f"]
