<!--Timotius Andrean Patrick Lagaunne /14173082-->

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
					<option value='1'>Query 1</option><option value='2'>Query 2</option><option value='3'>Query 3</option><option value='4'>Query 4</option><option value='5'>Query 5</option><option value='6'>Query 6</option><<option value='7'>Query 7</option><option value='8'>Query 8</option></select>
					<input type="submit" name="submit" value="Go"/>
				</form>
			</div>
			<?php
			$link=mysqli_connect("localhost","root","Palembang1","talyxd_lab5");
			#Create view 1
			mysqli_query($link,'CREATE VIEW weight AS SELECT person.pid,fname,lname FROM person INNER JOIN body_composition ON person.pid=body_composition.pid WHERE weight >140');
			
			#Create view 2
			mysqli_query($link,'CREATE VIEW BMI AS SELECT fname,lname,ROUND((703*weight/(height*height))) AS bmi FROM weight INNER JOIN body_composition ON weight.pid=body_composition.pid WHERE weight >150');

			if ($_POST['dropDown']!=NULL){
			switch($_POST['dropDown']){
				#Query 1
				case 1:
					$query ="SELECT * FROM weight";
					break;
				#Query 2
				case 2:
					$query ="SELECT  * FROM BMI";
					break;
				#Query 3
				case 3:
					$query ="SELECT university_name,city FROM university WHERE NOT EXISTS (SELECT * FROM person WHERE university.uid=person.uid)";
					break;
				#Query 4
				case 4:
					$query = "SELECT fname,lname FROM person WHERE person.uid IN (SELECT university.uid FROM university WHERE university.city='Columbia')";
					break;
				#Query 5
				case 5:
					$query = "SELECT activity.activity_name FROM activity WHERE activity.activity_name NOT IN (SELECT participated_in.activity_name FROM participated_in)" ;
					break;
				#Query 6
				case 6:
					$query ="SELECT pid FROM participated_in WHERE activity_name = 'running' UNION SELECT pid FROM participated_in WHERE activity_name = 'racquetball'";
					break;
				#Query 7
				case 7:
					$query = "SELECT DISTINCT new1.fname,new1.lname FROM person AS new1 INNER JOIN body_composition as new2 ON new1.pid=new2.pid  WHERE new2.age> 30 AND new2.age IN (SELECT age FROM person INNER JOIN body_composition ON person.pid=body_composition.pid  WHERE height >65)";
					break;
				#Query 8
				default:
					$query ="SELECT fname,lname,weight,height,age FROM person INNER JOIN body_composition ON  person.pid=body_composition.pid ORDER BY height DESC, weight ASC, lname ASC";
					
				}
					$result=mysqli_query($link,$query);
					$rows =mysqli_num_rows($result);
					
					#Showing resulted table
					echo "<h4>Number of rows: ". $rows ."</h4>";
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