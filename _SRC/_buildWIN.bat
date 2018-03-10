pyinstaller ^
-F ^
--distpath ../bin/win/ ^
--workpath ./__pyinstallerWIN__ ^
--specpath ./__specsWIN__ ^
--name "PC2DedicatedServerWrapper" ^
--icon "icons/main.ico" ^
--upx-dir C:\_PORTABLE\PROGRAMS\UPX ^
--noupx ^
--noconsole ^
--noconfirm ^
--clean ^
PC2_DedicatedServerWrapper.py


pyinstaller ^
-F ^
--distpath ../bin/win/ ^
--workpath ./__pyinstallerWIN__ ^
--specpath ./__specsWIN__ ^
--name "GenerateStartscripts" ^
--icon "icons/scripts.ico" ^
--upx-dir C:\_PORTABLE\PROGRAMS\UPX ^
--noupx ^
--noconsole ^
--noconfirm ^
--clean ^
make_startscripts.py
