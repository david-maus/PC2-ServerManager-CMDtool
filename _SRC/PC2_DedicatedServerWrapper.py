#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Project Cars 2 / Dedicated Server Wrapper & Weather Randomizer.

by David Maus/neslane at www.gef-gaming.de

Randomized weather slots server config for Project Cars 2 dedicated server .
Info at www.gef-gaming.de.

WARNING MESSY CODE! :)
"""


import fileinput
import os
import sys
import stat
import re
import random
import bisect
import subprocess
import time
import shutil
from configparser import ConfigParser


if os.path.basename(sys.argv[0]).endswith('.exe'):
    if sys.argv[1:]:
        if ('.ini' in sys.argv[1]):
            iniFile = sys.argv[1]
            if sys.argv[2:]:
                StartParameter = sys.argv[2]
            else:
                StartParameter = ""
        else:
            iniFile = 'basic.ini'
            StartParameter = sys.argv[1]
    else:
        iniFile = 'basic.ini'
        StartParameter = ""
elif os.path.basename(sys.argv[0]).endswith('.py'):
    if sys.argv[1:]:
        if ('.ini' in sys.argv[1]):
            iniFile = sys.argv[1]
            if sys.argv[2:]:
                StartParameter = sys.argv[2]
            else:
                StartParameter = ""
        else:
            iniFile = 'basic.ini'
            StartParameter = sys.argv[1]
    else:
        iniFile = 'basic.ini'
        StartParameter = ""


def replaceAll(iniFile, folderCurrent, StartParameter):
    """Get the condifg settings and start of the replace function."""
    rotateFile = os.path.abspath(os.path.join(folderCurrent, '../',
                                 'lua_Config', 'sms_rotate_config.json'))
    rotateCache = os.path.abspath(os.path.join(folderCurrent, '../',
                                  'lua_Config', 'sms_rotate_data.json'))
    statsCache = os.path.abspath(os.path.join(folderCurrent, '../',
                                 'lua_Config', 'sms_stats_data.json'))
    tracksFile = os.path.abspath(os.path.join(folderCurrent,
                                 'help', 'tracks.txt'))
    serverFile = os.path.abspath(os.path.join(folderCurrent,
                                 '../', 'server.cfg'))
    serverExe = os.path.abspath(os.path.join(folderCurrent,
                                '../', 'DedicatedServerCmd.exe'))
    serverDir = os.path.abspath(os.path.join(folderCurrent, '../'))

    iniPath = os.path.join(folderCurrent, 'configs', iniFile)

    incPath = os.path.join(folderCurrent, 'inc')

    if os.path.isfile(rotateCache):
        os.remove(rotateCache)
    else:    # Show an error #
        print("Error: %s file not found" % rotateCache)

    if os.path.isfile(statsCache):
        os.remove(statsCache)
    else:    # Show an error #
        print("Error: %s file not found" % statsCache)

    copyDirTree(incPath, serverDir)

    parser = ConfigParser()
    parser.read(iniPath, encoding='utf8')

    ServerStart = parser.get('SETTINGS', 'ServerStart')
    ServerName = parser.get('SETTINGS', 'ServerName')
    Password = parser.get('SETTINGS', 'Password')
    MaxGrid = parser.get('SETTINGS', 'MaxGrid')
    ServerRestart = int(parser.get('SETTINGS', 'ServerRestart'))
    PracticeServer = parser.get('SETTINGS', 'PracticeServer')

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

    ActivateWeather = parser.get('WEATHERCHANCE', 'ActivateWeather')

    AuthenticWeather = parser.get('WEATHERCHANCE', 'AuthenticWeather')
    Sunshine = parser.get('WEATHERCHANCE', 'Sunshine')

    PracticeSlots = parser.get('WEATHERSLOTS', 'Practice')
    QualifySlots = parser.get('WEATHERSLOTS', 'Qualify')
    RaceSlots = parser.get('WEATHERSLOTS', 'Race')

    RaceSettings = parser.get('RACESETTINGS', 'RaceSettings')

    Track = parser.get('RACESETTINGS', 'Track')

    ClassSlots = int(parser.get('RACESETTINGS', 'ClassSlots'))

    Class1 = parser.get('RACESETTINGS', 'Class1')
    Class2 = parser.get('RACESETTINGS', 'Class2')
    Class3 = parser.get('RACESETTINGS', 'Class3')
    Class4 = parser.get('RACESETTINGS', 'Class4')

    Year = parser.get('RACESETTINGS', 'Year')
    Month = parser.get('RACESETTINGS', 'Month')
    Day = parser.get('RACESETTINGS', 'Day')
    TimePractice = parser.get('RACESETTINGS', 'TimePractice')
    TimeQuali = parser.get('RACESETTINGS', 'TimeQuali')
    TimeRace = parser.get('RACESETTINGS', 'TimeRace')

    PracticeLenght = parser.get('RACESETTINGS', 'PracticeLenght')
    QualifyLenght = parser.get('RACESETTINGS', 'QualifyLenght')
    RaceLenght = parser.get('RACESETTINGS', 'RaceLenght')

    MandatoryPitStop = parser.get('RACESETTINGS', 'MandatoryPitStop')

    DateprogressP = parser.get('RACESETTINGS', 'DateprogressP')
    DateprogressQ = parser.get('RACESETTINGS', 'DateprogressQ')
    DateprogressR = parser.get('RACESETTINGS', 'DateprogressR')
    WeatherprogressP = parser.get('RACESETTINGS', 'WeatherprogressP')
    WeatherprogressQ = parser.get('RACESETTINGS', 'WeatherprogressQ')
    WeatherprogressR = parser.get('RACESETTINGS', 'WeatherprogressR')

    Cooldownlap = parser.get('RACESETTINGS', 'Cooldownlap')
    Rollingstart = parser.get('RACESETTINGS', 'Rollingstart')
    Formationlap = parser.get('RACESETTINGS', 'Formationlap')

    MinimumOnlineRank = parser.get('RACESETTINGS', 'MinimumOnlineRank')

    Penalties = parser.get('RACESETTINGS', 'Penalties')
    PenaltyMax = parser.get('RACESETTINGS', 'PenaltyMax')
    PenaltyCut = parser.get('RACESETTINGS', 'PenaltyCut')
    PenaltyDT = parser.get('RACESETTINGS', 'PenaltyDT')

    TireWear = parser.get('RACESETTINGS', 'TireWear')
    Damage = parser.get('RACESETTINGS', 'Damage')
    MechanicalFailures = parser.get('RACESETTINGS', 'MechanicalFailures')
    Fuel = parser.get('RACESETTINGS', 'Fuel')

    CockpitView = parser.get('RACESETTINGS', 'CockpitView')
    ManualPitStops = parser.get('RACESETTINGS', 'ManualPitStops')
    ManualRolling = parser.get('RACESETTINGS', 'ManualRolling')

    ForceSetups = parser.get('RACESETTINGS', 'ForceSetups')
    ManualGears = parser.get('RACESETTINGS', 'ManualGears')
    PitstopErrors = parser.get('RACESETTINGS', 'PitstopErrors')
    Racedirector = parser.get('RACESETTINGS', 'Racedirector')
    Broadcaster = parser.get('RACESETTINGS', 'Broadcaster')
    AutoEnginestart = parser.get('RACESETTINGS', 'AutoEnginestart')
    Drivingline = parser.get('RACESETTINGS', 'Drivingline')
    RealisticAIDS = parser.get('RACESETTINGS', 'RealisticAIDS')
    AllowTC = parser.get('RACESETTINGS', 'AllowTC')
    AllowABS = parser.get('RACESETTINGS', 'AllowABS')
    AllowSC = parser.get('RACESETTINGS', 'AllowSC')
    RaceReadyInput = parser.get('RACESETTINGS', 'RaceReadyInput')
    PitspeedLimiter = parser.get('RACESETTINGS', 'PitspeedLimiter')
    Ghosting = parser.get('RACESETTINGS', 'Ghosting')
    GhostCollisions = parser.get('RACESETTINGS', 'GhostCollisions')

    hostPort = parser.get('SERVERSETTINGS', 'hostPort')
    queryPort = parser.get('SERVERSETTINGS', 'queryPort')
    sleepWaiting = parser.get('SERVERSETTINGS', 'sleepWaiting')
    sleepActive = parser.get('SERVERSETTINGS', 'sleepActive')
    enableHttpApi = parser.get('SERVERSETTINGS', 'enableHttpApi')
    selectDS = parser.get('SERVERSETTINGS', 'selectDS')

    if (enableHttpApi == "1"):
        enableHttpApi = "true"
    else:
        enableHttpApi = "false"

    if (selectDS == "1"):
        selectDS = "false"
    else:
        selectDS = "true"

    if (ClassSlots == 0):
        ClassAll = "1"
        ClassSlots = str(ClassSlots)
    elif (ClassSlots > 0):
        ClassSlots -= 1
        ClassSlots = str(ClassSlots)
        ClassAll = "0"

    if ('PracticeServer' in StartParameter):
        PracticeServer = "1"
    if ('Sunshine' in StartParameter):
        Sunshine = "1"

    if (PracticeServer == "1"):
        PracticeLenght = "1440"
        QualifyLenght = "1440"
        RaceLenght = "1L"
        DateprogressP = "0x"
        DateprogressQ = "0x"
        DateprogressR = "0x"
        WeatherprogressP = "Realtime"
        WeatherprogressQ = "Realtime"
        WeatherprogressR = "Realtime"
        Password = ""
        MandatoryPitStop = "0"
        MinimumOnlineRank = ""

    if (CockpitView == "1"):
        CockpitView = "CockpitHelmet"
    else:
        CockpitView = "Any"

    if (ManualPitStops == "1"):
        ManualPitStops = "0"
    else:
        ManualPitStops = "1"

    if (TireWear == "0"):
        TireWear = "OFF"
    elif (TireWear == "slow"):
        TireWear = "SLOW"
    elif (TireWear == "standard"):
        TireWear = "STANDARD"
    elif (TireWear == "2x"):
        TireWear = "X2"
    elif (TireWear == "3x"):
        TireWear = "X3"
    elif (TireWear == "4x"):
        TireWear = "X4"
    elif (TireWear == "5x"):
        TireWear = "X5"
    elif (TireWear == "6x"):
        TireWear = "X6"
    elif (TireWear == "7x"):
        TireWear = "X7"
    else:
        TireWear = "OFF"

    if (Damage == "0"):
        Damage = "OFF"
    elif (Damage == "visual"):
        Damage = "VISUAL_ONLY"
    elif (Damage == "performance"):
        Damage = "PERFORMANCEIMPACTING"
    elif (Damage == "full"):
        Damage = "FULL"
    else:
        Damage = "OFF"

    if (Fuel == "0"):
        Fuel = "OFF"
    elif (Fuel == "slow"):
        Fuel = "SLOW"
    elif (Fuel == "standard"):
        Fuel = "STANDARD"
    else:
        Fuel = "OFF"

    if (Penalties == "1"):
        Penalties = "FULL"
    else:
        Penalties = "NONE"

    if (DateprogressP == "Realtime"):
        DateprogressP = "1"
    else:
        DateprogressP = DateprogressP[:-1]

    if (DateprogressQ == "Realtime"):
        DateprogressQ = "1"
    else:
        DateprogressQ = DateprogressQ[:-1]

    if (DateprogressR == "Realtime"):
        DateprogressR = "1"
    else:
        DateprogressR = DateprogressR[:-1]

    if (WeatherprogressP == "Sync"):
        WeatherprogressP = "0"
    elif (WeatherprogressP == "Realtime"):
        WeatherprogressP = "1"
    else:
        WeatherprogressP = WeatherprogressP[:-1]

    if (WeatherprogressQ == "Sync"):
        WeatherprogressQ = "0"
    elif (WeatherprogressQ == "Realtime"):
        WeatherprogressQ = "1"
    else:
        WeatherprogressQ = WeatherprogressQ[:-1]

    if (WeatherprogressR == "Sync"):
        WeatherprogressR = "0"
    elif (WeatherprogressR == "Realtime"):
        WeatherprogressR = "1"
    else:
        WeatherprogressR = WeatherprogressR[:-1]

    FlagList = []
    if (ForceSetups == "0"):
        FlagList.append('ALLOW_CUSTOM_VEHICLE_SETUP')
    if (ManualGears == "1"):
        FlagList.append('FORCE_MANUAL')
    if (PitstopErrors == "1"):
        FlagList.append('PIT_STOP_ERRORS_ALLOWED')
    if (Racedirector == "1"):
        FlagList.append('HAS_RACE_DIRECTOR')
    if (Broadcaster == "1"):
        FlagList.append('HAS_BROADCASTER')
    if (AutoEnginestart == "1"):
        FlagList.append('AUTO_START_ENGINE')
    if (Drivingline == "0"):
        FlagList.append('DISABLE_DRIVING_LINE')
    if (RealisticAIDS == "1"):
        FlagList.append('FORCE_REALISTIC_DRIVING_AIDS')
    if (AllowTC == "1"):
        FlagList.append('TCS_ALLOWED')
    if (AllowABS == "1"):
        FlagList.append('ABS_ALLOWED')
    if (AllowSC == "1"):
        FlagList.append('SC_ALLOWED')
    if (RaceReadyInput == "1"):
        FlagList.append('WAIT_FOR_RACE_READY_INPUT')
    if (PitspeedLimiter == "1"):
        FlagList.append('PIT_SPEED_LIMITER')
    if (Ghosting == "1"):
        FlagList.append('GHOST_GRIEFERS')
    if (GhostCollisions == "1"):
        FlagList.append('ANTI_GRIEFING_COLLISIONS')

    if (Cooldownlap == "1"):
        FlagList.append('COOLDOWNLAP')

    if (MechanicalFailures == "1"):
        FlagList.append('MECHANICAL_FAILURES')

    if RaceLenght.endswith('M'):
        FlagList.append('TIMED_RACE')

    if (MinimumOnlineRank != ""):
        FlagList.append('ONLINE_REPUTATION_ENABLED')
        OnlineRankSafety = MinimumOnlineRank[0]
        OnlineRankSkill = MinimumOnlineRank[1:]
    else:
        OnlineRankSafety = "U"
        OnlineRankSkill = "500"

    FlagListString = ",".join(FlagList)
    RaceLenght = RaceLenght[:-1]

    if (MaxGrid == "max"):
        with open(tracksFile, "r", encoding='utf8') as tracksFileReader:
            for line in tracksFileReader:
                if re.match('"' + Track + '"', line):
                    GridMatch = re.compile(r'(\d+)$',
                                           re.ASCII).search(line).group(1)

        try:
            GridMatch
        except NameError:
            GridMatch = "32"
        MaxGrid = GridMatch

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

    if (ActivateWeather == "1"):
        if (Sunshine == "1"):
            Practice1 = "Clear"
            Practice2 = "Clear"
            Practice3 = "Clear"
            Practice4 = "Clear"

            Qualify1 = "Clear"
            Qualify2 = "Clear"
            Qualify3 = "Clear"
            Qualify4 = "Clear"

            Race1 = "Clear"
            Race2 = "Clear"
            Race3 = "Clear"
            Race4 = "Clear"

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
        with open(rotateFile, "r", encoding='utf8') as rotateFileIO:
            lines = rotateFileIO.readlines()
        with open(rotateFile, "w+", encoding='utf8') as rotateFileIO:
            for line in lines:
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

                line = re.sub(r'"PracticeWeatherSlots" : .*,',
                              '"PracticeWeatherSlots" : '
                              + PracticeSlots + ',', line)
                line = re.sub(r'"QualifyWeatherSlots" : .*,',
                              '"QualifyWeatherSlots" : '
                              + QualifySlots + ',', line)
                line = re.sub(r'"RaceWeatherSlots" : .*,',
                              '"RaceWeatherSlots" : '
                              + RaceSlots + ',', line)
                rotateFileIO.write(line)

    with open(rotateFile, "r", encoding='utf8') as rotateFileIO:
        lines = rotateFileIO.readlines()
    with open(rotateFile, "w+", encoding='utf8') as rotateFileIO:
        for line in lines:
            if(RaceSettings == '1'):
                line = re.sub(r'"TrackId" : ".*"',
                              '"TrackId" : "'
                              + Track + '"', line)
                line = re.sub(r'"MultiClassSlots" : .*,',
                              '"MultiClassSlots" : '
                              + ClassSlots + ',', line)
                if (ClassAll == "1"):
                    line = re.sub(r'.*"VehicleClassId" : ".*"',
                                  '//"VehicleClassId" : "'
                                  + Class1 + '"', line)
                else:
                    line = re.sub(r'.*"VehicleClassId" : ".*"',
                                  '\t\t"VehicleClassId" : "'
                                  + Class1 + '"', line)

                line = re.sub(r'"MultiClassSlot1" : ".*"',
                              '"MultiClassSlot1" : "'
                              + Class2 + '"', line)
                line = re.sub(r'"MultiClassSlot2" : ".*"',
                              '"MultiClassSlot2" : "'
                              + Class3 + '"', line)
                line = re.sub(r'"MultiClassSlot3" : ".*"',
                              '"MultiClassSlot3" : "'
                              + Class4 + '"', line)

                line = re.sub(r'"RaceDateYear" : .*,',
                              '"RaceDateYear" : '
                              + Year + ',', line)
                line = re.sub(r'"RaceDateMonth" : .*,',
                              '"RaceDateMonth" : '
                              + Month + ',', line)
                line = re.sub(r'"RaceDateDay" : .*,',
                              '"RaceDateDay" : '
                              + Day + ',', line)
                line = re.sub(r'"PracticeDateHour" : .*,',
                              '"PracticeDateHour" : '
                              + TimePractice + ',', line)
                line = re.sub(r'"QualifyDateHour" : .*,',
                              '"QualifyDateHour" : '
                              + TimeQuali + ',', line)
                line = re.sub(r'"RaceDateHour" : .*,',
                              '"RaceDateHour" : '
                              + TimeRace + ',', line)
                line = re.sub(r'"PracticeLength" : .*,',
                              '"PracticeLength" : '
                              + PracticeLenght + ',', line)
                line = re.sub(r'"QualifyLength" : .*,',
                              '"QualifyLength" : '
                              + QualifyLenght + ',', line)
                line = re.sub(r'"RaceLength" : .*,',
                              '"RaceLength" : '
                              + RaceLenght + ',', line)
                line = re.sub(r'"RaceMandatoryPitStops" : .*,',
                              '"RaceMandatoryPitStops" : '
                              + MandatoryPitStop + ',', line)

                line = re.sub(r'"PracticeDateProgression" : .*,',
                              '"PracticeDateProgression" : '
                              + DateprogressP + ',', line)
                line = re.sub(r'"QualifyDateProgression" : .*,',
                              '"QualifyDateProgression" : '
                              + DateprogressQ + ',', line)
                line = re.sub(r'"RaceDateProgression" : .*,',
                              '"RaceDateProgression" : '
                              + DateprogressR + ',', line)

                line = re.sub(r'"PracticeWeatherProgression" : .*,',
                              '"PracticeWeatherProgression" : '
                              + WeatherprogressP + ',', line)
                line = re.sub(r'"QualifyWeatherProgression" : .*,',
                              '"QualifyWeatherProgression" : '
                              + WeatherprogressQ + ',', line)
                line = re.sub(r'"RaceWeatherProgression" : .*,',
                              '"RaceWeatherProgression" : '
                              + WeatherprogressR + ',', line)

                line = re.sub(r'"RaceRollingStart" : .*,',
                              '"RaceRollingStart" : '
                              + Rollingstart + ',', line)
                line = re.sub(r'"RaceFormationLap" : .*,',
                              '"RaceFormationLap" : '
                              + Formationlap + ',', line)

                line = re.sub(r'"MinimumOnlineRank" : ".*"',
                              '"MinimumOnlineRank" : "'
                              + OnlineRankSafety + '"', line)
                line = re.sub(r'"MinimumOnlineStrength" : .*,',
                              '"MinimumOnlineStrength" : '
                              + OnlineRankSkill + ',', line)

                line = re.sub(r'"PenaltiesType" : ".*"',
                              '"PenaltiesType" : "'
                              + Penalties + '"', line)
                line = re.sub(r'"AllowablePenaltyTime" : .*,',
                              '"AllowablePenaltyTime" : '
                              + PenaltyMax + ',', line)
                line = re.sub(r'"PitWhiteLinePenalty" : .*,',
                              '"PitWhiteLinePenalty" : '
                              + PenaltyCut + ',', line)
                line = re.sub(r'"DriveThroughPenalty" : .*,',
                              '"DriveThroughPenalty" : '
                              + PenaltyDT + ',', line)

                line = re.sub(r'"TireWearType" : ".*"',
                              '"TireWearType" : "'
                              + TireWear + '"', line)
                line = re.sub(r'"DamageType" : ".*"',
                              '"DamageType" : "'
                              + Damage + '"', line)
                line = re.sub(r'"FuelUsageType" : ".*"',
                              '"FuelUsageType" : "'
                              + Fuel + '"', line)

                line = re.sub(r'"AllowedViews" : ".*"',
                              '"AllowedViews" : "'
                              + CockpitView + '"', line)
                line = re.sub(r'"ManualPitStops" : .*,',
                              '"ManualPitStops" : '
                              + ManualPitStops + ',', line)
                line = re.sub(r'"ManualRollingStarts" : .*,',
                              '"ManualRollingStarts" : '
                              + ManualRolling + ',', line)

                line = re.sub(r'"Flags" : ".*"',
                              '"Flags" : "'
                              + FlagListString + '"', line)

                rotateFileIO.write(line)

    with open(serverFile, "r", encoding='utf8') as serverFileIO:
        lines = serverFileIO.readlines()
    with open(serverFile, "w+", encoding='utf8') as serverFileIO:
        for line in lines:
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
            if (ClassAll == "1"):
                line = re.sub(r'"ServerControlsVehicleClass" : .*,',
                              '"ServerControlsVehicleClass" : '
                              + '0' + ',', line)
            else:
                line = re.sub(r'"ServerControlsVehicleClass" : .*,',
                              '"ServerControlsVehicleClass" : '
                              + '1' + ',', line)

            line = re.sub(r'hostPort : .*',
                          'hostPort : '
                          + hostPort, line)
            line = re.sub(r'queryPort : .*',
                          'queryPort : '
                          + queryPort, line)
            line = re.sub(r'sleepWaiting : .*',
                          'sleepWaiting : '
                          + sleepWaiting, line)
            line = re.sub(r'sleepActive : .*',
                          'sleepActive : '
                          + sleepActive, line)
            line = re.sub(r'enableHttpApi : .*',
                          'enableHttpApi : '
                          + enableHttpApi, line)
            line = re.sub(r'controlGameSetup : .*',
                          'controlGameSetup : '
                          + selectDS, line)

            serverFileIO.write(line)

    if (ServerStart == '1'):
        startServer(serverExe,
                    serverDir, ServerRestart, iniFile, StartParameter)


def main(iniFile, StartParameter):
    """Start the main function."""
    if getattr(sys, 'frozen', False):
        folderCurrent = os.path.dirname(sys.executable)
        folderCurrent = os.path.abspath(os.path.join(folderCurrent,
                                        '../', '../'))
    else:
        folderCurrent = os.path.abspath(os.path.dirname(__file__))
        folderCurrent = os.path.abspath(os.path.join(folderCurrent, '../'))

    replaceAll(iniFile, folderCurrent, StartParameter)


def startServer(serverExe, serverDir, ServerRestart, iniFile, StartParameter):
    """Start of the server."""
    if (ServerRestart == 0):
        p = subprocess.Popen(serverExe, cwd=serverDir)
    else:
        p = subprocess.Popen(serverExe, cwd=serverDir)
        time.sleep(ServerRestart*60)
        p.kill()
        time.sleep(5)
        main(iniFile, StartParameter)


class WeightedChoice(object):
    """Randomweather Choice class."""

    def __init__(self, weights):
        """Initialise."""
        self.totals = []
        self.weights = weights
        running_total = 0

        for w in weights:
            running_total += w[1]
            self.totals.append(running_total)

    def next(self):
        """Give weightened random values."""
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]


def copyDirTree(root_src_dir, root_dst_dir):
    """
    Copy directory tree. Overwrites also read only files.

    :param root_src_dir: source directory
    :param root_dst_dir:  destination directory
    """
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                try:
                    os.remove(dst_file)
                except PermissionError as exc:
                    os.chmod(dst_file, stat.S_IWUSR)
                    os.remove(dst_file)

            shutil.copy(src_file, dst_dir)


if __name__ == "__main__":
    main(iniFile, StartParameter)
