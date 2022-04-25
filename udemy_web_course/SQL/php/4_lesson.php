<?php

    // ------> Making connection for my SQL database.
    $connection = mysqli_connect('localhost', 'root', '', 'my_database');

    if ($connection) {
        echo "Connected to database!";
    } else {
        die('Connection failded');
    }

    $query = 'SELECT * FROM users;';

    $query_result = mysqli_query($connection, $query);
    if (!$query_result) {
        die("Query failed" . mysqli_error());
    }

?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Document</title>
</head>

<body>

    <div class="container">
        <div class="col-md-6">

            <?php

            // while ($row = mysqli_fetch_row($query_result)) {
            //   print_r($row);
            // }
            while ($row = mysqli_fetch_assoc($query_result)) {
            ?>

                <pre>
                        <?php
                        print_r($row);
                        ?>
                    </pre>
            <?php
            }

            ?>
        </div>
    </div>



</body>

</html>