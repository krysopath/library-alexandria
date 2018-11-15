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
        // TODO: remove this CWE-546
        // eslint-disable-next-line
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
        { name: "Create", action: "" },
        { name: "Read", action: "" },
        { name: "Update", action: "" },
        { name: "Delete", action: "" }
      ],
      errors: [],
      values: {},
      search_expr: "",
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
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
