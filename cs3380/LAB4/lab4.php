<html>
	<head>
		<!--  I USE BOOTSTRAP BECAUSE IT MAKES FORMATTING/LIFE EASIER -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css"><!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css"><!-- Optional theme -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script><!-- Latest compiled and minified JavaScript -->
	</head>
	<body>
		<div class="container">
			<br>
			<br>
			<div class="row">
				<!-- 
					This form will submit a 'method' request
					the request is sent to 'action'
					In this case 'method' = POST and 'action' = this_php_script
				 -->
				<form action="html/lab4.php" method="POST" class="col-md-4 col-md-offset-5">
					<select name="dropDown">
					<option value='1'>Query 1</option><option value='2'>Query 2</option><option value='3'>Query 3</option><option value='4'>Query 4</option><option value='5'>Query 5</option><option value='6'>Query 6</option><option value='7'>Query 7</option><option value='8'>Query 8</option><option value='9'>Query 9</option><option value='10'>Query 10</option><option value='11'>Query 11</option><option value='12'>Query 12</option>						</select>
					<input type="submit" name="submit" value="Go"/>
				</form>
			</div>
			<?php
			$link=mysqli_connect("localhost","root","Palembang1","talyxd_lab4")
			switch($POST['dropDown']){
				case 1:
					$query ="SELECT Name, District, Population FROM City WHERE Name = 'Springfield' ORDER BY population DESC;"
					break;
				case 2:
					$query ="SELECT Name, District,Population FROM City WHERE CountryCode='BRA' ORDER BY Name ASC;"
					break;
				case 3:
					$query ="SELECT Name, Continent, SurfaceArea FROM Country ORDER BY SurfaceArea ASC LIMIT 20;"
					break;
				case 4:
					$query = "SELECT Name, Continent, GovernmentForm, GNP FROM Country WHERE GNP>200000 ORDER BY Name ASC;"
					break;
				case 5:
					$query = "SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy IS NOT NULL ORDER BY LifeExpectancy DESC LIMIT 10 OFFSET 9" 
					break;
				case 6:
					$query ="SELECT Name FROM City WHERE (Name LIKE 'B%' and Name LIKE '%s') ORDER BY Population DESC;"
					break;
				case 7:
					$query = "SELECT Name,CountryCode,Population FROM City WHERE Population>6000000 ORDER BY Population DESC;"
					break;
				case 8:
					$query = "SELECT Country.Name, Country.IndepYear, Country.Region FROM CountryLanguage INNER JOIN Country ON Country.Code=CountryLanguage.CountryCode WHERE (CountryLanguage.Language ='English' and CountryLanguage.IsOfficial='T') ORDER BY Country.Region ASC;"
					break;
				case 9:
					$query = "SELECT Country.Name,  City.Population AS 'Capital Population', Country.Population, (City.Population / Country.Population) AS 'Percentage of population that live in capital' FROM City INNER JOIN Country ON Country.Capital=City.Id  ORDER BY 4 DESC;" 
					break;
				case 10:
					$query = "SELECT CountryLanguage.Language AS 'language', Country.Name AS'name',CountryLanguage.Percentage  AS 'Percentage', CountryLanguage.Percentage*Country.Population  AS 'Total # of Speaker' FROM Country LEFT JOIN CountryLanguage ON Country.Code=CountryLanguage.CountryCode WHERE CountryLanguage.IsOfficial='T' ORDER BY 4 DESC ,1 ASC;" 
					break;
				default:
					$query = "SELECT Name, Region, GNP, GNPOld, (GNP-GNPOld)/GNPOld AS 'Real change in GNP' FROM Country WHERE (GNP IS NOT NULL and GNPOld IS NOT NULL) ORDER BY 5 DESC;" 
				}
				$result=mysqli_query($link,$query);
				$rows =mysql_num_rows($result);
				$fields=mysqli_num_fields($result);
				echo "<table>";
				echo "<tr>";
				for($i=0;$i< $fields;$i++){
					$name=mysql_field_name($result,$i);
					echo "<td>". $name ."</td>";
				}
				echo "</tr>";
				for($i=0;$i<$rows;$i++)
				{
					echo"<tr>"; 
					for ($j=0;$j<$fields;$j++){
						$name=mysql_field_name($result,$i);
						echo "<td>". $result[$name] ."</td>";
					}
					echo"</tr>";
				}
							
				echo "</table>";
			mysqli_close($link);
			?>
		</div>
	</body>
</html>