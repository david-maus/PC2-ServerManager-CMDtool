#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
RandomWeatherForPC2DS 0.7 - by David Maus / www.gef-gaming.de.

Randomize weather slots in dedicated server configuration for Project Cars 2.
Info at www.gef-gaming.de.
WARNING MESSY CODE! :)
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
    tracksFile = os.path.abspath(os.path.join(folderCurrent,
                                 'help', 'tracks.txt'))

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

    ActivateWeather = parser.get('WEATHERCHANCE', 'ActivateWeather')

    AuthenticWeather = parser.get('WEATHERCHANCE', 'AuthenticWeather')
    BugFree = parser.get('WEATHERCHANCE', 'BugFree')

    PracticeSlots = parser.get('WEATHERSLOTS', 'Practice')
    QualifySlots = parser.get('WEATHERSLOTS', 'Qualify')
    RaceSlots = parser.get('WEATHERSLOTS', 'Race')

    RaceSettings = parser.get('RACESETTINGS', 'RaceSettings')

    Track = parser.get('RACESETTINGS', 'Track')

    ClassSlots = int(parser.get('RACESETTINGS', 'ClassSlots'))
    ClassSlots -= 1
    ClassSlots = str(ClassSlots)

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



    ServerStart = parser.get('SETTINGS', 'ServerStart')
    ServerName = parser.get('SETTINGS', 'ServerName')
    Password = parser.get('SETTINGS', 'Password')
    MaxGrid = parser.get('SETTINGS', 'MaxGrid')

    if (MaxGrid == "max"):
        tracksFile = open(tracksFile, "r")
        for line in tracksFile:
            if re.match('"' + Track + '" .*', line):
                MaxGrid = re.compile(r'(\d+)$').search(line).group(1)
            else:
                MaxGrid = "32"



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
    if (ActivateWeather == "1"):
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


            line = re.sub(r'"PracticeWeatherSlots" : .*,',
                            '"PracticeWeatherSlots" : '
                            + PracticeSlots + ',', line)
            line = re.sub(r'"QualifyWeatherSlots" : .*,',
                            '"QualifyWeatherSlots" : '
                            + QualifySlots + ',', line)
            line = re.sub(r'"RaceWeatherSlots" : .*,',
                            '"RaceWeatherSlots" : '
                            + RaceSlots + ',', line)

            if(RaceSettings == '1'):
                line = re.sub(r'"TrackId" : ".*"',
                                '"TrackId" : "'
                                + Track + '"', line)
                line = re.sub(r'"MultiClassSlots" : .*,',
                                '"MultiClassSlots" : '
                                + ClassSlots + ',', line)
                line = re.sub(r'"VehicleClassId" : ".*"',
                                '"VehicleClassId" : "'
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
