#!/usr/bin/env python
# -- clipboard.py
#!/usr/bin/env python
# -- clipboard.py
import sys,subprocess 
 
global get;
global set; 
 
if sys.platform.startswith("win"):
    import ctypes
    wcscpy = ctypes.cdll.msvcrt.wcscpy
    OpenClipboard = ctypes.windll.user32.OpenClipboard
    EmptyClipboard = ctypes.windll.user32.EmptyClipboard
    GetClipboardData = ctypes.windll.user32.GetClipboardData
    SetClipboardData = ctypes.windll.user32.SetClipboardData
    CloseClipboard = ctypes.windll.user32.CloseClipboard
    CF_UNICODETEXT = 13
    GlobalAlloc = ctypes.windll.kernel32.GlobalAlloc
    GlobalLock = ctypes.windll.kernel32.GlobalLock
    GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock
    GMEM_DDESHARE = 0x2000
     
    def get():
        OpenClipboard(None)
        handle = GetClipboardData(CF_UNICODETEXT)
        data = ctypes.c_wchar_p(handle).value
        pcontents = GlobalLock(handle)
        data = ctypes.c_wchar_p(pcontents).value if pcontents else u''
        GlobalUnlock(handle)
        CloseClipboard()
        return data
     
    def set(data):
        if not isinstance(data, unicode):
            data = data.decode('mbcs')
        OpenClipboard(None)
        EmptyClipboard()
        hCd = GlobalAlloc(GMEM_DDESHARE, 2 * (len(data) + 1))
        pchData = GlobalLock(hCd)
        wcscpy(ctypes.c_wchar_p(pchData), data)
        GlobalUnlock(hCd)
        SetClipboardData(CF_UNICODETEXT, hCd)
        CloseClipboard()
elif sys.platform.startswith("cygwin"):
    def get():
        p = subprocess.Popen(['cat', '/dev/clipboard'], stdout=subprocess.PIPE) 
        data = p.stdout.read()
        return data
    def set(data):
        cp = file('/dev/clipboard', 'wb')
        cp.seek(0)
        cp.write(data)
        cp.close()
elif sys.platform.startswith("darwin"):
    def get():
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE) 
        # retcode = p.wait() 
        data = p.stdout.read()
        return data
    def set(data):
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(data) 
        p.stdin.close() 
        retcode = p.wait()
        return retcode
else:
    raise ImportError("my module doesn't support this system")

