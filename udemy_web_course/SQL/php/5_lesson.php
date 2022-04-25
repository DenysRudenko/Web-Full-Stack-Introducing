<!-- CRUD ~ CREATE,~READ,~UPDATE,~DELETE -->

<?php

    include "example.php";

    $query = 'SELECT * FROM users;';

    $query_result = mysqli_query($connection, $query);
    if (!$query_result) {
        die("Querry failed" . mysqli_error());
    }

?>