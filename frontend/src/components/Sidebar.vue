<template>
  <div class="sidebar">
      <div v-for="item in actions" :key="item.name">
        {{ item.name }}<br>
      </div>
      <div>
      <form method="get" action="/page2">
        <button type="Submit">Add book</button>
        <button type="Submit">Edit book</button>
        <button type="Submit">Delete book</button>
      </form>
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
      ],
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
  margin: 0 40px;
  color: #42b983;
}
button {
  display: fixed;
  margin: 16px 40px;
  padding: 10px 70px 10px 70px;
}
</style>
