C:\Python362\Scripts\pyrcc5.exe "C:\_GAMES\Steam\steamapps\common\Project CARS 2 - Dedicated Server\gef-gaming.de_pc2-ds-wrapper\_SRC\ui\resources.qrc" -o "C:\_GAMES\Steam\steamapps\common\Project CARS 2 - Dedicated Server\gef-gaming.de_pc2-ds-wrapper\_SRC\ui\resources.py"


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


pyinstaller ^
-F ^
--distpath ../bin/win/ ^
--workpath ./__pyinstallerWIN__ ^
--specpath ./__specsWIN__ ^
--name "GUI" ^
--icon "icons/main.ico" ^
--upx-dir C:\_PORTABLE\PROGRAMS\UPX ^
--noupx ^
--noconsole ^
--noconfirm ^
--clean ^
__specsWIN__/GUI.spec
