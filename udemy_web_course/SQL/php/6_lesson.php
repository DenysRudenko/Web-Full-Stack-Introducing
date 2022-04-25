<?php

    session_start();

    // $_SESSION['user_name'] = 'daniel2001';

    //echo $_SESSION['user_name'];

    // if ($_SESSION['email']) {
    //     echo "You are logged in";
    // } else {
    //     header("Location : login_task.php");
    // }

    setcookie('user_id', '1111', time() + 60 * 60 * 24 * 7);
    echo $_COOKIE['user_id'];

    ?>