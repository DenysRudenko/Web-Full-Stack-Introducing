<?php

if (isset($_POST['submit'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $username = $_POST['username'];

    // echo $email;
    // echo $password;

    // ------> Making connection for my SQL database.
    $connection = mysqli_connect('localhost', 'root', '', 'my_database');

    // ------> Need to be sure if connection exist!
    if ($connection) {
        echo "Database is connected!";
        // ------> Continue the cycle.    
    } else {
        // -------> Using die function, same as 'Exit' function!    
        die('Connection failed!');
    }

    $query = "INSERT INTO users (user_name, email, password) VALUES
        ('$username', '$email', '$password');";

    $query_result = mysqli_query($connection, $query);

    if (!$query_result) {
        die("Query failed! " . mysqli_error());
    }
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

    <!-- ......A simple form using Bootstrap...... -->

    <form action="login.php" method="post">
        <div class="mb-3">
            <label for="exampleInputUsername1" class="form-label">Username</label>
            <input type="username" placeholder="Enter your name" class="form-control" name="username" id="exampleInputUsername1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" placeholder="Enter your email" class="form-control" name="email" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" placeholder="Enter your password" class="form-control" name="password" id="exampleInputPassword1">
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
        <button type="submit" name="submit" class="btn btn-primary">Submit</button>
    </form>


</body>

</html>