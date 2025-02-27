#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" This is the launcher module of Biovarase."""
import sys
import profile
import pstats
import frames.main as main

__author__ = "Mainak Chaudhuri"
__copyright__ = "MV-2025"
__credits__ = ["MainakVerse",]
__license__ = "GNU GPL Version 3, 2 Jan 2023"
__version__ = "4.2"
__maintainer__ = "MainakRepositor"
__email__ = "mainakchaudhuri671@gmail.com"
__date__ = "2025-02-26"
__status__ = "Production"

if len(sys.argv)>1:
    profile.run('main.main()', 'profile_results')
    p = pstats.Stats('profile_results')
    p.sort_stats('cumulative').print_stats(10)
else:
    main.main()
    
