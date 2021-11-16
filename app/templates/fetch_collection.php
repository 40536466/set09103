<?php

// Fetch user's collection contents from DB, if logged in
if (isset($_SESSION['currentUser'])) {
  $query = mysqli_query($connection, "SELECT collection FROM users WHERE username='$_SESSION[currentUser]'");
  $result = mysqli_fetch_array($query);

  // If collection not empty, unserialize contents and add to collectionContents array, which stores comic IDs
  if (!empty($result['collection'])) {
    $_SESSION['collectionContents'] = unserialize($result['collection']);
  }
}

?>