import pjsua as pj
import sys

# コールバックを定義
class MyAccountCallback(pj.AccountCallback):
    def __init__(self, acc):
        pj.AccountCallback.__init__(self, acc)

    def on_incoming_call(self, call):
        print(f"Incoming call from {call.info().remote_uri}")
        call.answer(200)

# PJSUAライブラリを初期化
lib = pj.Lib()

try:
    # ライブラリの初期化
    lib.init()

    # トランスポートを作成
    transport = lib.create_transport(pj.TransportType.UDP)

    # ライブラリを開始
    lib.start()

    # アカウントを作成
    acc = lib.create_account_for_transport(transport, cb=MyAccountCallback)

    print("Registration complete, status=", acc.info().reg_status, "(" + acc.info().reg_reason + ")")

    # コンソール入力を待機
    input("Press Enter to exit...")

except pj.Error as e:
    print("Exception: " + str(e))
    lib.destroy()
    lib = None
    sys.exit(1)

# クリーンアップ
lib.destroy()
lib = None
