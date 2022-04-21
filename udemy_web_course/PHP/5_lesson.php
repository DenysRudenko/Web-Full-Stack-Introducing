<?php

$colors = array("red", "orange", "yellow", "green", "blue", "indigo", "violet");

foreach ($colors as $key => $value) {
    $colors[$key] = $value." color";
    echo $value." ";
}

for($i = 0; $i < sizeof($colors); $i++) {
    echo $colors[$i]." ";
}
 
 ?>