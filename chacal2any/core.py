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

import os, re
import ezdxf


class DataModel(object):
    """
    Class implementation of a CHACAL data model.
    """

    def __init__(self):
        # attributes
        self._tower_name = ""
        self._author_name = ""
        self._date_time = ""
        # load cases
        self._load_cases = []

    def add_load_case(self):
        lc = LoadCaseData()
        self._load_cases.append(lc)
        return lc

    def get_author_name(self):
        return self._author_name

    def get_date_time(self):
        return self._date_time

    def get_load_case(self, index):
        if index > self.nb_load_cases() - 1:
            return None
        return self._load_cases[index]

    def get_tower_name(self):
        return self._tower_name

    def nb_load_cases(self):
        return len(self._load_cases)

    def remove_load_case(self, index):
        if index > self.nb_load_cases() - 1:
            return False
        self._load_cases.pop(index)
        return True

    def set_author_name(self, name):
        self._author_name = name

    def set_date_time(self, date_time):
        self._date_time = date_time

    def set_tower_name(self, name):
        self._tower_name = name


class LoadCaseData(object):
    """
    Class implementation of a CHACAL 'load case' data model.
    """

    def __init__(self):
        # attributes
        self._case_name = ""
        self._line_angle = 0.
        self._tower_deviation = 0.
        self._weight_spans = (0., 0., 0.)
        self._wind_spans = (0., 0., 0.)
        self._ice_thickness = 0.
        self._wind_pressure = 0.
        self._temperature = 0.
        self._alpha_factor = 0.
        self._fma_factor = 0.
        self._fmb_factor = 0.
        # load points
        self._load_points = []

    def add_load_point(self):
        lp = LoadPointData()
        self._load_points.append(lp)
        return lp

    def get_alpha_factor(self):
        return self._alpha_factor

    def get_case_name(self):
        return self._case_name

    def get_fma_factor(self):
        return self._fma_factor

    def get_fmb_factor(self):
        return self._fmb_factor

    def get_ice_thickness(self):
        return self._ice_thickness

    def get_line_angle(self):
        return self._line_angle

    def get_load_point(self, index):
        if index > self.nb_load_points() - 1:
            return None
        return self._load_points[index]

    def get_PP_front(self):
        return self._weight_spans[0]

    def get_PP_rear(self):
        return self._weight_spans[1]

    def get_PP_total(self):
        return self._weight_spans[2]

    def get_PV_front(self):
        return self._wind_spans[0]

    def get_PV_rear(self):
        return self._wind_spans[1]

    def get_PV_total(self):
        return self._wind_spans[2]

    def get_temperature(self):
        return self._temperature

    def get_tower_deviation(self):
        return self._tower_deviation

    def get_weight_spans(self):
        return self._weight_spans

    def get_wind_pressure(self):
        return self._wind_pressure

    def get_wind_spans(self):
        return self._wind_spans

    def nb_load_points(self):
        return len(self._load_points)

    def remove_load_point(self, index):
        if index > self.nb_load_points() - 1:
            return False
        self._load_points.pop(index)
        return True

    def set_alpha_factor(self, factor):
        self._alpha_factor = factor

    def set_case_name(self, name):
        self._case_name = name

    def set_fma_factor(self, factor):
        self._fma_factor = factor

    def set_fmb_factor(self, factor):
        self._fmb_factor = factor

    def set_ice_thickness(self, load):
        self._ice_thickness = load

    def set_line_angle(self, angle):
        self._line_angle = angle

    def set_PP_front(self, pp_front):
        self._weight_spans[0] = pp_front

    def set_PP_rear(self, pp_rear):
        self._weight_spans[1] = pp_rear

    def set_PP_total(self, pp_total):
        self._weight_spans[2] = pp_total

    def set_PV_front(self, pv_front):
        self._wind_spans[0] = pv_front

    def set_PV_rear(self, pv_rear):
        self._wind_spans[1] = pv_rear

    def set_PV_total(self, pv_total):
        self._wind_spans[2] = pv_total

    def set_temperature(self, temperature):
        self._temperature = temperature

    def set_tower_deviation(self, angle):
        self._tower_deviation = angle

    def set_weight_spans(self, weight_spans):
        self._weight_spans = weight_spans

    def set_wind_pressure(self, pressure):
        self._wind_pressure = pressure

    def set_wind_spans(self, wind_spans):
        self._wind_spans = wind_spans


