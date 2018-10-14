<%-- 
    Document   : login
    Created on : Oct 14, 2018, 6:53:38 PM
    Author     : Babu
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="author" content="">

  <title>Super Canvasser Login</title>

  <!-- Bootstrap core CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <!-- Custom styles for this template -->
    <link href="loginstyle.css" rel="stylesheet">
     <script>
    function UserAction() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
             alert(this.responseText);
         }
    };
    xhttp.open("POST", "http://104.196.143.177:8080/api/login", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    var data = JSON.stringify({"email": $("#inputUser").val(), "password": $("#inputPassword").val()});
    xhttp.send(data);
    alert(xhttp.responseText);
}
</script>
</head>


 <body class="text-center">
    
      <div class ="jumbotron">
      

    <form class="form-signin">
      <h1>Super Canvasser</h1>

      <label for="inputUser" class="sr-only">Username</label>
      <input type="text" id="inputUser" class="form-control" placeholder="Username" required>
      <br>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="Password" id="inputPassword" class="form-control" placeholder="Password" required>
      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> Remember me
        </label>
      </div>
      <button class="btn btn-block btn-dark btn-outline-primary" type="submit" onclick = "UserAction();">Sign in</button>
      <br>
    </form>

  </div>
    <!-- 
      ================================================== -->
    
</body>
</html>
