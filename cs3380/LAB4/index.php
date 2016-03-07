<!-- Timotius Andrean Patrick Lagaunne
	 14173082 
	 talyxd
	-->



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

				<form action="<?=$_SERVER['PHP_SELF']?>" method="POST" class="col-md-4 col-md-offset-5">
					<select name="dropDown">
					<option value='1'>Query 1</option><option value='2'>Query 2</option><option value='3'>Query 3</option><option value='4'>Query 4</option><option value='5'>Query 5</option><option value='6'>Query 6</option><option value='7'>Query 7</option><option value='8'>Query 8</option><option value='9'>Query 9</option><option value='10'>Query 10</option><option value='11'>Query 11</option>						</select>
					<input type="submit" name="submit" value="Go"/>
				</form>
			</div>
			
			<?php
			#Connect to sql database
			$link=mysqli_connect("localhost","root","Palembang1","talyxd_lab4");
			

			if ($_POST['dropDown']!=NULL){
			switch($_POST['dropDown']){
				#Query 1
				case 1:
					$query ="SELECT Name, District, Population FROM City WHERE Name = 'Springfield' ORDER BY Population DESC";
					break;
				#Query 2
				case 2:
					$query ="SELECT Name, District,Population FROM City WHERE CountryCode='BRA' ORDER BY Name ASC";
					break;
				#Query 3
				case 3:
					$query ="SELECT Name, Continent, SurfaceArea FROM Country ORDER BY SurfaceArea ASC LIMIT 20";
					break;
				#Query 4
				case 4:
					$query = "SELECT Name, Continent, GovernmentForm, GNP FROM Country WHERE GNP>200000 ORDER BY Name ASC";
					break;
				#Query 5
				case 5:
					$query = "SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy IS NOT NULL ORDER BY LifeExpectancy DESC LIMIT 10 OFFSET 9" ;
					break;
				#Query 6
				case 6:
					$query ="SELECT Name FROM City WHERE (Name LIKE 'B%' and Name LIKE '%s') ORDER BY Population DESC";
					break;
				#Query 7
				case 7:
					$query = "SELECT Name,CountryCode,Population FROM City WHERE Population>6000000 ORDER BY Population DESC";
					break;
				#Query 8
				case 8:
					$query = "SELECT Country.Name, Country.IndepYear, Country.Region FROM CountryLanguage INNER JOIN Country ON Country.Code=CountryLanguage.CountryCode WHERE (CountryLanguage.Language ='English' and CountryLanguage.IsOfficial='T') ORDER BY Country.Region ASC";
					break;
				#Query 9
				case 9:
					$query = "SELECT Country.Name,  City.Population AS 'Capital Population', Country.Population, (City.Population / Country.Population) AS 'Percentage of population that live in capital' FROM City INNER JOIN Country ON Country.Capital=City.Id  ORDER BY 4 DESC" ;
					break;
				#Query 10
				case 10:
					$query = "SELECT CountryLanguage.Language AS 'language', Country.Name AS'name',CountryLanguage.Percentage  AS 'Percentage', CountryLanguage.Percentage*Country.Population  AS 'Total # of Speaker' FROM Country LEFT JOIN CountryLanguage ON Country.Code=CountryLanguage.CountryCode WHERE CountryLanguage.IsOfficial='T' ORDER BY 4 DESC ,1 ASC" ;
					break;
				#Query 11
				default:
					$query = "SELECT Name, Region, GNP, GNPOld, (GNP-GNPOld)/GNPOld AS 'Real change in GNP' FROM Country WHERE (GNP IS NOT NULL and GNPOld IS NOT NULL) ORDER BY 5 DESC" ;
				}
					#show result
					$result=mysqli_query($link,$query);
					$rows =mysqli_num_rows($result);
					
					$fields=mysqli_num_fields($result);
					echo "<h4>Number of rows:". $rows. "</h4>";
					echo "<table class='table table-hover'>";
					echo "<thead>";
					echo "<tr>";
		
					while ($fieldinfo=mysqli_fetch_field($result)) {
						echo "<th>".$fieldinfo->name."</th>";
					}
					echo"</tr>";
					echo "</thead>";
					
					while($row = mysqli_fetch_row($result)) {
    				echo "<tr>";
    				foreach($row as $_column) {
        				echo "<td>{$_column}</td>";
    				}
    				echo "</tr>";
					}
							
					echo "</table>";
				}
				
				#Closing the connection
				mysqli_close($link);

				?>
			
		</div>
	</body>
</html>