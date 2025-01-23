import win32clipboard
import time
import threading

def monitor_clipboard():
    last_text = ""
    while True:
        time.sleep(0.5)  # Check every 0.5 seconds
        try:
            win32clipboard.OpenClipboard()
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
                text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                if text != last_text:  # Only process new content
                    last_text = text
                    trim_clipboard(text)
        finally:
            win32clipboard.CloseClipboard()

def trim_clipboard(text):
    lines = text.split('\n')
    if len(lines) > 100:
        trimmed = '\n'.join(lines[-100:])
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, trimmed)
        win32clipboard.CloseClipboard()

if __name__ == "__main__":
    monitor_clipboard()
