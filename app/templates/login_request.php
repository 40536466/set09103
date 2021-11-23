<?php


// Automatically login if $_SESSION['username'] is already set - i.e. if the user has just completed the registration form
if (isset($_SESSION['username'])) {

  // Set current user
  $_SESSION['currentUser'] = $_SESSION['username'];
  
  header("Location: index.php");
  exit();
}





// If $_SESSION['username'] not already set, standard log in process below:
// Apostrophes replaced in strings to avoid SQL errors
else {
  
  // User input variables
  $_SESSION['username'] = str_replace("'", "&#39;", $_POST['username']);
  $_SESSION['password'] = str_replace("'", "&#39;", $_POST['password']);

  // Check username and password exist in DB
  $query = mysqli_query($connection, "SELECT * FROM users WHERE username='$_SESSION[username]' AND password='$_SESSION[password]'");

  // If details not found, return to login form with error
  if (mysqli_num_rows($query) != 1) {
    unset($_SESSION['username']);
    unset($_SESSION['password']);
    header("Location: login_register.php?section=login&error=user_details_not_found");
  }





  // If details found, set session variables
  else {

    // Set current user
    $_SESSION['currentUser'] = $_SESSION['username'];

    header("Location: index.php");
  }
}

?>