import tkinter as tk
import os
import threading
import time

# タイマーのデフォルト値（秒）
default_timer = 60

def start_shutdown_timer():
    # 入力されたタイマー値を取得
    try:
        timer_seconds = int(timer_entry.get())
    except ValueError:
        timer_seconds = default_timer

    # シャットダウンを実行する関数
    def shutdown():
        time.sleep(timer_seconds)
        os.system("shutdown /s /t 1")

    # タイマースレッドを開始
    timer_thread = threading.Thread(target=shutdown)
    timer_thread.start()

def cancel_shutdown_timer():
    # シャットダウンをキャンセルする関数
    os.system("shutdown /a")

# ウィンドウの作成
window = tk.Tk()
window.title("シャットダウンタイマー")

# タイマー入力フィールド
timer_label = tk.Label(window, text="タイマー（秒）:")
timer_label.pack()
timer_entry = tk.Entry(window)
timer_entry.insert(0, str(default_timer))
timer_entry.pack()

# 開始ボタン
start_button = tk.Button(window, text="タイマーを開始", command=start_shutdown_timer)
start_button.pack()

# キャンセルボタン
cancel_button = tk.Button(window, text="タイマーをキャンセル", command=cancel_shutdown_timer)
cancel_button.pack()

window.mainloop()
