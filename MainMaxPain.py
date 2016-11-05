import MaxPainstd
import logging


logging.basicConfig(
    filename=LOGFILE,
    level=logging.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')

# cfgpath = 'C:\FINANCE\Python\PyCharm\Projects\DailySPYrun\DailySPYrun.cfg'
config = ConfigParser.ConfigParser()
config.read(DailyOIstd.cfgpath)
