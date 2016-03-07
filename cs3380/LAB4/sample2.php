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
					<?php
						for($i = 0; $i< 5; $i++) {
  						if(isset($_POST['dropDown']) && $_POST['dropDown']==$i) {
    						echo "<option selected='selected' value='".$i."'>Option ".$i."</option>";
  						} else {
      					echo "<option value='".$i."'>Option ".$i."</option>";	
  						}
						}
					?>
					</select>
					<input type="submit" name="submit" value="Go"/>
				</form>
			</div>
			<?php
				if(isset($_POST['submit'])) { // Was the form submitted?
					//The value submitted from the drop down was...
					echo "You selected ".$_POST['dropDown']."...........";
					echo "Rather than just printing ".$_POST['dropDown']." here, we could have used the ".$_POST['dropDown']." as MySQL query parameter.";
					echo "For example: SELECT * FROM table WHERE id = ".$_POST['dropDown'].";";
				}
			?>

			<table class="table table-hover">
				<thead>
					<tr>
						<th>Column1</th> <!-- Print 1st column header -->
						<th>Column2</th> <!-- Print 2nd column header -->
					</tr>
				</thead>
				<tbody>
				<?php
					$arr = array("col1","col2"); //sample data (attributes)
					for($i = 0; $i< 5; $i++) { //iterate
				?>
					<tr>
						<td><?=$arr[0]?></td> <!-- Print 1st column -->
						<td><?=$arr[1]?></td> <!-- Print 2nd column -->
					</tr>
				<?php
					} //end for loop
				?>
				</tbody>
			</table>
		</div>
	</body>
</html>
