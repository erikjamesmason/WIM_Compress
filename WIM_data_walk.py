########################################################################################################################
# WIM Data Walk Data Script
# Authored by: Erik Mason
# Authored on: April 30, 2020
# WIM Sites Targeted: Tudor (tds), Palmer (plm), Sterling (ste), Tok (Tok), cont->
# Port of Anchorage (poa), New Seward Highway (nsh)
#
#
########################################################################################################################

import os
import zipfile
import datetime
import logging
from pathlib import Path

from datetime import date

today = datetime.datetime.now().strftime("%y-%m-%d")

WIM_zip = zipfile.ZipFile('C:\\Users\\ejmason\\Desktop\\WIM_Migration_TS_' + str(today) + '_WIM.zip', 'w')


# begin logging section

logging.basicConfig(filename='wim_migration_2020.log', format='%(message)s', filemode='a', level=logging.INFO)
filename = ''


########################################################################################################################
# tds for loop
for folder, subfolder, files in os.walk('Z:'):

    counter = 0
    for file in files:
        log = open('wim_migration_2020.log', 'r')
        file = str(Path(file))
        if file not in log.read() and file.startswith('2015') \
                or file.startswith('2016')\
                or file.startswith('2017')\
                or file.startswith('2018'):
            if file.endswith('.tds') or file.endswith('.TDS') \
                    or file.endswith('.ste') or file.endswith('.STE')\
                    or file.endswith('.poa') or file.endswith('.POA')\
                    or file.endswith('.nsh') or file.endswith('.NSH')\
                    or file.endswith('.plm') or file.endswith('.PLM')\
                    or file.endswith('.tok') or file.endswith('.TOK')\
                    or file.endswith('.glh') or file.endswith('.GLH'):
                spcfile = file
                WIM_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'Z:'),
                              compress_type=zipfile.ZIP_DEFLATED)
                counter += 1
                print(str(counter) + ' - ' + str(spcfile))
                filename = file
                logging.info(f'{filename}')
        else:

            pass
    print('Total WIM Files: ' + str(counter))

# end wim for loop
########################################################################################################################