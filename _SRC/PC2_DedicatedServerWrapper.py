#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
RandomWeatherForPC2DS 0.7 - by David Maus / www.gef-gaming.de.

Randomize weather slots in dedicated server configuration for Project Cars 2.
Info at www.gef-gaming.de.
"""


import fileinput
import os
import sys
import re
import random
import bisect
import subprocess
import time
from configparser import ConfigParser


if os.path.basename(sys.argv[0]).endswith('.exe'):
    if sys.argv[1:]:
        iniFile = sys.argv[1]
    else:
        iniFile = 'basic.ini'
elif os.path.basename(sys.argv[0]).endswith('.py'):
    if sys.argv[1:]:
        iniFile = sys.argv[1]
    else:
        iniFile = 'basic.ini'


def replaceAll(iniFile, folderCurrent):

    rotateFile = os.path.abspath(os.path.join(folderCurrent, '../',
                                 'lua_Config', 'sms_rotate_config.json'))
    rotateCache = os.path.abspath(os.path.join(folderCurrent, '../',
                                 'lua_Config', 'sms_rotate_data.json'))
    statsCache = os.path.abspath(os.path.join(folderCurrent, '../',
                                 'lua_Config', 'sms_stats_data.json'))

    if os.path.isfile(rotateCache):
        os.remove(rotateCache)
    else:    # Show an error #
        print("Error: %s file not found" % rotateCache)

    if os.path.isfile(statsCache):
        os.remove(statsCache)
    else:    # Show an error #
        print("Error: %s file not found" % statsCache)

    serverFile = os.path.abspath(os.path.join(folderCurrent,
                                 '../', 'server.cfg'))
    serverExe = os.path.abspath(os.path.join(folderCurrent,
                                '../', 'DedicatedServerCmd.exe'))
    serverDir = os.path.abspath(os.path.join(folderCurrent, '../'))

    iniPath = os.path.join(folderCurrent, 'configs', iniFile)

    parser = ConfigParser()
    parser.read(iniPath)

    Clear = int(parser.get('WEATHERCHANCE', 'Clear'))
    LightCloud = int(parser.get('WEATHERCHANCE', 'LightCloud'))
    MediumCloud = int(parser.get('WEATHERCHANCE', 'MediumCloud'))
    HeavyCloud = int(parser.get('WEATHERCHANCE', 'HeavyCloud'))
    Overcast = int(parser.get('WEATHERCHANCE', 'Overcast'))
    LightRain = int(parser.get('WEATHERCHANCE', 'LightRain'))
    Rain = int(parser.get('WEATHERCHANCE', 'Rain'))
    Storm = int(parser.get('WEATHERCHANCE', 'Storm'))
    ThunderStorm = int(parser.get('WEATHERCHANCE', 'ThunderStorm'))
    snow = int(parser.get('WEATHERCHANCE', 'snow'))
    heavysnow = int(parser.get('WEATHERCHANCE', 'heavysnow'))
    blizzard = int(parser.get('WEATHERCHANCE', 'blizzard'))
    Foggy = int(parser.get('WEATHERCHANCE', 'Foggy'))
    FogWithRain = int(parser.get('WEATHERCHANCE', 'FogWithRain'))
    HeavyFog = int(parser.get('WEATHERCHANCE', 'HeavyFog'))
    HeavyFogWithRain = int(parser.get('WEATHERCHANCE', 'HeavyFogWithRain'))
    Hazy = int(parser.get('WEATHERCHANCE', 'Hazy'))

    AuthenticWeather = parser.get('WEATHERCHANCE', 'AuthenticWeather')
    BugFree = parser.get('WEATHERCHANCE', 'BugFree')

    PracticeSlots = parser.get('WEATHERSLOTS', 'Practice')
    QualifySlots = parser.get('WEATHERSLOTS', 'Qualify')
    RaceSlots = parser.get('WEATHERSLOTS', 'Race')

    RaceSettings = parser.get('RACESETTINGS', 'RaceSettings')

    ServerStart = parser.get('SETTINGS', 'ServerStart')
    ServerName = parser.get('SETTINGS', 'ServerName')
    Password = parser.get('SETTINGS', 'Password')
    MaxGrid = parser.get('SETTINGS', 'MaxGrid')
    ServerRestart = int(parser.get('SETTINGS', 'ServerRestart'))

    WeatherList = (('Clear', Clear), ('LightCloud', LightCloud),
                    ('MediumCloud', MediumCloud), ('HeavyCloud', HeavyCloud),
                    ('Overcast', Overcast), ('LightRain', LightRain),
                    ('Rain', Rain), ('Storm', Storm),
                    ('ThunderStorm', ThunderStorm), ('snow', snow),
                    ('heavysnow', heavysnow), ('blizzard', blizzard),
                    ('Foggy', Foggy), ('FogWithRain', FogWithRain),
                    ('HeavyFog', HeavyFog),
                    ('HeavyFogWithRain', HeavyFogWithRain), ('Hazy', Hazy))

    weightedChoice = WeightedChoice(WeatherList)

    if (BugFree == "1"):
        Practice1 = "clear"
        Practice2 = "clear"
        Practice3 = "clear"
        Practice4 = "clear"

        Qualify1 = "clear"
        Qualify2 = "clear"
        Qualify3 = "clear"
        Qualify4 = "clear"

        Race1 = "clear"
        Race2 = "clear"
        Race3 = "clear"
        Race4 = "clear"

        PracticeSlots = "1"
        QualifySlots = "1"
        RaceSlots = "1"
    else:
        Practice1 = weightedChoice.next()
        Practice2 = weightedChoice.next()
        Practice3 = weightedChoice.next()
        Practice4 = weightedChoice.next()

        Qualify1 = weightedChoice.next()
        Qualify2 = weightedChoice.next()
        Qualify3 = weightedChoice.next()
        Qualify4 = weightedChoice.next()

        Race1 = weightedChoice.next()
        Race2 = weightedChoice.next()
        Race3 = weightedChoice.next()
        Race4 = weightedChoice.next()

        if (AuthenticWeather == "1"):

            if (PracticeSlots == "1"):
                Qualify1 = Practice1
            elif (PracticeSlots == "2"):
                Qualify1 = Practice2
            elif (PracticeSlots == "3"):
                Qualify1 = Practice3
            elif (PracticeSlots == "4"):
                Qualify1 = Practice4

            if (QualifySlots == "1"):
                Race1 = Qualify1
            elif (QualifySlots == "2"):
                Race1 = Qualify2
            elif (QualifySlots == "3"):
                Race1 = Qualify3
            elif (QualifySlots == "4"):
                Race1 = Qualify4
        else:
            print("AuthenticWeather deactivated")

    for line in fileinput.input(rotateFile, inplace=1):
        line = re.sub(r'"PracticeWeatherSlot1" : ".*"',
                        '"PracticeWeatherSlot1" : "'
                        + Practice1 + '"', line)
        line = re.sub(r'"PracticeWeatherSlot2" : ".*"',
                        '"PracticeWeatherSlot2" : "'
                        + Practice2 + '"', line)
        line = re.sub(r'"PracticeWeatherSlot3" : ".*"',
                        '"PracticeWeatherSlot3" : "'
                        + Practice3 + '"', line)
        line = re.sub(r'"PracticeWeatherSlot4" : ".*"',
                        '"PracticeWeatherSlot4" : "'
                        + Practice4 + '"', line)
        line = re.sub(r'"QualifyWeatherSlot1" : ".*"',
                        '"QualifyWeatherSlot1" : "'
                        + Qualify1 + '"', line)
        line = re.sub(r'"QualifyWeatherSlot2" : ".*"',
                        '"QualifyWeatherSlot2" : "'
                        + Qualify2 + '"', line)
        line = re.sub(r'"QualifyWeatherSlot3" : ".*"',
                        '"QualifyWeatherSlot3" : "'
                        + Qualify3 + '"', line)
        line = re.sub(r'"QualifyWeatherSlot4" : ".*"',
                        '"QualifyWeatherSlot4" : "'
                        + Qualify4 + '"', line)

        line = re.sub(r'"RaceWeatherSlot1" : ".*"',
                        '"RaceWeatherSlot1" : "'
                        + Race1 + '"', line)
        line = re.sub(r'"RaceWeatherSlot2" : ".*"',
                        '"RaceWeatherSlot2" : "'
                        + Race2 + '"', line)
        line = re.sub(r'"RaceWeatherSlot3" : ".*"',
                        '"RaceWeatherSlot3" : "'
                        + Race3 + '"', line)
        line = re.sub(r'"RaceWeatherSlot4" : ".*"',
                        '"RaceWeatherSlot4" : "'
                        + Race4 + '"', line)


        line = re.sub(r'"PracticeWeatherSlots" :.*',
                        '"PracticeWeatherSlots" : '
                        + PracticeSlots + ',', line)
        line = re.sub(r'"QualifyWeatherSlots" :.*',
                        '"QualifyWeatherSlots" : '
                        + QualifySlots + ',', line)
        line = re.sub(r'"RaceWeatherSlots" :.*',
                        '"RaceWeatherSlots" : '
                        + RaceSlots + ',', line)

        sys.stdout.write(line)

    for line in fileinput.input(serverFile, inplace=1):
        line = re.sub(r'name : ".*"',
                        'name : "'
                        + ServerName + '"', line)
        line = re.sub(r'password : ".*"',
                        'password : "'
                        + Password + '"', line)
        line = re.sub(r'"GridSize" : .*,',
                        '"GridSize" : '
                        + MaxGrid + ',', line)
        line = re.sub(r'"MaxPlayers" : .*,',
                        '"MaxPlayers" : '
                        + MaxGrid + ',', line)

        sys.stdout.write(line)

    if(RaceSettings == '1'):
        print('RaceSettings deactivated. Loading the rotate file without change.')

    if (ServerStart == '1'):
        startServer(serverExe, serverDir, ServerRestart)


def main(iniFile):

    if getattr(sys, 'frozen', False):
        folderCurrent = os.path.dirname(sys.executable)
    else:
        folderCurrent = os.path.abspath(os.path.dirname(__file__))

    replaceAll(iniFile, folderCurrent)


def startServer(serverExe, serverDir, ServerRestart):

    if (ServerRestart == 0):
        p = subprocess.Popen(serverExe, cwd=serverDir)
    else:
        while True:
            p = subprocess.Popen(serverExe, cwd=serverDir)
            time.sleep(ServerRestart*60)
            p.kill()


class WeightedChoice(object):
    def __init__(self, weights):
        self.totals = []
        self.weights = weights
        running_total = 0

        for w in weights:
            running_total += w[1]
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]


if __name__ == "__main__":
    main(iniFile)
