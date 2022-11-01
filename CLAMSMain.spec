# -*- mode: python -*-
a = Analysis(['clamsmain.pyw'],
             pathex=['C:\\Users\\rick.towler\\Desktop\\CLAMS'],
             hiddenimports=['events','measurementDialogs','conditionals','validations'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='CLAMS2.exe',
          debug=False,
          strip=None,
          upx=False,
          console=True,
          version='version.txt',
          icon='icons\\giant_clam.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=False,
               name='CLAMS2')