class LoadPointData(object):
    """
    Class implementation of a CHACAL 'load point' data model.
    """

    def __init__(self):
        # attributes
        self._point_id = 0
        self._transversal_loads = (0., 0., 0.)
        self._longitudinal_loads = (0., 0., 0.)
        self._vertical_loads = (0., 0., 0.)

    def get_L1p_load(self):
        return self._longitudinal_loads[0]

    def get_L2p_load(self):
        return self._longitudinal_loads[1]

    def get_Lp_load(self):
        return self._longitudinal_loads[2]

    def get_longitudinal_loads(self):
        return self._longitudinal_loads

    def get_point_id(self):
        return self._point_id

    def get_T1p_load(self):
        return self._transversal_loads[0]

    def get_T2p_load(self):
        return self._transversal_loads[1]

    def get_Tp_load(self):
        return self._transversal_loads[2]

    def get_transversal_loads(self):
        return self._transversal_loads

    def get_V1p_load(self):
        return self._vertical_loads[0]

    def get_V2p_load(self):
        return self._vertical_loads[1]

    def get_Vp_load(self):
        return self._vertical_loads[2]

    def get_vertical_loads(self):
        return self._vertical_loads

    def set_L1p_load(self, L1p):
        self._longitudinal_loads[0] = L1p

    def set_L2p_Load(self, L2p):
        self._longitudinal_loads[1] = L2p

    def set_Lp_load(self, Lp):
        self._longitudinal_loads[2] = Lp

    def set_longitudinal_loads(self, longitudinal_loads):
        self._longitudinal_loads = longitudinal_loads

    def set_point_id(self, point_id):
        self._point_id = point_id

    def set_T1p_load(self, T1p):
        self._transversal_loads[0] = T1p

    def set_T2p_load(self, T2p):
        self._transversal_loads[1] = T2p

    def set_Tp_load(self, Tp):
        self._transversal_loads[2] = Tp

    def set_transversal_loads(self, transversal_loads):
        self._transversal_loads = transversal_loads

    def set_V1p_load(self, V1p):
        self._vertical_loads[0] = V1p

    def set_V2p_load(self, V2p):
        self._vertical_loads[1] = V2p

    def set_Vp_load(self, Vp):
        self._vertical_loads[2] = Vp

    def set_vertical_loads(self, vertical_loads):
        self._vertical_loads = vertical_loads


