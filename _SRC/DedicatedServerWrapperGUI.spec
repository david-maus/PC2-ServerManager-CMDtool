# -*- mode: python -*-

block_cipher = None


a = Analysis(['./DedicatedServerWrapperGUI.py'],
             pathex=['./_pyinstaller'],
             binaries=[],
             datas=[ ('./ui', 'ui' ) ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DedicatedServerWrapperGUI',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False , icon='./icons/main.ico')
