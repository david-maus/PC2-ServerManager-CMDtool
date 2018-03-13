#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Project Cars 2 / Dedicated Server Wrapper & Weather Randomizer.

by David Maus/neslane at www.gef-gaming.de

Randomized weather slots server config for Project Cars 2 dedicated server .
Info at www.gef-gaming.de.

WARNING MESSY CODE! :)
"""
import os
import sys; sys.dont_write_bytecode = True
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QFont
import glob
from ui import resources


def resource_path(relative_path):
    """Get Absolute Path."""
    base_path = getattr(sys, '_MEIPASS',
                        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def getIniFiles():
    """Get list of ini Files."""
    if getattr(sys, 'frozen', False):
        folderCurrent = os.path.dirname(sys.executable)
        folderCurrent = os.path.abspath(os.path.join(folderCurrent,
                                        '../', '../'))
    else:
        folderCurrent = os.path.abspath(os.path.dirname(__file__))
        folderCurrent = os.path.abspath(os.path.join(folderCurrent, '../'))

    iniFiles = []
    iniPath = os.path.abspath(os.path.join(folderCurrent, 'configs'))
    iniFiles = next(os.walk(iniPath))[2]

    return iniFiles


def Start():
    """Start Main Window UI."""
    global m
    m = Ui()
    m.show()
    return m


WHITE = QColor(255, 255, 255)
BLACK = QColor(0, 0, 0)
RED = QColor(255, 0, 0)
PRIMARY = QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY = QColor(42, 130, 218)


def css_rgb(color, a=False):
    """Get a CSS `rgb` or `rgba` string from a `QtGui.QColor`."""
    return ("rgba({}, {}, {}, {})" if a else "rgb({}, {}, {})").format(*color.getRgb())


class QDarkPalette(QPalette):
    """Set Dark palette for Qt meant to be used with the Fusion theme."""

    def __init__(self, *__args):
        """Initialize Palettes."""
        super().__init__(*__args)

        # Set all the colors based on the constants in globals
        self.setColor(QPalette.Window,          PRIMARY)
        self.setColor(QPalette.WindowText,      WHITE)
        self.setColor(QPalette.Base,            SECONDARY)
        self.setColor(QPalette.AlternateBase,   PRIMARY)
        self.setColor(QPalette.ToolTipBase,     WHITE)
        self.setColor(QPalette.ToolTipText,     WHITE)
        self.setColor(QPalette.Text,            WHITE)
        self.setColor(QPalette.Button,          PRIMARY)
        self.setColor(QPalette.ButtonText,      WHITE)
        self.setColor(QPalette.BrightText,      RED)
        self.setColor(QPalette.Link,            TERTIARY)
        self.setColor(QPalette.Highlight,       TERTIARY)
        self.setColor(QPalette.HighlightedText, BLACK)

    @staticmethod
    def set_stylesheet(app):
        """Start method to set the tooltip stylesheet to a `QtApplication`."""
        app.setStyleSheet("QToolTip {{"
                          "color: {white};"
                          "background-color: {tertiary};"
                          "border: 1px solid {white};"
                          "}}".format(white=css_rgb(WHITE), tertiary=css_rgb(TERTIARY)))

    def set_app(self, app):
        """Set the Fusion theme and this palette to a `QApplication`."""
        app.setStyle("Fusion")
        app.setPalette(self)
        self.set_stylesheet(app)


class UiSteamLogin(QtWidgets.QDialog):
    """Make Steam Login Window."""

    def __init__(self):
        """Initialize Steam Login Window."""
        super(UiSteamLogin, self).__init__()
        uic.loadUi(uiLoginFilePath, self)
        self.setWindowTitle('Steam Login Data')


class Ui(QtWidgets.QDialog):
    """Make Main Window."""

    def __init__(self):
        """Initialize Main Window."""
        super(Ui, self).__init__()
        uic.loadUi(uiFilePath, self)
        self.comboBox_2.installEventFilter(self)
        self.fillComboBox()
        self.pushButton_3.clicked.connect(self.handleOpenDialog)
        self.show()

    def handleOpenDialog(self):
        """Show Steam Login Window."""
        self.dialog = UiSteamLogin()
        self.dialog.exec_()

    def eventFilter(self, target, event):
        """Start Main Function."""
        if target == self.comboBox_2 and event.type() == QtCore.QEvent.MouseButtonPress:
            print('Button press')
            self.fillComboBox()

        return False

    def fillComboBox(self):
        """Start Main Function."""
        self.comboBox_2.clear()
        #self.comboBox_2.addItems(getIniFiles())


def main():
    """Start Main Function."""
    app = QtWidgets.QApplication(sys.argv)
    # font = QFont()
    # font.setPointSize(7)
    # app.setFont(font)
    QDarkPalette().set_app(app)
    window = Start()
    window.setWindowTitle(
        'Project Cars 2 Dedicated Server wrapper 1.1 - by GEF-GAMING.DE')

    sys.exit(app.exec_())


if __name__ == '__main__':
    uiFilePath = resource_path("ui/interfaceNEW.ui")
    uiLoginFilePath = resource_path("ui/interfaceLogin.ui")
    main()
