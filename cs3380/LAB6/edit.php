<html>
	<head>
		<!--  I USE BOOTSTRAP BECAUSE IT MAKES FORMATTING/LIFE EASIER -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css"><!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css"><!-- Optional theme -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script><!-- Latest compiled and minified JavaScript -->
	</head>
	<body>
		<div class="container">
<h3>Update record from the City table...</h3><form action='update.php' method='POST' ><input type='hidden' name='table' value='city'><div class='form-group'><label class='inputdefault'>ID</label><input class='form-control' type='text' name='ID' value='4186' readonly></div><div class='form-group'><label class='inputdefault'>Name</label><input class='form-control' type='text' name='Name' value='' readonly></div><div class='form-group'><label class='inputdefault'>CountryCode</label><input class='form-control' type='text' name='CountryCode' value='ANT' readonly></div><div class='form-group'><label class='inputdefault'>District</label><input class='form-control' type='text' name='District' value='Test District' required></div><div class='form-group'><label class='inputdefault'>Population</label><input class='form-control' type='number' name='Population' value='9876543' required></div><input class='btn btn-info' type='submit' name='submit' value='Save'></form>		</div>
	</body>
</html>