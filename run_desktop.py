import os
import sys
import time
import subprocess
import webview
import socket

os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["DJANGO_SETTINGS_MODULE"] = "DjangoDesktopApp.settings"


def wait_for_server(host="127.0.0.1", port=8002, timeout=15):
    start = time.time()
    while time.time() - start < timeout:
        s = socket.socket()
        try:
            s.connect((host, port))
            s.close()
            return True
        except Exception:
            time.sleep(0.2)
    return False


def start_django_server():
    return subprocess.Popen(
        [sys.executable, "manage.py", "runserver", "127.0.0.1:8002"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )


def start_webview():
    if not wait_for_server():
        print("Django failed to start.")
        return

    window = webview.create_window(
        "My Django Desktop App",
        "http://127.0.0.1:8002/",
        confirm_close=True,
        width=900,
        height=600
    )
    webview.start()


if __name__ == "__main__":
    django_process = start_django_server()

    start_webview()

    django_process.terminate()
    os._exit(0)
