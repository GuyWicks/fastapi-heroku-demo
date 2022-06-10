# Login Demo

Example of a login form to return an API access token.
<style>
    .login_form INPUT[type="text"] {background-color: LightGoldenRodYellow}
    .login_form INPUT[type="submit"] {padding: 1em}
    .login_form INPUT[type="submit"]:hover {background-color: lightgrey}
</style>

<form class="login_form" action="https://fastapi-heroku-demo.herokuapp.com/token/" method="post">
  <fieldset>
    <legend>Login:</legend>
        <label for="username">Username: </label> <input type="text" id="username" name="username" value="johndoe"><br>
        <label for="password">Password: </label> <input type="text" id="password" name="password" value="secret"> &lt; Obviously this should be type="password"<br>
        <input type="submit" value="Login">
    </fieldset>
</form>

Command line example
```
curl -X 'POST' \
  'https://fastapi-heroku-demo.herokuapp.com/token/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret='
```
