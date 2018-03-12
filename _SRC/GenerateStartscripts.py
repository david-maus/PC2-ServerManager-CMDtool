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


def replaceAll(folderCurrent):
    """Start the main function."""
    configFolder = os.path.abspath(os.path.join(folderCurrent,
                                                '../', '../', 'configs'))
    scriptsFolder = os.path.abspath(os.path.join(folderCurrent,
                                                 'startscripts'))

    os.chdir(scriptsFolder)
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


def main():
    """Start the main function."""
    if getattr(sys, 'frozen', False):
        folderCurrent = os.path.dirname(sys.executable)
    else:
        folderCurrent = os.path.abspath(os.path.dirname(__file__))
        folderCurrent = os.path.abspath(os.path.join(folderCurrent,
                                                     '../', 'bin', 'win'))

    replaceAll(folderCurrent)


if __name__ == "__main__":
    main()
