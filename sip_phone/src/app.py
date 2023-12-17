import tkinter as tk
from tkinter import messagebox
import asterisk.manager
import threading

class CallManagerWindow:
    def __init__(self, manager):
        self.manager = manager

        # 新しいウィンドウを作成
        self.window = tk.Toplevel()
        self.window.title("Call Manager")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # 発信用の入力フィールドとボタン
        self.dial_frame = tk.Frame(self.window)
        self.dial_frame.pack()

        self.number_label = tk.Label(self.dial_frame, text="Number to dial:")
        self.number_label.pack(side=tk.LEFT)

        self.number_entry = tk.Entry(self.dial_frame)
        self.number_entry.pack(side=tk.LEFT)

        self.dial_button = tk.Button(self.dial_frame, text="Dial", command=self.dial)
        self.dial_button.pack(side=tk.LEFT)

        self.answer_frame = tk.Frame(self.window)
        self.answer_frame.pack()

        self.answer_label = tk.Label(self.answer_frame, text="Answer Call:")
        self.answer_label.pack(side=tk.LEFT)

        self.answer_button = tk.Button(self.answer_frame, text="Answer", command=self.answer_call)
        self.answer_button.pack(side=tk.LEFT)

        # ステータス表示用のテキストボックス
        self.status_text = tk.Text(self.window, height=10, width=50)
        self.status_text.pack()

    def dial(self):
        """ 発信処理 """
        number = self.number_entry.get()
        if not number:
            self.status_text.insert(tk.END, "番号が入力されていません。\n")
            return

        if not number.isdigit():
            self.status_text.insert(tk.END, "無効な番号です。\n")
            return

        # 発信処理を別スレッドで実行
        threading.Thread(target=self.do_dial, args=(number,), daemon=True).start()

    def do_dial(self, number):
        try:
            # 発信処理を行う
            self.manager.originate(f'SIP/{number}', '1000', 'default', '1', timeout=30000)
            self.status_text.insert(tk.END, f"{number} へ発信しました。\n")
        except Exception as e:
            self.status_text.insert(tk.END, f"発信エラー: {e}\n")

    def answer_call(self):
        """ 着信応答処理 """
        # ここに着信応答の処理を記述
        self.status_text.insert(tk.END, "応答しました。\n")

    def on_close(self):
        """ ウィンドウが閉じられるときの処理 """
        self.manager.logoff()
        self.window.destroy()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        root.title("AMI Login")

        # ユーザー名の入力
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # パスワードの入力
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # サーバーアドレスの入力
        self.server_label = tk.Label(root, text="Server Address:")
        self.server_label.pack()
        self.server_entry = tk.Entry(root)
        self.server_entry.pack()

        # ログインボタン
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        """ ログインボタンが押された時の処理 """
        username = self.username_entry.get()
        password = self.password_entry.get()
        server = self.server_entry.get()

        manager = asterisk.manager.Manager()
        try:
            manager.connect(server, port=5060)
            manager.login(username, password)
            messagebox.showinfo("Success", "Logged in successfully")
            CallManagerWindow(manager)
        except asterisk.manager.ManagerException as e:
            messagebox.showerror("Error", str(e))
            manager.logoff()

# GUIアプリケーションの起動
root = tk.Tk()
login_window = LoginWindow(root)
root.mainloop()
