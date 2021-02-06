# =============================================================================
# Copyright (C) 2021-
# Hydro-Quebec, Innovation Equipement et services partages
# Alexis L. Desrochers
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# =============================================================================

import sys
import chacal2any
from PyQt5 import QtCore, QtWidgets
from chacal2any import application as Application
from chacal2any import core as Core



__APPDESC__ = """
===============================================================================

Copyright (C) 2021-
Hydro-Quebec, Innovation Equipement et services partages
Alexis L. Desrochers

This is a simple application used to convert CHACAL (*.crs) tower load files
to any other usefull formats such as .dxf and .xls.

CHACAL is an HQ proprietary software not publicly available.

Alexis L. Desrochers <alexisdesrochers@hotmail.ca>

===============================================================================
"""


def convert_chacal_to_dxf(engine, filename_in, filename_out):
    """
    Method used to convert CHACAL to DXF from command-line.
    """
    raise NotImplementedError()
    return True

def convert_chacal_to_xls(engine, filename_in, filename_out):
    """
    Method used to convert CHACAL to XLS from command-line.
    """
    raise NotImplementedError()
    return True

def main():
    """
    Application main entry point.
    """
    # initialize an application
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("chacal2any")
    app.setApplicationDisplayName("chacal2any")
    app.setApplicationVersion(chacal2any.VERSION_STRING)

    # command-line arguments
    parser = QtCore.QCommandLineParser()
    option_chacal_input = QtCore.QCommandLineOption(("chacal"),
                                                    "Path to a CHACAL (*.crs) input file.",
                                                    "filename",
                                                    "")
    parser.addOption(option_chacal_input)
    option_dxf_output = QtCore.QCommandLineOption(("dxf"),
                                                  "Path to a DXF (*.dxf) output file.",
                                                  "filename",
                                                  "")
    parser.addOption(option_dxf_output)
    parser.addHelpOption()
    option_gui = QtCore.QCommandLineOption(("gui"),
                                           "Start the application in GUI mode.")
    parser.addOption(option_gui)
    option_xls_output = QtCore.QCommandLineOption(("xls"),
                                                  "Path to an Excel (*.xls) output file.",
                                                  "filename",
                                                  "")
    parser.addOption(option_xls_output)
    parser.addVersionOption()
    parser.process(app)

    # initialize an application engine
    engine = Core.Engine()

    # show gui ?
    if parser.isSet(option_gui):
        desktop = Application.MainWindow(engine)
        desktop.show()
        return sys.exit(app.exec_())

    # check if 'convert' from command-line
    if parser.isSet(option_chacal_input):
        n = 0
        chacal_filename = parser.value(option_chacal_input)
        if parser.isSet(option_dxf_output):
            dxf_filename = parser.value(option_dxf_output)
            if convert_chacal_to_dxf(engine, chacal_filename, dxf_filename):
                n += 1
        if parser.isSet(option_xls_output):
            xls_filename = parser.value(option_xls_output)
            if convert_chacal_to_xls(engine, chacal_filename, xls_filename):
                n += 1
        if n == 0:
            print("Could not convert any file.")
        sys.exit(0)
    else:
        desktop = Application.MainWindow(engine)
        desktop.show()
        return sys.exit(app.exec_())



if __name__ == '__main__':
    main()