class ChacalCRSFileParser(object):
    """
    Class implementation of a 'file parser' for CHACAL files.
    """

    ERROR_None = 0
    ERROR_FileNotExists = 1
    ERROR_FileNotOpen = 2
    ERROR_InvalidFileType = 3

    def __init__(self, model, filename):
        self._model = model
        self._filename = filename
        self._error_code = self.ERROR_None
        self._error_string = ""
        self._is_done = False

    def error_code(self):
        return self._error_code

    def error_string(self):
        return self._error_string

    def filename(self):
        return self._filename

    def is_done(self):
        return self._is_done

    def model(self):
        return self._model

    def process(self):
        # check for valid filename
        filename = os.path.abspath(self._filename)
        if not os.path.exists(filename):
            self._error_code = self.ERROR_FileNotExists
            self._error_string = "File does not exists at path {}".format(filename)
            return False
        # process file
        with open(filename, 'r') as f:
            try:
                content = f.readlines()
            except:
                self._error_code = self.ERROR_FileNotOpen
                self._error_string = "Could not process file at path {}".format(filename)
                return False
        # check if valid 'CHACAL' file, only a basic check
        if content[60].split()[0] != "PRÉPARÉ":
            self._error_code = self.ERROR_InvalidFileType
            self._error_string = "File at path {} is not a valid 'CHACAL' file".format(filename)
            return False
        # get author name
        start = re.search("^PRÉPARÉ PAR :", content[60].strip()).span()[1]
        end = re.search("(____________________)", content[60].strip()).span()[0]
        author_name = content[60].strip()[start:end].strip()
        self._model.set_author_name(author_name)
        # get tower name
        tower_name = content[65].strip().split()[0]
        self._model.set_tower_name(tower_name)
        # get date/time
        date = content[65].strip().split()[1]
        time = content[65].strip().split()[3]
        date_time = "{} ({})".format(date, time)
        self._model.set_date_time(date_time)
        # get indexes for each load case
        # try to locate start of the load case definition and 'PP =' line.
        delimiter = "***********************************"
        start = None
        indexes = []
        for i, line in enumerate(content):
            if len(line.strip()) >= len(delimiter):
                if line.strip().split()[0] == delimiter and start == None:
                    start = i
            if re.match("PP =", line.strip()):
                indexes.append((start, i))
                start = None
        # populate data for each load case
        for i, indexes in enumerate(indexes):
            case = self._model.add_load_case()
            index_start, index_PP = indexes
            case_name = content[index_start + 1].strip()[:-5]
            case.set_case_name(case_name)
            angle, deviation = re.findall("[0-9.0]+", content[index_start + 4])
            case.set_line_angle(float(angle))
            case.set_tower_deviation(float(deviation))
            pp_front, pp_rear, pp_total = re.findall("[0-9.0]+", content[index_PP])
            case.set_weight_spans((float(pp_front), float(pp_rear), float(pp_total)))
            pv_front, pv_rear, pv_total = re.findall("[0-9.0]+", content[index_PP + 1])
            case.set_wind_spans((float(pv_front), float(pv_rear), float(pv_total)))
            ice, wind, temp, alpha = re.findall("[0-9.0]+", content[index_PP + 2])
            case.set_ice_thickness(float(ice))
            case.set_wind_pressure(float(wind))
            case.set_temperature(float(temp))
            case.set_alpha_factor(float(alpha))
            fma, fmb = re.findall("[0-9.0]+", content[index_PP + 3])
            case.set_fma_factor(float(fma))
            case.set_fmb_factor(float(fmb))
            # loop load points
            nb_load_points = (index_PP - index_start) - 8
            for i in range(nb_load_points):
                load_point = case.add_load_point()
                point_id, t1p, l1p, v1p, t2p, l2p, v2p, tp, lp, vp = re.findall("[0-9.0]+",
                                                                                content[index_start + 7 + i])
                load_point.set_point_id(point_id)
                load_point.set_longitudinal_loads((float(l1p), float(l2p), float(lp)))
                load_point.set_transversal_loads((float(t1p), float(t2p), float(tp)))
                load_point.set_vertical_loads((float(v1p), float(v2p), float(vp)))
        # set the 'is_done' flag internally
        self._is_done = True
        return True


class DXFDrawingParameters:
    """
    Class implementation of DXF drawing parameters.
    """

    # type of lines
    LineType_CONTINUOUS = 0

    # color of lines
    LineColor_WHITE = 0
    LineColor_CYAN = 4
    LineColor_MAGENTA = 6

    def __init__(self):
        self.ColumnWidth = 35
        self.FloatDigits = 1
        self.GridColor1 = self.LineColor_MAGENTA
        self.GridColor2 = self.LineColor_CYAN
        self.HeaderHeight = 18
        self.LayerName = "0"
        self.LineColor = self.LineColor_WHITE
        self.LineHeight = 10
        self.LineType = self.LineType_CONTINUOUS
        self.TableSpacing = 50
        self.TextHeight = 6
        self.TitleHeight = 14
        self.TitleTextHeight = 8


