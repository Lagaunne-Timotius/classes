<!DOCTYPE html>
<html>
<head>
    <title>Lab 4 Sample</title>
</head>
<body>    
  
<?php
  $link = mysqli_connect("HOSTNAME", "DBUSER", "PASSWORD", "DBNAME");
  if (mysqli_connect_errno()) { // if no error occurred when connecting
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
	} else { // we are connected
		echo "Connected<br>";
	}
                
 // Function to execute & display the number of results from an SQL query
  function runQueryPrintResults($sql) {
    global $link;
    
    if ($result = mysqli_query($link, $sql)) { // if the query is valid
      printf("Query returned %d rows.\n", mysqli_num_rows($result)); //print number of rows
  		mysqli_free_result($result); // free result set 
  	} else {
  		printf("Error: %s\n", mysqli_error($link));		
  	} 
  }
  
  //mysql query
  $query = "SELECT * FROM City;";
  runQueryPrintResults($query);
?>

</body>
</html>
