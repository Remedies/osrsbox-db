# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2019/01/19

Description:
Join directory of single JSON files with beast_name -> beast_wikitext

Copyright (c) 2019, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

>>> CHANGELOG:
    1.0.0       Base functionality
"""

__version__ = "1.0.0"

import os
import json
import glob

################################################################################
if __name__=="__main__":   
    wikitext_fis_path = "extract_all_bestiary_page_wikitext" + os.sep + "*"
    wikitext_fis = glob.glob(wikitext_fis_path)

    all_beasts = dict()
    for fi in wikitext_fis:
        with open(fi) as f:
            data = json.load(f)
            beast_name = next(iter(data))
            beast_wikitext = data[beast_name]
            all_beasts[beast_name] = beast_wikitext
             
    with open("extract_all_bestiary_page_wikitext.json", "w") as fi:
        json.dump(all_beasts, fi)