class DXFDrawingBuilder(object):
    """
    Class implementation of a dxf drawing builder.
    """

    ERROR_None = 0
    ERROR_InvalidDXF = 1
    ERROR_FailToProcessTable = 2

    def __init__(self, model, filename, parameters=DXFDrawingParameters()):
        self._model = model
        self._filename = filename
        self._error_code = self.ERROR_None
        self._error_string = ""
        self._is_done = False
        self._parameters = parameters
        self._dxf = None

    def _create_table(self, case_index):
        # coordinates of the 'table' top-left corner
        X0 = 0. + case_index * (self._table_width() + self._parameters.TableSpacing)
        Y0 = 0.
        # create table grid
        self._create_table_grid(case_index, X0, Y0)
        # create table texts
        self._create_table_texts(case_index, X0, Y0)
        return True

    def _create_table_grid(self, case_index, X0, Y0):
        # get the load case from model
        load_case = self._model.get_load_case(case_index)

        # attributes for principal grid
        attribs_1 = {}
        attribs_1["layer"] = self._parameters.LayerName
        attribs_1["color"] = self._parameters.GridColor1

        # attributes for secondary grid
        attribs_2 = {}
        attribs_2["layer"] = self._parameters.LayerName
        attribs_2["color"] = self._parameters.GridColor2

        # get a reference to the model
        model = self._dxf.modelspace()

        # get table height for this load case
        tableHeight = self._table_height(load_case)
        tableWidth = self._table_width()

        # create grid
        x1, y1 = X0, Y0
        x2, y2 = X0 + tableWidth, Y0
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0, Y0 - tableHeight
        x2, y2 = X0 + tableWidth, Y0 - tableHeight
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0, Y0
        x2, y2 = X0, Y0 - tableHeight
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0 + tableWidth, Y0
        x2, y2 = X0 + tableWidth, Y0 - tableHeight
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0, Y0 - self._parameters.TitleHeight
        x2, y2 = X0 + tableWidth, y1
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0, y2 - self._parameters.HeaderHeight
        x2, y2 = X0 + tableWidth, y1
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0, y2 - self._parameters.LineHeight
        x2, y2 = X0 + tableWidth, y1
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_2)

        x1, y1 = X0, y2 - self._parameters.LineHeight
        x2, y2 = X0 + tableWidth, y1
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        x1, y1 = X0, y2 - load_case.nb_load_points() * self._parameters.LineHeight
        x2, y2 = X0 + tableWidth, y1
        model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_1)

        for i in range(9):
            x1 = X0 + (i + 1) * self._parameters.ColumnWidth
            x2 = x1
            if i == 0 or i == 3 or i == 6:
                y1 = Y0 - self._parameters.TitleHeight - self._parameters.HeaderHeight
            else:
                y1 = Y0 - self._parameters.TitleHeight - self._parameters.HeaderHeight - self._parameters.LineHeight
            y2 = Y0 - self._parameters.HeaderHeight
            y2 += - (2 + load_case.nb_load_points()) * self._parameters.LineHeight
            y2 += - self._parameters.TitleHeight
            model.add_line((x1, y1), (x2, y2), dxfattribs=attribs_2)

    def _create_table_footer(self, footer_index, case_index, X0, Y0, text):
        # get the load case from model
        load_case = self._model.get_load_case(case_index)

        # get a reference to the model
        model = self._dxf.modelspace()

        # create footer
        attribs = {"height": self._parameters.TextHeight}
        x = X0 + 0.05 * self._parameters.ColumnWidth
        y = Y0 - (3.5 + footer_index + load_case.nb_load_points()) * self._parameters.LineHeight
        y += - self._parameters.HeaderHeight - self._parameters.TitleHeight
        model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_LEFT')

    def _create_table_texts(self, case_index, X0, Y0):
        # get the load case from model
        load_case = self._model.get_load_case(case_index)

        # get a reference to the model
        model = self._dxf.modelspace()

        # get table height for this load case
        tableHeight = self._table_height(load_case)
        tableWidth = self._table_width()

        # create headers
        attribs = {"height": self._parameters.TextHeight}
        texts = ['PT.', 'T', 'L', 'V', 'T', 'L', 'V', 'T', 'L', 'V']
        y = Y0 - self._parameters.LineHeight * 1.5 - self._parameters.HeaderHeight - self._parameters.TitleHeight
        for i, text in enumerate(texts):
            x = X0 + self._parameters.ColumnWidth / 2.0 + i * self._parameters.ColumnWidth
            model.add_text("{}".format(text), dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')

        texts = ['ARRIÈRE', 'AVANT', 'TOTAL']
        y = Y0 - self._parameters.LineHeight * 0.5 - self._parameters.HeaderHeight - self._parameters.TitleHeight
        for i, text in enumerate(texts):
            x = X0 + self._parameters.ColumnWidth * 2.5 + (i * 3) * self._parameters.ColumnWidth
            model.add_text("{}".format(text), dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')

        # create case name
        attribs = {"height": self._parameters.TitleTextHeight}
        x = X0 + tableWidth / 2.0
        y = Y0 - self._parameters.TitleHeight / 2.0
        text = load_case.get_case_name()
        model.add_text("{}".format(text), dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')

        # create tower name
        attribs = {"height": self._parameters.TextHeight}
        x = X0 + 0.05 * self._parameters.ColumnWidth
        y = Y0 - self._parameters.TitleHeight - self._parameters.HeaderHeight / 2.0
        text = "PYLÔNE : {}".format(self._model.get_tower_name())
        model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_LEFT')

        # create line angle
        attribs = {"height": self._parameters.TextHeight}
        x = X0 + 0.05 * self._parameters.ColumnWidth + 3. * self._parameters.ColumnWidth
        y = Y0 - self._parameters.TitleHeight - self._parameters.HeaderHeight / 2.0
        text = u"ANGLE : {}\N{DEGREE SIGN}".format(load_case.get_line_angle(), ".2f")
        model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_LEFT')

        # create deviation angle
        attribs = {"height": self._parameters.TextHeight}
        x = X0 + 0.05 * self._parameters.ColumnWidth + 6 * self._parameters.ColumnWidth
        y = Y0 - self._parameters.TitleHeight - self._parameters.HeaderHeight / 2.0
        text = u"DÉVIATION : {}\N{DEGREE SIGN}".format(load_case.get_line_angle(), ".2f")
        model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_LEFT')

        # create weight spans
        text = "PP = {:.1f} ({:.1f} / {:.1f})".format(*load_case.get_weight_spans())
        self._create_table_footer(0, case_index, X0, Y0, text)

        # create wind spans
        text = "PP = {:.1f} ({:.1f} / {:.1f})".format(*load_case.get_wind_spans())
        self._create_table_footer(1, case_index, X0, Y0, text)

        # create climatic loads
        text = "GLACE = {:.1f}    VENT = {:.3f}    TEMP. = {:.1f}\N{DEGREE SIGN}    ALPHA = {:.1f}".format(load_case.get_ice_thickness(),
                                                                                                           load_case.get_wind_pressure(),
                                                                                                           load_case.get_temperature(),
                                                                                                           load_case.get_alpha_factor())
        self._create_table_footer(2, case_index, X0, Y0, text)

        # create load factors fma/fmb
        text = "MAJORATION DES CHARGES : FMA = {:.2f}    FMB = {:.2f}".format(load_case.get_fma_factor(),
                                                                              load_case.get_fmb_factor())
        self._create_table_footer(3, case_index, X0, Y0, text)

        # create gravity load set
        text = "CHARGES DE GRAVITÉ SUR LE PYLÔNE : P2"
        self._create_table_footer(4, case_index, X0, Y0, text)

        # create wind load set
        text = "CHARGES DE VENT SUR LE PYLÔNE : HT1"
        self._create_table_footer(5, case_index, X0, Y0, text)

        # create loads
        attribs = {"height": self._parameters.TextHeight}
        for i in range(load_case.nb_load_points()):

            load_point = load_case.get_load_point(i)

            # id
            x = X0 + self._parameters.ColumnWidth / 2.0
            y = Y0 - self._parameters.LineHeight * 1.5 - self._parameters.HeaderHeight
            y += - (i+1) * self._parameters.LineHeight - self._parameters.TitleHeight
            text = "{}".format(i+1)
            model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')

            for j in range(3):
                # transversal
                x = X0 + self._parameters.ColumnWidth / 2.0 + (j * 3 + 1) * self._parameters.ColumnWidth
                text = "{:.1f}".format(load_point.get_transversal_loads()[j])
                model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')
                # longitudinal
                x = X0 + self._parameters.ColumnWidth / 2.0 + (j * 3 + 2) * self._parameters.ColumnWidth
                text = "{:.1f}".format(load_point.get_longitudinal_loads()[j])
                model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')
                # vertical
                x = X0 + self._parameters.ColumnWidth / 2.0 + (j * 3 + 3) * self._parameters.ColumnWidth
                text = "{:.1f}".format(load_point.get_vertical_loads()[j])
                model.add_text(text, dxfattribs=attribs).set_pos((x, y), align='MIDDLE_CENTER')

    def _initialize_dxf(self):
        self._dxf = ezdxf.new("R2010")
        if self._parameters.LayerName != "0":
            # !!! create only a layer if name != 0. Exists by default.
            attributes = {}
            # set 'linetype' attributes for dxf
            if self._parameters.LineType == DXFDrawingParameters.LineType_CONTINUOUS:
                attributes["linetype"] = "CONTINUOUS"
            else:
                attributes["linetype"] = "CONTINUOUS"
            # set 'color' attributes for dxf
            if self._parameters.LineColor == DXFDrawingParameters.LineColor_WHITE:
                attributes["color"] = 0
            else:
                self._e
                attributes["color"] = 0
            self._dxf.layers.new(name=self._parameters.LayerName,
                                 dxfattribs=attributes)

    def _table_height(self, load_case):
        h = self._parameters.TitleHeight
        h += self._parameters.HeaderHeight
        h += (2. + load_case.nb_load_points()) * self._parameters.LineHeight
        h += 8. * self._parameters.LineHeight
        return h

    def _table_nb_columns(self):
        # table always have 10 columns
        return 10

    def _table_width(self):
        return self._table_nb_columns() * self._parameters.ColumnWidth

    def error_code(self):
        return self._error_code

    def error_string(self):
        return self._error_string

    def filename(self):
        return self._filename

    def is_done(self):
        return self._is_done

    def model(self):
        return self._model

    def parameters(self):
        return self._parameters

    def process(self):
        self._initialize_dxf()
        for i in range(self._model.nb_load_cases()):
            if not self._create_table(i):
                self._error_code = self.ERROR_FailToProcessTable
                self._error_string = "Fail to process table {} in data model".format(i)
                return False
        self._is_done = True
        return True

    def save(self):
        if not self._is_done:
            self.process()
        if not self._dxf:
            self._error_code = self.ERROR_InvalidDXF
            self._error_string = "Cannot save file. Invalid DXF object."
            return False
        self._dxf.saveas(self._filename)
        return True


class Engine(object):
    """
    Class implementation of an engine for the application.
    """

    def __init__(self):
        # hold data models internally
        self._models = {}
        self._error_code = 0
        self._error_string = ""


    def create_dxf_file(self, model_id, filename):
        # get a reference to a data model
        model = self.get_data_model(model_id)
        # create drawing builder
        builder = DXFDrawingBuilder(model, filename)
        return builder.save()

    def create_xls_file(self, model_id, filename):
        raise NotImplementedError()

    def get_data_model(self, model_id, force=True):
        if model_id in self._models.keys():
            model = self._models[model_id]
            return model
        elif force:
            model = DataModel()
            self._models[model_id] = model
            return model
        else:
            return None

    def get_free_model_id(self):
        id = 1
        while id in self._models.keys():
            id += 1
        return id

    def get_nb_models(self):
        return len(self._models.keys())

    def new_data_model(self, model_id):
        if model_id in self._models.keys():
            self._models.pop(model_id)
        model = DataModel()
        self._models[model_id] = model
        return model

    def import_from_chacal_crs(self, model_id, filename):
        # get a reference to a data model
        model = self.get_data_model(model_id)
        # create parser
        parser = ChacalCRSFileParser(model, filename)
        return parser.process()

    def remove_data_model(self, model_id):
        if not model_id in self._models.keys():
            return False
        del self._models[model_id]
        return True





