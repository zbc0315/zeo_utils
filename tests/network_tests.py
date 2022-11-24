#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 11/24/2022 3:02 PM
# @Author  : zhangbc0315@outlook.com
# @File    : network_tests.py
# @Software: PyCharm

import unittest

from zeo_utils import Network


class NetworkTests(unittest.TestCase):

    network = Network('../example/network.exe')
    cif_fp = '../example/31.cif'

    def test_calc_pore_diameter(self):
        pdm = self.network.calc_pore_diameter(self.cif_fp)
        self.assertTrue(pdm.startswith('High accuracy requested'))

    def test_calc_specific_surface_are(self):
        ssa = self.network.calc_specific_surface_area(self.cif_fp, 1.2, 1.2, 2000)
        self.assertTrue(ssa.startswith('High accuracy requested'))

    def test_calc_accessible_volume(self):
        av = self.network.calc_accessible_volume(self.cif_fp, 0.0, 0.0, 100000)
        self.assertTrue(av.startswith('High accuracy requested'))

    def test_calc_pore_size_distribution(self):
        psd = self.network.calc_pore_size_distribution(self.cif_fp, 0.5, 0.5, 100000)
        print()
        self.assertTrue(psd.startswith('High accuracy requested'))


if __name__ == "__main__":
    unittest.main()
