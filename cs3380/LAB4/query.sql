/* 1. Find the district and population of all cities named Springfield. Sort results from most populous to
least populous. (3 results)
2. Find the name, district, and population of each city in Brazil (country code BRA). Order results by
city name alphabetically. (250 results)
3. Find the name, continent, and surface area of the smallest countries by surface area. Order by surface
area with smallest first. Return only 20 countries. (20 results)
4. Find the name, continent, form of government, and GNP of all countries having a GNP greater than
200,000. Sort the output by the name of the country in alphabetical order from A to Z. (23 results)
5. Find the 10 countries with the 10th through 19th best life expectancy rates. You should use WHERE
life expectancy IS NOT NULL to remove null values when querying this table. (10 results)
6. Find all city names that start with the letter B and ends in the letter s. Results should be ordered
from largest to smallest population, but do not display the population field. (12 results)
7. Return the name, name of the country, and city population of each city in the world having population
greater than 6,000,000. Order results by the city population with the most populous first. (20 results)
8. Find the name, independence year, and region of all countries where English is an official language.
Order results by region ascending and alphabetize the results within each region by country name. (44
results)
9. For each country display the capital city name and the percentage of the population that lives in the
capital for each country. Sort the results from largest percentage to smallest percentage. (Hint: Don’t
be surprised if there are some countries with a percentage greater than 100% due to errors in the data.)
(232 results)
10. Find all official languages, the country for which it is spoken, and the percentage of speakers (percentage
of speakers is calculated as percentage spoken times country population divided by 100). Order results
by the total number of speakers with the most popular language first. (238 results)
11. Find the name, region, GNP, old GNP, and real change in GNP for the countries who have most
improved their relative wealth. the real change in GNP is defined as (gnp - gnp old)/gnp old. Order
results by real change with the most improved country first. Also, this data is missing some entries for
gnp and gnp old. Filter these missing entries out by only returning countries where gnp IS NOT NULL
and gnp old IS NOT NULL. (178 results)
*/
#1
SELECT Name, District, Population FROM City 
WHERE Name = 'Springfield' 
ORDER BY population DESC;
#2
SELECT Name, District,Population FROM City
WHERE 	CountryCode='BRA'
ORDER BY Name ASC;
#3
SELECT Name, Continent, SurfaceArea FROM Country
ORDER BY SurfaceArea ASC
LIMIT 20;
#4
SELECT Name, Continent, GovernmentForm, GNP FROM Country
WHERE GNP>200000
ORDER BY Name ASC;
#5
SELECT countries FROM world
WHERE NOT NULL
ORDER BY life expectancy DESC
LIMIT 10 OFFSET 9; 
#6
SELECT city FROM world




#7
SELECT countries FROM world
WHERE NOT NULL
ORDER BY life expectancy DESC
LIMIT 10 OFFSET 9; 
#8
SELECT countries FROM world
WHERE NOT NULL
ORDER BY life expectancy DESC
LIMIT 10 OFFSET 9; 
#9
SELECT countries FROM world
WHERE NOT NULL
ORDER BY life expectancy DESC
LIMIT 10 OFFSET 9; 
#10
SELECT countries FROM world
WHERE NOT NULL
ORDER BY life expectancy DESC
LIMIT 10 OFFSET 9; 
#11
SELECT countries FROM world
WHERE NOT NULL
ORDER BY life expectancy DESC
LIMIT 10 OFFSET 9; 


