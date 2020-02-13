########################################################################################################################
# WIM File Management Script
# Authored by: Erik Mason
# Authored on: December 28, 2019
# WIM Sites Targeted: gnc, gnm, gsc, gsm, fox, plm
#
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

WIM_zip = zipfile.ZipFile('Z:\\EJMcompressedWIM\\' + str(today) + '_WIM.zip', 'w')

# begin logging section

logging.basicConfig(filename='wim_import_2020.log', format='%(message)s', filemode='a', level=logging.INFO)
filename = ''

#####################################
# begin WIM Stations 'for' loops#
#####################################

########################################################################################################################
# gsc for loop
for folder, _, files in os.walk('Z:\\gsc\\2020'):

    countergsc = 0

    for file in files:
        log = open('wim_import_2020.log', 'r')
        file = Path(file).stem + ".gsc"
        if file not in log.read():

            if file.endswith('.gsc') or file.endswith('.GSC'):
                WIM_zip.write(os.path.join(folder, file),
                                  os.path.relpath(os.path.join(folder, file), 'Z:\\gsc\\2020'),
                                  compress_type=zipfile.ZIP_DEFLATED)
                countergsc += 1
            print(str(countergsc) +' - '+ str(file))
            filename = file
            logging.info(f'{filename}')
        else:

            pass
    print('Total for gsc: ' + str(countergsc))

########################################################################################################################
# gsm for loop
for folder, _, files in os.walk('Z:\\gsm\\2020'):

    countergsm = 0

    for file in files:
        log = open('wim_import_2020.log', 'r')
        file = Path(file).stem + ".gsm"
        if file not in log.read():
            if file.endswith('.gsm') or file.endswith('.GSM'):
                WIM_zip.write(os.path.join(folder, file),
                                  os.path.relpath(os.path.join(folder, file), 'Z:\\gsm\\2020'),
                                  compress_type=zipfile.ZIP_DEFLATED)
                countergsm += 1
            print(str(countergsm) +' - '+ str(file))
            filename = file
            logging.info(f'{filename}')
        else:

            pass
    print('Total for gsm: ' + str(countergsm))
########################################################################################################################
# gnm for loop
for folder, _, files in os.walk('Z:\\gnm\\2020'):

    countergnm = 0

    for file in files:
        log = open('wim_import_2020.log', 'r')
        file = Path(file).stem + ".gnm"
        if file not in log.read():
            if file.endswith('.gnm') or file.endswith('.GNM'):
                WIM_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'Z:\\gnm\\2020'),
                              compress_type=zipfile.ZIP_DEFLATED)
                countergnm += 1
            print(str(countergnm) +' - '+ str(file))
            filename = file
            logging.info(f'{filename}')
        else:

            pass
    print('Total for gnm: ' + str(countergnm))

########################################################################################################################
# gnc for loop
for folder, _, files in os.walk('Z:\\gnc\\2020'):

    countergnc = 0

    for file in files:
        log = open('wim_import_2020.log', 'r')
        file = Path(file).stem + ".gnc"
        if file not in log.read():
            if file.endswith('.gnc') or file.endswith('.GNC'):
                WIM_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'Z:\\gnc\\2020'),
                              compress_type=zipfile.ZIP_DEFLATED)
                countergnc += 1
            print(str(countergnc) +' - '+ str(file))
            filename = file
            logging.info(f'{filename}')
        else:

            pass
    print('Total for gnc: ' + str(countergnc))

########################################################################################################################
# fox for loop
for folder, _, files in os.walk('Z:\\fox\\2020'):

    counterfox = 0

    for file in files:
        log = open('wim_import_2020.log', 'r')
        file = Path(file).stem + ".fox"
        if file not in log.read():
            if file.endswith('.fox') or file.endswith('.FOX'):
                WIM_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'Z:\\fox\\2020'),
                              compress_type=zipfile.ZIP_DEFLATED)
                counterfox += 1
            print(str(counterfox) +' - '+ str(file))
            filename = file
            logging.info(f'{filename}')
        else:

            pass
    print('Total for fox: ' + str(counterfox))

########################################################################################################################
# plm for loop
for folder, _, files in os.walk('Z:\\plm\\2020'):

    counterplm = 0

    for file in files:
        log = open('wim_import_2020.log', 'r')
        file = Path(file).stem + ".plm"
        if file not in log.read():
            if file.endswith('.plm') or file.endswith('.PLM'):
                WIM_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'Z:\\plm\\2020'),
                              compress_type=zipfile.ZIP_DEFLATED)
                counterplm += 1
            print(str(counterplm) +' - '+ str(file))
            filename = file
            logging.info(f'{filename}')
        else:

            pass
    print('Total for plm: ' + str(counterplm))

########################################################################################################################
#####################################
# Begin ending scripts with console #
#####################################

# station count
station_count = [counterplm, countergnc, counterfox, countergnm, countergsm, countergsc]

# visual check for console for amount of days per station and total files for all stations combined
print('Total Files: ' + str(counterplm + countergnc + counterfox + countergnm + countergsm + countergsc)
      + ' file by ' + str(len(station_count)) + ' stations')

# close the zip process
WIM_zip.close()