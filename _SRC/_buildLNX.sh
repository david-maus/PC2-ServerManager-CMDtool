pyinstaller ^
-F ^
--distpath ../bin/lnx/ ^
--workpath ./__pyinstallerLNX__ ^
--specpath ./__specsLNX__ ^
--name "PC2_DedicatedServerWrapper" ^
--upx-dir C:\_PORTABLE\PROGRAMS\UPX ^
--noupx ^
--noconsole ^
--noconfirm ^
--clean ^
PC2_DedicatedServerWrapper.py
