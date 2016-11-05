SELECT * FROM OpenInterest WHERE OpenInterest.RecDateTime = 
(SELECT MAX(OpenInterest.RecDateTime) FROM OpenInterest)