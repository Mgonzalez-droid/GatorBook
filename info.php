

<?php
$text = $_POST["body"];
$host = "localhost";
$dbname = "gatorbookdb";
$username = "root";
$password = "password";
function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

$conn = mysqli_connect($host, $username, $password, $dbname);
if (mysqli_connect_errno()){
  die("Connection Error: " . mysqli_connect_error());
}
$sample_username = "johndoe";
$sql_1 = "SELECT * FROM user WHERE username = '$sample_username'";
$result = mysqli_query($conn, $sql_1);
if(mysqli_num_rows($result) > 0){

$sql = "INSERT INTO public_post (body)
        VALUES (?)";

$stmt = mysqli_stmt_init($conn);

if ( ! mysqli_stmt_prepare($stmt, $sql)) {

        die(mysqli_error($conn));
    }


mysqli_stmt_bind_param($stmt, "s",
                       $text);

mysqli_stmt_execute($stmt);

echo "Post saved.";
} else{
  echo "your username was not found, you are not a user of gatorbook";
}

 ?>
