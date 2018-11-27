<template>
  <tr v-if="is_contained(book, this.$store.state.selected_books)" bgcolor="#ADD8E6">
    <td>{{book.title}}</td>
    <td>{{book.author.name}} {{book.author.surename}}</td>
    <td>{{book.condition}}</td>
    <td>{{book.identity}}</td>
    <td>{{book.borrowed_by.name}} {{book.borrowed_by.surename}}</td>
    <td>something</td>
  </tr>
  <tr v-else>
    <td>{{book.title}}</td>
    <td>{{book.author.name}} {{book.author.surename}}</td>
    <td>{{book.condition}}</td>
    <td>{{book.identity}}</td>
    <td>{{book.borrowed_by.name}} {{book.borrowed_by.surename}}</td>
    <td>something</td>
  </tr>
</template>

<script>
export default {
  name: "BookRow",
  props: {
    book: { type: Object }
  },
  data() {
    return {
      books: {}
    };
  },
  created() {},
  computed: {
    selected_rows: function() {
      return this.$store.state.selected_books;
    },
    is_selected: function(obj) {
      if (obj === this.$store.state.selected) {
        return true;
      } else {
        return false;
      }
    }
  },
  methods: {
    is_contained: function(obj, list) {
      return list.some(listElement => {
        return listElement === obj;
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
tr {
  width: 100%;
}
</style>
