# -*- coding: utf-8 -*-
"""
@Time        : 16/11/2020
@Author      : sybcf
@File        : backupToZip
@Description : 
"""
import zipfile, os


def backupToZip(folder):
    # backup the entire contents of 'folder' into a ZIP file
    folder = os.path.abspath(folder) # make sure folder is absolute

    # figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # todo: create the ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # todo: walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
    for filename in filenames:
        newBase / os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue # don't backup the backup ZIP files
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('D:/JJ')