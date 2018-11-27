<template>
  <div class="sidebar">
      <div v-for="item in actions" :key="item.name">
        {{ item.name }}<br>
      </div>
      <br>
      <div v-for="key in this.selected_keys" :key="key">
        {{key}}: <br><input v-model="message" :placeholder="selected[key]"><br><br>
      </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  props: {},
  computed: {
    selected: function() {
      return this.$store.state.selected
    },
    selected_keys: function() {
      if (this.selected !== {}) {
        this.values = this.selected;
        return Object.keys(this.selected);
      }
    },
    selected_values: function() {
      if (this.selected !== {}) {
        return Object.values(this.selected);
      }
    }
  },
  data() {
    return {
      actions: [
        { name: "Add book", action: "" },
        { name: "Edit book", action: "" },
        { name: "Delete book", action: "" },
        { name: "Release book", action: "" },
      ],
    };
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
  padding: 6px 6px 6px 24px;
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
  padding: 0 10px;
}

li {
  margin: 0 10px;
}


a {
  margin: 0px 40px;
  color: #42b983;
}

</style>
