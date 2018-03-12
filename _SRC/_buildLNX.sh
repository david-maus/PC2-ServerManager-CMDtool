pyinstaller \
-F \
--distpath ../bin/lnx/ \
--workpath ./__pyinstallerLNX__ \
--specpath ./__specsLNX__ \
--name "PC2_DedicatedServerWrapper" \
--icon "icons/main.ico" \
--upx-dir C:\_PORTABLE\PROGRAMS\UPX \
--noupx \
--noconsole \
--noconfirm \
--clean \
PC2_DedicatedServerWrapper.py




pyinstaller \
-F \
--distpath ../bin/lnx/ \
--workpath ./__pyinstallerLNX__ \
--specpath ./__specsLNX__ \
--name "GenerateStartscripts" \
--icon "icons/scripts.ico" \
--upx-dir C:\_PORTABLE\PROGRAMS\UPX \
--noupx \
--noconsole \
--noconfirm \
--clean \
make_startscripts.py


pyinstaller \
-F \
--distpath ../bin/lnx/ \
--workpath ./__pyinstallerLNX__ \
--specpath ./__specsLNX__ \
--name "GUI" \
--icon "icons/main.ico" \
--upx-dir C:\_PORTABLE\PROGRAMS\UPX \
--noupx \
--noconsole \
--noconfirm \
--clean \
__specsLNX__/GUI.spec
