import win32clipboard

def trim_clipboard():
    try:
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        lines = text.split('\n')
        
        if len(lines) > 100:
            trimmed = '\n'.join(lines[-100:])
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, trimmed)
            
    except (TypeError, Exception):
        # No text in clipboard or other error
        pass
    finally:
        win32clipboard.CloseClipboard()

if __name__ == "__main__":
    trim_clipboard()
