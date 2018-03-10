#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Project Cars 2 / Dedicated Server Wrapper / Release maker.

by David Maus/neslane at www.gef-gaming.de

"""


import glob
import os
import sys
import re


def findLargestNumber(text):
    ls = list()
    for w in text.split(':'):
        try:
            ls.append(int(w))
        except:
            pass
    try:
        return max(ls)
    except:
        return None


def replaceAll(folderCurrent):
    """Start the main function."""
    folder7zip = os.path.abspath(os.path.join(folderCurrent,
                                              '_7zip'))
    folderRelease = os.path.abspath(os.path.join(folderCurrent,
                                                 '../', '_RELEASE'))
    folderRoot = os.path.abspath(os.path.join(folderCurrent,
                                              '../'))
    norelease = 0
    os.chdir(folderRelease)
    releaseNumber = []
    for file in glob.glob("*.zip"):
        releaseName = file.replace('.zip', '')
        LatestVersion = re.compile(r'(\d+)$').search(releaseName).group(1)
        releaseNumber.append(LatestVersion)
    if not releaseNumber:
        releaseNumber = ['0']
        norelease = 1
    versionNumberString = ':'.join(releaseNumber)
    versionNumber = findLargestNumber(versionNumberString)
    if (norelease == 1):
        versionNumber = versionNumber
    else:
        versionNumber = versionNumber + 1
    versionNumber = str(versionNumber)
    print(versionNumber)
    fileReleaseName = 'PC2DedicatedServerWrapper_1.' + versionNumber + '.zip'

    fileRelase = os.path.abspath(os.path.join(folderRelease,
                                              fileReleaseName))

    os.chdir(folder7zip)
    os.system('7za.exe a -t7z "' + fileRelase + '" "' + folderRoot + '" -xr!_SRC -xr!.git -xr!_RELEASE')


def main():
    """Start the main function."""
    if getattr(sys, 'frozen', False):
        folderCurrent = os.path.dirname(sys.executable)
    else:
        folderCurrent = os.path.abspath(os.path.dirname(__file__))

    replaceAll(folderCurrent)


if __name__ == "__main__":
    main()
