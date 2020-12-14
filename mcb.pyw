#! python3
# mcb.pyw - save and loads pieces of text to the clipboard
# usage: py.exe mcb.pyw save<keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> -Loads keyword to clipboard
#        py.exe moc.pyw list - loads all keywords to clipboard
'''
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# todo: save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower()=='save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# todo: list keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
# todo: list keywords and load content.

mcbShelf.close()

import zipfile, os
os.chdir('C:\\Users\\sybcf\\Desktop') #move to the folder with wm.zip
wmZip = zipfile.ZipFile('wm.zip')
print(wmZip.namelist())
'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - % (levelname)s - %(message)s')
