#!/usr/bin/env python
# coding: utf8
#
# Copyright (c) 2020 Centre National d'Etudes Spatiales (CNES).
#
# This file is part of Shareloc
# (see https://github.com/CNES/shareloc).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#-------------------------------------------------------------------------------

import numpy as np


class Localization:
    """ base class for localization function.
    Underlying model can be both multi layer localization grids or RPCs models
    """
    def __init__(self, model, dtm = None):
        """
        constructor
        :param model : geometric model
        :type model  : shareloc.grid or  shareloc.rpc
        :param dtm  : dtm (optional)
        :type dtm  : shareloc.dtm
        """
        self.dtm = dtm
        self.use_rpc = model.type is 'rpc'
        self.model = model


    def direct(self, row, col, h):
        """
        direct localization
        :param row :  sensor row
        :param col : sensor col
        :param h: altitude
        :return coordinates : [lon,lat,h] (3D np.array)
        """

        return self.model.direct_loc_h(row,col,h)

    def direct_dtm(self, row, col):
        """
        forward localization on dtm
        :param row : sensor row
        :param col : sensor col
        :return coordinates : [lon,lat,h] (3D np.array)
        """
        if self.use_rpc == True:
            print('forward_dtm not yet impelemented for RPC model')
            return None
        else:
            if self.dtm is not None:
                return self.model.direct_loc_dtm(row,col, self.dtm)
            else:
                print('direct_loc_dtm needs a dtm')
                return None

    def inverse(self,lon,lat,h):
        """
        inverse localization
        :param lat :  latitude
        :param lon : longitude
        :param h : altitude
        :return coordinates : [row,col,valid] (2D np.array), valid == 1 if coordinates is valid
        :rtype numpy.array
        """

        if self.use_rpc == False and not hasattr(self.model, 'pred_ofset_scale_lon'):
            self.model.estimate_inverse_loc_predictor()
        return self.model.inverse_loc(lon,lat,h)



