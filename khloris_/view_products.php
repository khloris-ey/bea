<?php
session_start();
include('../php/config.php');




    $servername="localhost";
    $username="beicoleene";
    $password="030419061313bei";
    $dbname="khloris_ecommerce";

    $conn= new mysqli($servername, $username, $password,$dbname);

    if ($conn -> connect_error){
      die("Connection Failed".$conn->connect_error);
    }


    if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $delete_sql = "DELETE FROM products WHERE id='$id'";

    $data = mysqli_query($con, $delete_sql);

    if ($data) {
        header("location:view_products.php");
    }
    }

    $sql = "SELECT * FROM products";
    $result = mysqli_query($conn, $sql);

    ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Product</title>
    <link rel="stylesheet" href="view_products.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" />

</head>

<body>
    <header>
        <input type="checkbox" name="" id="toggler" />
        <label for="toggler" class="fas fa-bars"></label>
        <a href="../admin/admin_dashboard.php" class="logo">Khloris<span>.</span></a>
        <nav class="navbar">
            <a href="../admin/admin_dashboard.php">Home</a>
            <a href="../admin/add_products.php">Add Products</a>
            <a href="../admin/view_products.php">View Products</a>
            <a href="../admin/orders.php">Orders</a>
            <a href="#Orders">Users</a>
        </nav>
        <div class="icons">
            <a href="admin_logout.php" class="fa-solid fa-right-from-bracket" onclick="return confirmLogout()"></a>
        </div>
    </header>

    <div class="info">

        <h1>All Products</h1>

        <table>
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Image</th>
                <th>Category</th>
                <th>Type</th>
                <th>Update</th>
                <th>Remove</th>


            </tr>

            <?php
            while ($row = mysqli_fetch_assoc($result)) {
            ?>
                <tr>
                    <td><?php echo $row['name'] ?></td>
                    <td><?php echo $row['description'] ?></td>
                    <td><?php echo $row['price'] ?></td>
                    <td><?php echo $row['quantity'] ?></td>
                    <td>
                        <img src="<?php echo $row['image_url'] ?>">
                    </td>
                    <td><?php echo $row['category_id'] ?></td>
                    <td><?php echo $row['type_id'] ?></td>
                    <td>
                        <a href="../admin/update_product.php?id=<?php echo $row['id'] ?>" class="update-btn">Update</a>
                    </td>

                    <td>
                        <a href="view_products.php?id=<?php echo $row['id'] ?>" class="delete-btn"
                            onclick="return confirm('Are you sure you want to remove this product?')">Remove</a>
                    </td>

                </tr>

            <?php
            }
            ?>
        </table>
    </div>

    <script>
        function confirmLogout() {
            return confirm("Are you sure you want to log out?");
        }
    </script>
</body>

</html>