# =============================================================================
# Copyright (C) 2019-
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
import chacal2any
from PyQt5 import QtCore, QtGui



def _get_icons_dirpath():
    return os.path.join(chacal2any.ROOT_DIRPATH, "icons")

def get_icon(name, size=QtCore.QSize(64,64)):
    path = os.path.join(_get_icons_dirpath(), name)
    if not os.path.exists(path):
        path = os.path.join(_get_icons_dirpath(), "not_found.png")
    pixmap = QtGui.QPixmap(path)
    pixmap = pixmap.scaled(size, QtCore.Qt.KeepAspectRatio)
    return QtGui.QIcon(pixmap)

def get_pixmap(name, size=QtCore.QSize(64,64)):
    path = os.path.join(_get_icons_dirpath(), name)
    if not os.path.exists(path):
        path = os.path.join(_get_icons_dirpath(), "not_found.png")
    pixmap = QtGui.QPixmap(path)
    pixmap = pixmap.scaled(size, QtCore.Qt.KeepAspectRatio)
    return pixmap