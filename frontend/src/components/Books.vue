<template>
  <div class="books">
    Books total: {{stats.total}}<br>
    Borrowed books: {{stats.borrowed}}<br>
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Author</th>
          <th>Condition</th>
          <th>Identity</th>
          <th>Student</th>
          <th>Status</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
          <BookRow
            v-for="book in books_filtered"
            :key="book.id"
            :book="book"
            :selected_rows="books_filtered"
            @click.native="toggle_row(book)"
          />
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import BookRow from "./BookRow.vue";

axios.defaults.baseURL = "http://localhost:4000/api";

export default {
  name: "Books",
  components: {BookRow},
  props: {},
  data() {
    return {
      errors: [],
      search_expr: "",
    };
  },
  created() {
    // test
    axios
      .get("/books")
      .then(response => {
        this.$store.commit("store_books", response.data);
      })
      .catch(e => {
        this.errors.push(e);
      });
  },
  computed: {
    stats: function() {
      var borrowed = [];
      for (var i = 0; i < this.$store.state.books.length; i++) {
        var si = this.$store.state.books[i];

        if (si.borrowed_by != null) {
          borrowed.push(si);
        }
      }
      return {
        total: this.$store.state.books.length,
        borrowed: borrowed.length
      };
    },
    selectedCategory() {
      return this.$store.state.selected_category.toLowerCase();
    },
    books_filtered: function() {
      let books = [];
      if (this.$store.state.search_expr.length > 0) {
        var books_filtered = [];
        var expr = this.$store.state.search_expr.toLowerCase();
        var category = this.$store.state.selected_category.toLowerCase();

        for (var i = 0; i < this.$store.state.books.length; i++) {
          var si = this.$store.state.books[i];
          console.log(si, expr, category)
          if (category && si[category].includes(expr)){
            books_filtered.push(si);
          }
        }
        books = books_filtered;
      } else {
        books = this.$store.state.books;
      }
      books = this.sortByKey(books, category)
      return books
    }
  },
  methods: {
    is_contained(obj, list) {
      return list.some((listElement) => {
        return listElement === obj;
      });
    },
    remove_by_attr(arr, attr, value) {
      return arr.filter((element) => {
        return element[attr] !== value;
      })
    },
    sortByKey(array, key) {
      debugger;
      if (typeof array === 'Array') {
        let sorteArrary = array
        sorteArrary.sort(function(a, b) {
          var x = a[key];
          var y = b[key];
          return ((x < y) ? -1 : ((x > y) ? 1 : 0));
        });
        return sorteArrary;
      }
      return array;

    },
    toggle_row(row) {
      this.$store.commit("select_row", row);
      if (this.is_contained(row, this.$store.state.selected_books)) {
        this.$store.commit(
          "set_selected_books",
          this.remove_by_attr(
            this.$store.state.selected_books, "id", row.id)
        );
      } else {
        this.$store.commit("add_selected_book", row);
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
tbody {
  // display: block;
}

thead,
tbody tr {
  // display: table;
  width: 100%;
  align: center;
}

thead {
  width: 100%;
}

table {
  width: 100%;
  margin:   30px 10px 0 -20px;
}

</style>
