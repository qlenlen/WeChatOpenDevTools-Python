# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

pyfiglet_datas = collect_data_files("pyfiglet")

datas = [
    ("configs/*.json", "configs"),
    ("scripts/*", "scripts"),
]

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=pyfiglet_datas + datas,
    hiddenimports=["pyfiglet.fonts"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="WechatOpenDevTools",
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name="WechatOpenDevTools",
)
