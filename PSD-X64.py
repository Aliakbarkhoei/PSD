# This app was created by Aliakbar Zeinali.
# Copyright: All right's reserved.
# Python ver 3.10.1
# This program is made for NVDA Screen reader and is used for better Persian pronunciation in that.

import time # Time library; used for stops in this app..
import os # os library; a library for working with files.

ADP = str(os.getenv('APPDATA')) # Gets User AppData path which is required for this program; str(...) convert it to String.
DFP = ADP + "\\nvda\\speechDicts\\voiceDicts.v1\\espeak\\espeak-Persian.dic" # Persian Speech Dictionary path.
OpenReffrence = open("reffrence.txt", "r") # Reffrence for edit.
OpenDicFile = open(DFP, "a") # open Dictionary file for edit.
ODFAppend = open(DFP, "r") # open Dictionary file for search the characters.
CLDR = open(r"c:\Program Files (x86)\nvda\locale\fa\cldr.dic", "w") # open cldr; a file for Symbels.
CLDRReffrence = open("reffrenceCLDR.txt", "r") # CLDR's reffrence
ReadCR = CLDRReffrence.read() # reads CLDR Reffrence.
CLDR.write(ReadCR) # Writes reffrences content to CLDR.
CLDR.close() # close CLDR file.
CLDRReffrence.close() # close CLDR's Reffrence file.
os.remove("reffrenceCLDR.txt") # remove CLDR's Reffrence file.
SYM = open(r"c:\Program Files (x86)\nvda\locale\fa\symbols.dic", "w") # open another file for symbels.
SYMReffrence = open("reffrenceSymbels.txt", "r") # Reffrence for this file.
ReadSR = SYMReffrence.read() # Reads the reffrence.
SYM.write(ReadSR) # Writes reffrences content to the file.
SYM.close() # close the file.
SYMReffrence.close() # close the Reffrence file.
os.remove("reffrenceSymbels.txt") # Removes the Reffrence file because we won't need it.
ReadOR = OpenReffrence.read() # reads dictionary reffrence file.
ODAppend = ODFAppend.read() # reads Dictionary file.
Rep=[2] # report variable.
if (ReadOR in ODAppend): # checks if the character is in Dictionary file
	OpenDicFile.close()
	ODFAppend.close()
	OpenReffrence.close()
	# closed the files
	print("It is exist")
	Rep=[0] # report = false.
	os.remove("reffrence.txt") # Removes the reffrence file because we won't need it.
else: # if the character isn't in the dictionary.
	OpenDicFile.write(ReadOR) # Add character to dictionary.
	Rep=[1] # report = true.
	OpenReffrence.close()
	os.remove("reffrence.txt")

if 1 in Rep: # if report is true
	Report = "با موفقیت نصب شد."
	print(Report)
elif 0 in Rep: # if report is false
	Report = "این دیکشنری قبلا نصب شده است."
	print(Report)
else: # if app didn't any thing, maybe an error.
	Report = "خطا."
	print(Report)
time.sleep(4) # stops four seconds.
print("برای لغوِ‌نصبِ این برنامه، بر روی آیکن UPd در Desktop کلیک کنید. با تشکر از نصب این برنامه.")
time.sleep(4) # stops four seconds.
