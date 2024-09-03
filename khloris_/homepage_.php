<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Khloris</title>
    <link rel="stylesheet" href="homepage_.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"
    />
  </head>
  <body>

    

    <?php


        $servername = "localhost";
        $username = "beicoleene";
        $password = "030419061313bei"; 
        $dbname = "khloris_flowershop";

        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn ->connect_error){
            die("Connection Failed" .$conn->connect_error);
        }
        echo "Connected!"
        ?>





    <header>
      <input type="checkbox" name="" id="toggler" />
      <label for="toggler" class="fas fa-bars"></label>
      <a href="#" class="logo">Khloris<span>.</span></a>
      <nav class="navbar">
        <a href="#home">Home</a>
        <a href="#Customization">Customization</a>
        <a href="flowerpage.html">Flowers</a>
        <a href="#Occassions">Occassions</a>
      </nav>
      <div class="icons">
        <a href="" class="fas fa-shopping-cart"></a>
        <a href="logout.php" class="fa-solid fa-right-from-bracket" onclick="return confirmLogout()"></a>
      </div>
    </header>
    <section class="home" id="home">
      <div class="content">
        <img
          class="logoimg"
          src="https://res.cloudinary.com/dogrgo15f/image/upload/v1724128500/images/kk90fhhfsltwy7eqgtfg.png"
          alt="logochloris"
        />
        <h3><span>Khloris</span> Flower Shop</h3>
        <p>
          Creating memories with every each petals. Try our <br />long lasting
          flowers for every occasion <br />anywhere and anytime.
        </p>
        <a href="#" class="btnshopnow">Shop now</a>
      </div>
    </section>

    <section class="prdctsrecommend" id="prdctsrecommend">
      <h1 class="recommend">recommend <span>for you</span></h1>
      <div class="box-container">

      <?php

        $sql= "SELECT name, price, img_url FROM product";

        $result= $conn -> query($sql);

        if ($result -> num_rows > 0){

            while ($row = $result -> fetch_assoc()) {
              



        echo '<div class="flwrbox">';
        echo'   <div class="flwrimg">';
        echo '      <img src="'. $row["img_url"].'" alt="'.$row["name"].'"/>';
        echo '      <div class="icons">';
        echo'           <a href="#" class="cart-btn">add to cart</a>';
        echo'       </div>';
        echo '  </div>';
        echo'   <div class="imgcontent">';
        echo'      <h3>'. $row["name"] .'</h3>';
        echo'        <div class="price">P'. $row["price"] . '</div>';
        echo'    </div>';
        echo' </div>';

       
            }
        }else {
            echo "No products found";

        }


        $conn ->close();

        ?>
        
      </div>
      <div class="button-container">
        <a href="#flowers">More flowers</a>
        <a href="#Occasions">Occasions</a>
      </div>
    </section>

    <footer class="footer">
      <div class="ftrcontainer">
        <div class="ftrrow">
          <div class="footer-col">
            <h4 class="logofooter">Khloris<span>.</span></h4>
            <ul class="ftrul">
              <p>Follow us in Social Media!</p>
              <div class="social-links">
                <a href="#" class="fa-brands fa-square-facebook"></a>
                <a href="#" class="fa-brands fa-square-instagram"></a>
              </div>
            </ul>
          </div>

          <div class="footer-col">
            <h4>Information</h4>
            <ul class="ftrul">
              <p>Flower Shop in Pandi,Bulacan <br />Delivery only in Pandi</p>
              <li><a href="#">Privacy policy</a></li>
              <li><a href="#">Payment Instruction</a</li>
              <li><a href="#">Terms and conditions</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <h4>Contact us</h4>
            <ul class="ftrul">
              <p><span>Address:</span>Pandi, Bulacan</p>
              <p><span>Mobile:</span>(+63) 0903-2301484/09299750331</p>
              <p><span>Telephone:</span>(632) 8881-4173</p>
              <p><span>Email:</span>admin@khlorisflowershop.com</p>
            </ul>
          </div>

          <div class="footer-col">
            <h4>Contact Services</h4>
            <ul class="ftrul">
              <li><a href="#">Contact us</a></li>
              <li><a href="#">My account</a></li>
              <li><a href="#">Order History</a></li>
            </ul>
          </div>
        </div>
      </div>
    </footer>

    <script>
        function confirmLogout() {
          return confirm("Are you sure you want to log out?");
          }
    </script>

  </body>
</html>
