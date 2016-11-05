import MaxPainstd
import ConfigParser
import logging
import sqlite3
import pandas as pd

logging.basicConfig(
    filename=MaxPainstd.LOGFILE,
    level=logging.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')

config = ConfigParser.ConfigParser()
config.read(MaxPainstd.cfgpath)


lastDayData = pd.read_csv(config.get('Settings', 'spyoptfile'))

def frameScrape(headers):

    for col in headers:

print ('Headers=',list(lastDayData) )
# JKSeries = pd.Series(lastDayData['PutsOI'])
# pd.to_numeric(JKSeries, errors='coerce')
# JKSeries = (lastDayData['PutsOI']!= '-').astype(int)
# JK1 = lastDayData[lastDayData.PutsOI != '-']
# JK2 = JK1[JK1.PutsVolume != '-']
# JK3 = JK2[JK2.CallsOI != '-']
# JK4 = JK3[JK3.CallsVolume != '-']

# lastDayData = lastDayData[lastDayData.PutsOI != '-']
# lastDayData = lastDayData[lastDayData.PutsVolume != '-']
# lastDayData = lastDayData[lastDayData.CallsOI != '-']
# lastDayData = lastDayData[lastDayData.CallsVolume != '-']

# JK = lastDayData['PutsOI'].convert_objects(convert_numeric=True)
#
# try:
#     conn = sqlite3.connect(config.get('Settings', 'oidatabase'))
#     # conn.text_factory = str
#     cur = conn.cursor()
#
#     oi_frame = lastDayData[
#         ['ExpirationDate', 'CallsLastPrice', 'CallsVolume', 'CallsOI', 'Strike', 'PutsLastPrice', 'PutsVolume',
#          'PutsOI']]
#
#     oi_frame.to_sql('t_LastDayOI', conn, if_exists='replace')
#     conn.commit()
#     conn.close()
# except sqlite3.Error as er:
#     # Something is wrong with the database
#     print 'er', er.message
#
# lastDayData.to_csv('JKSeries.csv')
# print lastDayData.head()
