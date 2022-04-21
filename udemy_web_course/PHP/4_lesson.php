<?php

$userName = "Joe";
$userAge = 15;
$isUserLogin = false;

if($isUserLogin || $userAge > 18) {
    echo "Hello ".$userName;
} else {
    echo "You have to login and you have to be older than 18!";
}

?>