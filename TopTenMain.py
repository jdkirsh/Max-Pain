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


topPuts = '''
DROP TABLE IF EXISTS t_10OIPuts;
CREATE TABLE [t_10OIPuts] AS SELECT [Index],
       [ExpirationDate],
       [Strike],
       [PutsOI],
       [PutsVolume]
FROM   [t_LastDayOI]
ORDER  BY CAST ([PutsOI] AS [DECIMAL]) DESC
LIMIT 10;
'''

topCalls = '''
DROP TABLE IF EXISTS t_10OICalls;
CREATE TABLE [t_10OICalls] AS SELECT [Index],
       [ExpirationDate],
       [Strike],
       [CallsOI],
       [CallsVolume]
FROM   [t_LastDayOI]
ORDER  BY CAST ([CallsOI] AS [DECIMAL]) DESC
LIMIT 10;
'''


emptyLastDayIO = '''
DELETE FROM t_LastDayOI ;
'''

emptyTop10Calls = '''
DELETE FROM t_Top10OICalls ;
'''

emptyTop10Puts = '''
DELETE FROM t_Top10OIPuts
'''


def doSQLscript(sql_script):
    try:
        conn = sqlite3.connect(config.get('Settings', 'oidatabase'))
        cur = conn.cursor()
        cur.executescript(sql_script)
        conn.commit()
        conn.close()
    except sqlite3.Error as er:
        # Something is wrong with the database
        logger.debug("sqlite Err: %s", er.message, exc_info=True)
        print 'er', er.message
        conn.close

def doSQL(sqlText):
    try:
        conn = sqlite3.connect(config.get('Settings', 'oidatabase'))
        cur = conn.cursor()
        cur.execute(sqlText)
        conn.commit()
        conn.close()
    except sqlite3.Error as er:
        # Something is wrong with the database
        logger.debug("sqlite Err: %s", er.message, exc_info=True)
        print 'er', er.message
        conn.close


def loadLastDay():
    logger.debug('In loadLastDay')
    Dailyframe = pd.read_csv(SPYoptFile)
    #Dailyframe = pd.read_csv(SPYoptFile, index_col = False)
    try:
        conn = sqlite3.connect(DATABASE)
        conn.text_factory = str
        cur = conn.cursor()

        # oi_frame = Dailyframe[['Index', 'ExpirationDate','CallsLastPrice', 'CallsVolume', 'CallsOI', 'Strike', 'PutsLastPrice', 'PutsVolume', 'PutsOI']]
        oi_frame = Dailyframe[['ExpirationDate', 'CallsLastPrice', 'CallsVolume', 'CallsOI', 'Strike', 'PutsLastPrice','PutsVolume', 'PutsOI']]
        # oi_frame.to_sql('OpenInterest', conn, if_exists='append',index_label=False, index=False)
        oi_frame.to_sql('t_LastDayOI', conn, if_exists='append')
        conn.commit()
        conn.close()
    except sqlite3.Error as er:
        # Something is wrong with the database
        logger.debug("sqlite Err: %s",er.message, exc_info=True )
        print 'er', er.message


# ######################## Main ########################
if __name__ == '__main__':
    logging.debug('In %s',__file__)
    logging.debug('Calling doSQL(emptyLastDayIO)...')
    doSQL(emptyLastDayIO)
    # doSQL(emptyTop10Calls)
    # doSQL(emptyTop10Puts)
    logging.debug('Calling loadLastDay()...')
    loadLastDay()
    logging.debug('Calling doSQLscript(topCalls)...')
    doSQLscript(topCalls)
    logging.debug('Calling doSQLscript(topPuts)...')
    doSQLscript(topPuts)

    logging.debug('Generating TopPuts File...')
    try:
        conn = sqlite3.connect(DATABASE)
        TopPuts = pd.read_sql('SELECT * FROM t_10OIPuts', conn)
    except sqlite3.Error as er:
        # Something is wrong with the database
        print 'er', er.message
    TopPuts.to_csv(config.get('Settings', 'oiPutsFile'),sep=',')

    logging.debug('Generating TopCalls File...')
    try:
        conn = sqlite3.connect(DATABASE)
        TopPuts = pd.read_sql('SELECT * FROM t_10OICalls', conn)
    except sqlite3.Error as er:
        # Something is wrong with the database
        print 'er', er.message
    TopPuts.to_csv(config.get('Settings', 'oiCallsFile'),sep=',')
