import MaxPainstd
import os
import pandas as pd
import csv
import sqlite3
import ConfigParser
import logging

logging.basicConfig(
    filename=MaxPainstd.LOGFILE,
    level=logging.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)

config = ConfigParser.ConfigParser()
config.read(MaxPainstd.cfgpath)

SPYoptFile = config.get('Settings', 'SPYoptFile')
DATABASE = config.get('Settings', 'OIdatabase')

try:
    conn = sqlite3.connect(DATABASE)
    TopPuts = pd.read_sql('SELECT * FROM t_10OIPuts', conn)
except sqlite3.Error as er:
    # Something is wrong with the database
    print 'er', er.message
TopPuts.to_csv(config.get('Settings', 'oiPutsFile'),sep=',')

try:
    conn = sqlite3.connect(DATABASE)
    TopPuts = pd.read_sql('SELECT * FROM t_10OICalls', conn)
except sqlite3.Error as er:
    # Something is wrong with the database
    print 'er', er.message
TopPuts.to_csv(config.get('Settings', 'oiCallsFile'),sep=',')
