<?php
    
    if(isset($_GET['number'])) {
        $value = $_GET["number"];

        if (floor($value) == $value && is_numeric($value)) {
            if ($value % 2) {
                echo $value . ' is odd';
            } else {
                echo $value . ' is even';
            }
        } else {
            echo "The number have to be whole!";
        }
    
    }


?>

<p>Input whole number</p>

<form action="">
    <input type="text" name="userName">
    <input type="submit" name="">
</form>