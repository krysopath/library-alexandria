<template>
  <div id="app">
    
    <div id="header">
      <input @input="set_search_expr" placeholder="search me">
      <div id="navbar">
        <a href="/#/books">
          <img class="navitem" src="./assets/library.png">
        </a>
        <a href="/#/students">
          <img class="navitem" src="./assets/students.png">
        </a>
        <img class="navitem" src="./assets/email.png">
      </div>
    </div>

    <div id="left_side">
      <Sidebar/>
    </div>

    <div id="content">
      <router-view/>
    </div>

  </div>
</template>

<script>
import Home from "./components/Home.vue";
import Students from "./components/Students.vue";
import Books from "./components/Books.vue";
import Sidebar from "./components/Sidebar.vue";

export default {
  name: "app",
  components: {
    Home,
    Students,
    Books,
    Sidebar
  },
  data() {
    return {
      search_expr: ""
    };
  },
  methods: {
    set_search_expr: function($event) {
      this.$store.commit("set_search_expr", $event.target.value);
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 2.5%;
  position: relative;
}

#header {
  position: fixed;
  text-align: left;
  background: #ffffff;
  padding: 10px;
  top: 0;
  left: 11%;
  width: 100%;
  border: 1px dotted blue;
}

#navbar {
  position: fixed;
  text-align: right;
  background: #ffffff;
  top: 0;
  left: 80%;
  border: 1px dotted yellow;
}

.navitem {
  margin-left: 20px;
  margin-right: 20px;
  width: 20%;
  height: 20%;
}

#left_side {
  margin-top: 3.5%;
  position: fixed;
  top: 3.5%;
  width: 10%;
  height: 100%;
  background-repeat: repeat-y;
  font-size: 16px;
  border: 1px dotted red;
}
#content {
  height: auto;
  margin-top: 5.5%;
  margin-left: 11%;
  margin-right: 2%;
  overflow: auto;
  border: 1px dotted black;
}
</style>
