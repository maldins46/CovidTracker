#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uses the library to generate all available charts in the ./docs/ directory.
@author: riccardomaldini
"""
import regions.analysis as regions_analysis
import provinces.analysis as provinces_analysis
import national.analysis as national_analysis

national_analysis.compute_national_data(save_image=True, show=False)
national_analysis.compute_ti_occupation(save_image=True, show=False)
regions_analysis.compute_ti_occupation_per_regions(save_image=True, show=False)
regions_analysis.compute_daily_cases(save_image=True, show=False)
regions_analysis.compute_rec_with_symptoms(save_image=True, show=False)
regions_analysis.compute_death(save_image=True, show=False)
regions_analysis.compute_marche_data(save_image=True, show=False)
provinces_analysis.compute_total_cases_per_provinces(save_image=True, show=False)
provinces_analysis.compute_total_cases_per_provinces_abs(save_image=True, show=False)
