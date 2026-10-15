import os
import sys
import sysconfig
from importlib.metadata import version

patch_map = {
    ".cp311-win_amd64.pyd": [("0F 85 BE 04 00 00", "90 E9 BE 04 00 00"), ("0F 84 F6 F5 FF FF", "90 90 90 90 90 90")],
    ".cp312-win_amd64.pyd": [("0F 85 61 04 00 00", "90 E9 61 04 00 00"), ("0F 84 BD F4 FF FF", "90 90 90 90 90 90")],
    ".cp313-win_amd64.pyd": [("0F 84 3E 2A 00 00", "90 90 90 90 90 90"), ("0F 85 53 27 00 00", "90 90 90 90 90 90")]
}

code = """
WeChatMainWnd.__init__.__closure__[0].cell_contents = lambda: True
"""

def patch(data, pattern_hex, patch_hex):
    pattern = bytes.fromhex(pattern_hex.replace(" ", ""))
    patch_bytes = bytes.fromhex(patch_hex.replace(" ", ""))
    pos = data.find(pattern)
    
    if pos == -1:
        return None, data

    data = bytearray(data)
    data[pos:pos + len(patch_bytes)] = patch_bytes
    return pos, bytes(data)

if __name__ == "__main__":
    if sys.platform != "win32":
        raise RuntimeError(f"仅支持 Windows")
        
    try:
        import wxautox4
    except ImportError as e:
        raise ImportError(f"请确认已安装 wxautox4")

    if version('wxautox4') != "41.2.1":
        raise RuntimeError(f"仅支持 v41.2.1")
        
    config_var = sysconfig.get_config_var("EXT_SUFFIX")
    wxautox_dir = os.path.join(os.path.expanduser("~"), ".wxautox")
    py_path  = os.path.join(os.path.dirname(wxautox4.__file__), 'ui', '__init__.py')
    pyd_path = os.path.join(os.path.dirname(wxautox4.__file__), 'ui', 'main' + config_var)
    
    if config_var not in patch_map:
        raise RuntimeError(f"仅支持 Python 3.11/3.12/3.13")
        
    if not os.path.exists(wxautox_dir):
        os.makedirs(wxautox_dir)

    with open(pyd_path, "rb") as f:
        data = f.read()

    _, data = patch(data, *patch_map[config_var][0])
    _, data = patch(data, *patch_map[config_var][1])

    with open(pyd_path, "wb") as f:
        f.write(data)

    with open(py_path, "a", encoding="utf-8") as f:
        f.write(code)
        
    print("破解 wxautox4 完成！")
    input("Enjoy reverse engineering!\n\nPress ENTER to exit...")
