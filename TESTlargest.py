import MaxPainstd
import ConfigParser
import logging
import sqlite3
import pandas

# config = ConfigParser.ConfigParser()
# config.read(MaxPainstd.cfgpath)

logging.basicConfig(
    filename=MaxPainstd.LOGFILE,
    level=logging.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')

config = ConfigParser.ConfigParser()
config.read(MaxPainstd.cfgpath)

oiPuts = pandas.read_csv((config.get('Settings', 'oiPutsFile')) )

print oiPuts.head()

# oiPuts['PutsOI'].replace('-',0,inplace=True)
# oiPuts['PutsOI'].convert_objects(convert_numeric=True)
# oiPuts['PutsOI'].astype(float)

oiPuts['PutsOI'].replace('-',0,inplace=True)

oiPutsLargest = oiPuts.nlargest(5, 'PutsOI')

print oiPutsLargest.head(12)
