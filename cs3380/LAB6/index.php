
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
				<form action="<?=$_SERVER['PHP_SELF']?>" method="POST" class="col-md-4 col-md-offset-4">
					<div class="row">
							<input class='col-md-10' type="text" name="userinput">
							<input class=" btn btn-info col-md-2" type="submit" name="submit" value="Go"/>
					</div>
					<div class="row">
						<input checked="check" type="radio" name="radios" value=0>City
						<input type="radio" name="radios" value=1>Country
						<input type="radio" name="radios" value=2>Language
					</div>
				</form>
				<!--<a href="insert.php" class="btn btn-primary">Insert into city</a>-->
			</div>
			<?php

			$link = mysqli_connect('localhost','root','Palembang1','talyxd_lab6');
			$name = "C%";

			$sql = "SELECT * FROM City WHERE LOWER(name) LIKE LOWER(?) ORDER BY name ASC";
			if ($stmt = mysqli_prepare($link, $sql)) {
 				mysqli_stmt_bind_param($stmt, "s", $prefix) or die("bind param");
 				mysqli_stmt_execute($stmt) or die("execute");
 				$result = mysqli_stmt_get_result($stmt);
 				echo "Number of rows: ".mysqli_num_rows($result);
			}


			?>
		</div>
	</body>
</html>
