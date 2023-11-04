# ベースイメージの指定
FROM debian:bullseye-slim

# Asteriskのインストールに必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    asterisk \
    asterisk-modules \
    && rm -rf /var/lib/apt/lists/*

# 設定ファイルをコンテナにコピー
COPY config/sip.conf /etc/asterisk/sip.conf
COPY config/extensions.conf /etc/asterisk/extensions.conf

# 必要なポートを公開
EXPOSE 5060/udp
EXPOSE 10000-20000/udp

# Asteriskの実行
CMD ["/usr/sbin/asterisk", "-f"]
