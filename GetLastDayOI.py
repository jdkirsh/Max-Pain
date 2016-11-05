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

lastDayData = '''
SELECT *
FROM   [OpenInterest]
WHERE  [OpenInterest].[ExpirationDate] = (SELECT DISTINCT MAX ([OpenInterest].[ExpirationDate])
       FROM   [OpenInterest])
'''


def get_TableSql(SqlName, DataBase):
    db = sqlite3.connect(DataBase)
    TableFrame = pandas.read_sql(SqlName, db)
    db.close()
    return TableFrame

def get_oi_calls():
    _oiFrame = get_TableSql(lastDayData, config.get('Settings', 'oidatabase'))
    _oiCalls = _oiFrame[['Strike','CallsOI']]
    return _oiCalls

def get_oi_puts():
    _oiFrame = get_TableSql(lastDayData, config.get('Settings', 'oidatabase'))
    _oiPuts = _oiFrame[['Strike', 'PutsOI']]
    return _oiPuts

# def _get_N_Largest(pdArray, N):

######################## Main ########################
if __name__ == '__main__':

    oiFrame = get_TableSql(lastDayData, config.get('Settings', 'oidatabase'))
    oiFrame.to_csv(config.get('Settings','oiFile'),sep=',',encoding='utf=8')
    get_oi_puts().to_csv(config.get('Settings','oiPutsFile'),sep=',',encoding='utf=8')
    get_oi_calls().to_csv(config.get('Settings','oiCallsFile'),sep=',',encoding='utf=8')


