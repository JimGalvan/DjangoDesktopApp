import subprocess
import time
import webview
import threading

def run_django():
    subprocess.Popen(["python", "manage.py", "runserver", "8765"])

def open_window():
    # wait for the server
    time.sleep(2)
    webview.create_window("My Django Desktop App", "http://127.0.0.1:8765")
    webview.start()

if __name__ == "__main__":
    threading.Thread(target=run_django).start()
    open_window()
