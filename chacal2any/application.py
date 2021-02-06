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

import os
from PyQt5 import QtWidgets
import chacal2any.resources as Resources
import chacal2any
from chacal2any.uis.ui_mainwindow import Ui_MainWindow


__ABOUT__ = u"""
chacal2any - version {}
Cet utilitaire permet de convertir des fichiers CHACAL (.crs) et de les
exporter à d'autres formats. CHACAL est une application propriétaire à 
Hydro-Québec et n'est pas disponible gratuitement.

Copyright (C) 2021-
Alexis L. Desrochers <alexisdesrochers@hotmail.ca>
""".format(chacal2any.VERSION_STRING)

__WARNING__ = u"""
L'utilitaire lit uniquement les fichiers CHACAL au format .crs générés d'une 
sortie sommaire sur le logiciel CHACAL.

Attention!!! Les fichiers de sorties définissent des valeurs par défaut pour les 
groupes de charges permanentes et de vent sur les structures dans les tableaux 
de charges puisque ces groupes ne sont pas définis par CHACAL. Une modification 
manuelle est requise.
"""

class AboutDialog(QtWidgets.QDialog):
    """
    Class implementation of an about dialog.
    """

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        label = QtWidgets.QLabel()
        label.setText(__ABOUT__)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QtWidgets.QMainWindow):
    """
    Class implementation of the application main window.
    """

    def __init__(self, engine, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._initialize()

        # hold a reference to the application engine
        self._engine = engine

    def _initialize(self):
        self.setWindowTitle(u"chacal2any - Utilitaire de conversion de fichiers CHACAL (.crs)")
        self.setWindowIcon(Resources.get_icon("chacal2any.png"))
        self.ui.action_Quit.setText("&Quitter")
        self.ui.action_Quit.setIcon(Resources.get_icon("quit.png"))
        self.ui.action_About.setText("À propos")
        self.ui.action_About.setIcon(Resources.get_icon("about.png"))
        self.ui.menu_File.setTitle("&Fichier")
        self.ui.menu_Help.setTitle("&Aide")
        self.ui.groupBoxInput.setTitle("Entrées")
        self.ui.groupBoxOutput.setTitle("Sorties")
        self.ui.groupBoxWarning.setTitle("Avertissements")
        self.ui.labelWarning.setText(__WARNING__)
        self.ui.labelCHACAL.setText("CHACAL : ")
        self.ui.checkBoxDXF.setText("DXF : ")
        self.ui.checkBoxXLS.setText("XLS : ")
        self.ui.pushButtonCHACAL.setIcon(Resources.get_icon("open_file.png"))
        self.ui.pushButtonCHACAL.setText("")
        self.ui.pushButtonDXF.setIcon(Resources.get_icon("open_file.png"))
        self.ui.pushButtonDXF.setText("")
        self.ui.pushButtonXLS.setIcon(Resources.get_icon("open_file.png"))
        self.ui.pushButtonXLS.setText("")
        self.ui.pushButtonAction.setIcon(Resources.get_icon("write.png"))
        self.ui.pushButtonAction.setText("Exporter")

        # Signals & slots
        self.ui.action_Quit.triggered.connect(self.close)
        self.ui.action_About.triggered.connect(self.show_about_dialog)
        self.ui.pushButtonCHACAL.clicked.connect(self.open_chacal_file_dialog)
        self.ui.pushButtonDXF.clicked.connect(self.open_dxf_file_dialog)
        self.ui.pushButtonXLS.clicked.connect(self.open_xls_file_dialog)
        self.ui.checkBoxDXF.clicked.connect(self.update_dxf_output)
        self.ui.checkBoxXLS.clicked.connect(self.update_xls_output)
        self.ui.pushButtonAction.clicked.connect(self.export)

        # update
        self.reset()
        self.update_dxf_output()
        self.update_xls_output()

    def engine(self):
        return self._engine

    def export(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # check if valid input file
        in_filename = self.ui.lineEditCHACAL.text()
        if not os.path.exists(in_filename) or len(in_filename) == 0:
            dlg.setWindowTitle("Erreur")
            dlg.setText("Le fichier CHACAL (.crs) sélectionné est invalide ou inexistant.")
            dlg.show()
            return
        # create model from input file
        if not self._engine.import_from_chacal_crs(1, in_filename):
            dlg.setWindowTitle("Erreur")
            dlg.setText("Erreur lors du traitement du fichier CHACAL (.crs).")
            dlg.show()
            return
        # process outputs
        msg = ""
        nError = 0
        if self.ui.checkBoxDXF.isChecked():
            out_filename = self.ui.lineEditDXF.text()
            if self._engine.create_dxf_file(1, out_filename):
                msg += "\nFichier DXF exporté correctement sous {}".format(out_filename)
            else:
                msg += "\nErreur lors de l'exportation du fichier DXF."
                nError += 1
        if self.ui.checkBoxXLS.isChecked():
            out_filename = self.ui.lineEditXLS.text()
            if self._engine.create_xls_file(1, out_filename):
                msg += "\nFichier XLS exporté correctement sous {}".format(out_filename)
            else:
                msg += "\nErreur lors de l'exportation du fichier XLS."
                nError += 1
        # show status log
        dlg.setWindowTitle("Log")
        dlg.setText(msg)
        dlg.show()
        # reset if no error
        if nError <= 0:
            self.reset()

    def open_chacal_file_dialog(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, filter="CHACAL (*.crs)")
        if filename[0] != "":
            self.ui.lineEditCHACAL.setText(filename[0])

    def open_dxf_file_dialog(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, filter="DXF (*.dxf)")
        if filename[0] != "":
            self.ui.lineEditDXF.setText(filename[0])

    def open_xls_file_dialog(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, filter="XLS (*.xls)")
        if filename[0] != "":
            self.ui.lineEditXLS.setText(filename[0])

    def reset(self):
        self.ui.lineEditCHACAL.setText("")
        self.ui.lineEditDXF.setText("")
        self.ui.lineEditXLS.setText("")
        self.ui.checkBoxDXF.setChecked(False)
        self.ui.checkBoxXLS.setChecked(False)

        # TODO!!!
        self.ui.checkBoxXLS.setEnabled(False)

    def update_dxf_output(self):
        self.ui.lineEditDXF.setEnabled(self.ui.checkBoxDXF.isChecked())
        self.ui.pushButtonDXF.setEnabled(self.ui.checkBoxDXF.isChecked())

    def update_xls_output(self):
        self.ui.lineEditXLS.setEnabled(self.ui.checkBoxXLS.isChecked())
        self.ui.pushButtonXLS.setEnabled(self.ui.checkBoxXLS.isChecked())

    def show_about_dialog(self):
        dlg = AboutDialog(self)
        dlg.show()
