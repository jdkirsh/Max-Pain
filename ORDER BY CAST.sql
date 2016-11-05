CREATE TABLE [t_10OIPuts] AS SELECT [Index], 
       [ExpirationDate], 
       [Strike], 
       [PutsOI], 
       [PutsVolume]
FROM   [t_LastDayOI]
ORDER  BY CAST ([PutsOI] AS [DECIMAL]) DESC
LIMIT 10;

