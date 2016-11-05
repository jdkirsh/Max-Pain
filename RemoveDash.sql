--INSERT INTO t_Top10Puts 
--AS 
SELECT t_LastDayOI.RecDateTime, ExpirationDate, Strike, PutsLastPrice, PutsOI, PutsVolume
FROM t_LastDayOI
ORDER BY PutsOI LIMIT 10 