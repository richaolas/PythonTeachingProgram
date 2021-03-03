# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cls39_snake_grow.py'],
             pathex=['C:\\Users\\ric_r\\Desktop\\research\\PythonTeachingProgram\\PythonFunnyProgram\\00.classic\\level5\\2.贪吃蛇'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='cls39_snake_grow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
