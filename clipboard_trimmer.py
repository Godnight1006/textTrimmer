import win32clipboard
import time
import threading

def monitor_clipboard():
    last_text = ""
    while True:
        time.sleep(0.5)
        clipboard_opened = False
        try:
            win32clipboard.OpenClipboard()
            clipboard_opened = True
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
                text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                if text != last_text:
                    last_text = text
                    trim_clipboard(text)
        except Exception as e:
            pass  # Handle clipboard access errors silently
        finally:
            if clipboard_opened:
                try:
                    win32clipboard.CloseClipboard()
                except:
                    pass

def trim_clipboard(text):
    lines = text.split('\n')
    if len(lines) > 100:
        trimmed = '\n'.join(lines[-100:])
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, trimmed)
        finally:
            try:
                win32clipboard.CloseClipboard()
            except:
                pass

if __name__ == "__main__":
    monitor_clipboard()
