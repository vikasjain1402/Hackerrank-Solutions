
select (select count(city) from station ) - (select count(distinct city) from station);



