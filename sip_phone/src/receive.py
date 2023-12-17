import pjsua2
import time
import threading

class MyAccountCallback(pjsua2.AccountCallback):
    def __init__(self, account):
        super().__init__(account)

    def onIncomingCall(self, prm):
        call = MyCall(self.account, prm.callId)
        call_prm = pjsua2.CallOpParam(True)
        call.answer(call_prm)

class MyCall(pjsua2.Call):
    def __init__(self, acc, call_id=pjsua2.PJSUA_INVALID_ID):
        super().__init__(acc, call_id)

    # ここに着信時の処理を記述
    def onCallState(self, prm):
        ci = self.getInfo()
        print("Call is", ci.stateText, ci.lastStatusCode)

def main():
    # PJSUA2の初期化
    ep = pjsua2.Endpoint()
    ep.libCreate()

    # エンドポイントの設定
    ep_cfg = pjsua2.EpConfig()
    ep.libInit(ep_cfg)

    # トランスポートの設定
    tp_cfg = pjsua2.TransportConfig()
    tp_cfg.port = 5060
    ep.transportCreate(pjsua2.PJSIP_TRANSPORT_UDP, tp_cfg)

    # ライブラリの開始
    ep.libStart()
    print("PJSUA2 started")

    # アカウントの設定と登録
    acc_cfg = pjsua2.AccountConfig()
    acc_cfg.idUri = "sip:your_username@sip_server"
    acc_cfg.regConfig.registrarUri = "sip:sip_server"
    authCred = pjsua2.AuthCredInfo("digest", "*", "your_username", 0, "your_password")
    acc_cfg.sipConfig.authCreds.append(authCred)

    acc = MyAccount()
    acc.create(acc_cfg)

    # 一定時間（例えば10秒）着信を待つ
    time.sleep(10)

    # シャットダウン
    ep.libDestroy()

if __name__ == "__main__":
    main()
