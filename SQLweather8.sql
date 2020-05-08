SELECT distinct CITY FROM STATION WHERE (
    CITY LIKE 'a%' 
        and( city like '%a' or City like '%e'or City like '%i' or City like '%o' or City like '%u')
or CITY LIKE 'E%' 
        and( city like '%a' or City like '%e'or City like '%i' or City like '%o' or City like '%u')
or CITY LIKE 'i%' 
        and( city like '%a' or City like '%e'or City like '%i' or City like '%o' or City like '%u')
or CITY LIKE 'o%' 
        and( city like '%a' or City like '%e'or City like '%i' or City like '%o' or City like '%u')
or CITY LIKE 'u%' 
        and( city like '%a' or City like '%e'or City like '%i' or City like '%o' or City like '%u'));


/*
SELECT DISTINCT CITY FROM STATION WHERE (
CITY LIKE 'a%' OR CITY LIKE 'e%' OR CITY LIKE 'i%' OR CITY LIKE 'o%' OR CITY LIKE 'u%') 
AND 
(CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' OR CITY LIKE '%u');
*/
