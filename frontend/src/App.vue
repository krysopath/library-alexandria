<template>
  <div id="app">
    <div id="header">
      <div id= "search_box">
      <input @input="set_search_expr" placeholder="search">
      </div>
      <div id="category_box">
      <select @input="set_search_category">
        <option value="title">Title</option>
        <option value="author">Author</option>
        <option value="condition">Condition</option>
        <option value="identity">Identity</option>
        <option value="borrower">Borrower</option>
      </select>
    </div>

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
    },
    set_search_category: function($event) {
      this.$store.commit("select_a_category", $event.target.value);
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
  color: #000000;
  margin-top: 2.5%;
  position: relative;
}

#header {
  position: left;
  text-align: left;
  background: #3399ff;
  padding: 10px;
  margin-left: 0px;
  top: 0;
  left: 11%;
  width: 100%;
  border: none;
  display: flex;
}

#search_box {
  margin-right: 24px;
}

#navbar {
  position: fixed;
  text-align: right;
  background: #3399ff;
  top: 0;
  left: 80%;
  margin-top: 39px;
  margin-left: 10px;
}

.navitem {
  margin-left: 20px;
  margin-right: 20px;
  width: 10%;
  height: 10%;
}

#left_side {
  margin-top: 3%;
  padding-top: 7%;
  margin-left: -0.25%;
  position: fixed;
  top: 3.5%;
  width: 15%;
  height: 100%;
  background-repeat: repeat-y;
  font-size: 16px;
  border: 1px solid #3399ff;
  border-top: 5.5%;
}

#content {
  height: auto;
  margin-top: 0%;
  margin-left: 15.5%;
  margin-right: -2%;
  overflow: auto;
  border: none;
  padding-top: 3%;
  padding-bottom: 3%;
  padding-left: 3%;
  padding-right:3%;
}
#select {
  margin: 10px;
}
</style>
