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

# ######################## Main ########################
if __name__ == '__main__':

    try:
        conn = sqlite3.connect(DATABASE)
        Data = pd.read_sql('SELECT Strike, CallsOI, PutsOI FROM t_LastDayOI' , conn)
    except sqlite3.Error as er:
        # Something is wrong with the database
        print 'er', er.message

    Data.insert(2, 'CallsCash',0)
    Data.insert(4,'PutsCash',0)

    print Data.head()

    loc = 5
    for i in Data.Strike:
        # print ('loc=',loc,'i=',i)
        Data.insert(loc,i,0)
        loc += 1
    Data['CallsOI'].replace('-',0,inplace=True)
    Data['PutsOI'].replace('-', 0, inplace=True)


    # print Data.CallsOI.head()
    Data.to_csv('Data.csv')
