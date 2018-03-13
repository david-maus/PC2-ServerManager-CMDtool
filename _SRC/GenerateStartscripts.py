#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Project Cars 2 / Dedicated Server Wrapper / Scripts maker.

by David Maus/neslane at www.gef-gaming.de

Randomized weather slots server config for Project Cars 2 dedicated server .
Info at www.gef-gaming.de.

WARNING MESSY CODE! :)
"""


import glob
import os
import sys
import pathlib
import stat

def replaceAll(folderCurrent, osPref):
    """Start the main function."""
    configFolder = os.path.abspath(os.path.join(folderCurrent,
                                                '../', '../', 'configs'))
    scriptsFolder = os.path.abspath(os.path.join(folderCurrent,
                                                 'startscripts'))
    pathlib.Path(scriptsFolder).mkdir(parents=False, exist_ok=True)
    os.chdir(scriptsFolder)

    if(osPref == "win"):
        for file in glob.glob("*.bat"):
            os.remove(file)

        os.chdir(configFolder)
        for file in glob.glob("*.ini"):
            if 'basic.ini' in file:
                pass
            else:
                scriptName = file.replace('.ini', '')
                scriptFile = os.path.abspath(os.path.join(scriptsFolder,
                                             scriptName + '.bat'))
                scriptFilePR = os.path.abspath(os.path.join(scriptsFolder,
                                               scriptName + '-Practice.bat'))
                scriptFileSun = os.path.abspath(os.path.join(scriptsFolder,
                                                scriptName + '-Sun.bat'))
                scriptFilePR_Sun = os.path.abspath(os.path.join(scriptsFolder,
                                                   scriptName +
                                                   '-PracticeSun.bat'))

                scriptWriter = open(scriptFile, "w")
                scriptWriter.write('cd ../\n')
                scriptWriter.write('DedicatedServerWrapper.exe ' + file)
                scriptWriter.close()

                scriptWriter = open(scriptFilePR, "w")
                scriptWriter.write('cd ../\n')
                scriptWriter.write('DedicatedServerWrapper.exe ' + file +
                                   ' PracticeServer')
                scriptWriter.close()

                scriptWriter = open(scriptFileSun, "w")
                scriptWriter.write('cd ../\n')
                scriptWriter.write('DedicatedServerWrapper.exe ' + file +
                                   ' Sunshine')
                scriptWriter.close()

                scriptWriter = open(scriptFilePR_Sun, "w")
                scriptWriter.write('cd ../\n')
                scriptWriter.write('DedicatedServerWrapper.exe ' + file +
                                   ' PracticeServer:Sunshine')
                scriptWriter.close()
    else:
        for file in glob.glob("*.sh"):
            os.remove(file)

        os.chdir(configFolder)

        for file in glob.glob("*.ini"):
            if 'basic.ini' in file:
                pass
            else:
                scriptName = file.replace('.ini', '')
                scriptFile = os.path.abspath(os.path.join(scriptsFolder,
                                             scriptName + '.sh'))
                scriptFilePR = os.path.abspath(os.path.join(scriptsFolder,
                                               scriptName + '-Practice.sh'))
                scriptFileSun = os.path.abspath(os.path.join(scriptsFolder,
                                                scriptName + '-Sun.sh'))
                scriptFilePR_Sun = os.path.abspath(os.path.join(scriptsFolder,
                                                   scriptName +
                                                   '-PracticeSun.sh'))

                scriptWriter = open(scriptFile, "w")
                scriptWriter.write('#!/bin/bash\n')
                scriptWriter.write('cd ../\n')
                scriptWriter.write('./DedicatedServerWrapper ' + file)
                scriptWriter.close()
                os.chmod(scriptFile, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

                scriptWriter = open(scriptFilePR, "w")
                scriptWriter.write('#!/bin/bash\n')
                scriptWriter.write('cd ../\n')
                scriptWriter.write('./DedicatedServerWrapper ' + file +
                                   ' PracticeServer')
                scriptWriter.close()
                os.chmod(scriptFilePR, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

                scriptWriter = open(scriptFileSun, "w")
                scriptWriter.write('#!/bin/bash\n')
                scriptWriter.write('cd ../\n')
                scriptWriter.write('./DedicatedServerWrapper ' + file +
                                   ' Sunshine')
                scriptWriter.close()
                os.chmod(scriptFileSun, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

                scriptWriter = open(scriptFilePR_Sun, "w")
                scriptWriter.write('#!/bin/bash\n')
                scriptWriter.write('cd ../\n')
                scriptWriter.write('./DedicatedServerWrapper ' + file +
                                   ' PracticeServer:Sunshine')
                scriptWriter.close()
                os.chmod(scriptFilePR_Sun, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)


def main():
    """Start the main function."""
    if sys.platform == "linux" or sys.platform == "linux2":
        osPref = "lnx"
    elif sys.platform == "win32":
        osPref = "win"
    if getattr(sys, 'frozen', False):
        folderCurrent = os.path.dirname(sys.executable)
    else:
        folderCurrent = os.path.abspath(os.path.dirname(__file__))
        folderCurrent = os.path.abspath(os.path.join(folderCurrent,
                                                     '../', 'bin', osPref))

    replaceAll(folderCurrent, osPref)


if __name__ == "__main__":
    main()
