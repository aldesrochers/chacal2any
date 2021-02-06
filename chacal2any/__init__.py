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

__version_data__ = (0, 1, 0, "dev0")

import os

# Paths
ROOT_DIRPATH = os.path.dirname(os.path.abspath(__file__))

# Version
VERSION = ".".join(map(str, __version_data__))
VERSION_STRING = ".".join(map(str, __version_data__[0:3]))
VERSION_MAJOR = __version_data__[0]
VERSION_MINOR = __version_data__[1]
VERSION_PATCH = __version_data__[2]
VERSION_DEVEL = __version_data__[3]

