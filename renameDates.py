# -*- coding: utf-8 -*-
"""
@Time        : 16/11/2020
@Author      : sybcf
@File        : renameDates
@Description : 
"""
import shutil, os, re
datePattern = re.compile(r'''^(.*?)  #all text before the date.
((0|1)?\d)-                          # one or two digits for the month
((0|1|2|3)?\d)-                      # one ro two digits for the day
((19|20)\d\d)                       #four digits for the year 
(.*?)$                              # all text after the date
''', re.VERBOSE)
# TODO: loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# todo: skip files without a date
    if mo == None:
        continue
# todo: get the different parts of teh filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
# todo: form the european style filenaeme
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# todo : get the full absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # todo: rename the files.
    print('Renaming "%s to "%s"... ' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing