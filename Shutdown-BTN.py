import tkinter as tk
import os
import threading
import time

# タイマーのデフォルト値（分）
default_timer = 30  # 30分

def start_shutdown_timer():
    # 入力されたタイマー値を取得
    try:
        timer_minutes = int(timer_entry.get())
    except ValueError:
        timer_minutes = default_timer

    # 分を秒に変換
    timer_seconds = timer_minutes * 60

    # シャットダウンを予約する関数
    def shutdown():
        os.system(f"shutdown /s /hybrid /f /t {timer_seconds}")

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
timer_label = tk.Label(window, text="タイマー（分）:")
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
