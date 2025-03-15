# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],  # Add the current directory to the search path
    binaries=[],
    datas=[
        # Include all necessary data folders and files
        ('data', 'data'),  # Include the data folder
        ('processed', 'processed'),  # Include the processed folder
        ('src/models', 'src/models'),  # Include models
        ('src/qt', 'src/qt'),  # Include Qt files
        ('src/ui', 'src/ui'),  # Include UI files
        ('static', 'static'),  # Include static folder
        ('templates', 'templates'),  # Include templates folder
        ('weights', 'weights'),  # Include weights folder
        ('uploads', 'uploads'),  # Include uploads folder
    ],
    hiddenimports=[
        # Add any hidden imports if necessary
        'cv2', 
        'numpy', 
        'PyQt5',
        'PyQt5.QtWidgets',
        'PyQt5.QtGui',
        'PyQt5.QtCore',
    ],
    hookspath=[],  # Specify hooks if custom ones are needed
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True if you want a console window for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
