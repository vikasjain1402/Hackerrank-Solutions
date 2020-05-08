select country.continent ,truncate(avg(city.population),0) as dd
from city
left join country on city.countrycode=country.code
group by country.continent having country.continent is not NULL
order by dd 
