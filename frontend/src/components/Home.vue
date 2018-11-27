<template>
  <div class="hello">
    <h1>Alexandria</h1>
    <body>
      <div class="sidenav">
        //<a href="#"> Add new book</a>
        <a href="#"> Edit book </a>
        <a href="#"> Delete book </a>
        <a href="#"> Release book </a>
      </div>
    </body>
  </div>


</template>

<script>
export default {
  name: "Home",
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

body{
  font-family:"Lato", sans-serif;
}

.sidenav {
  height: 80%;
  width: 13%;
  position: fixed;
  z-index: 1;
  top: 10%;
  left:10px;
  background-color: #fff;
  overflow-x: hidden;
  padding-top: 110px;
}

.sidenav a {
  padding: 0px 6px 6px 32px;
  text-decoration:  none;
  font-size: 16px;
  color: #818181;
  display: block;
}

.sidenav a:hover {
  color: #000;
}

.main {
  margin-left: 200px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {front-size: 18px;}
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 16px;
}
li {
  display: inline-block;
  margin: 0px 10px;
}
a {
  color: #42b983;
  padding-top: 16px;
}
</style>
