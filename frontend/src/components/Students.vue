<template>
  <div class="students">
    Students total: {{stats.total}}<br>
    Students with books: {{stats.borrowed}}<br>
    <table>
      <thead>
        <tr>
          <th>Lastname</th>
          <th>Firstname</th>
          <th>PersonalId</th>
          <th>Email</th>
          <th>Books</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
          <StudentRow
            v-for="student in students_filtered"
            :key="student.id"
            :student="student"
            :selected_rows="students_filtered"
            @click.native="toggle_row(student)"
          />
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import StudentRow from "./StudentRow.vue";

axios.defaults.baseURL = "http://localhost:4000/api";

export default {
  name: "Students",
  components: {StudentRow},
  props: {},
  data() {
    return {
      errors: [],
      search_expr: "",
    };
  },
  created() {
    axios
      .get("/students")
      .then(response => {
        this.$store.commit("store_students", response.data);
      })
      .catch(e => {
        this.errors.push(e);
      });
  },
  computed: {
    stats: function() {
      return {
        total: this.$store.state.students.length,
        borrower: this.get_book_borrowers.length
      };
    },
    students_filtered: function() {
      if (this.$store.state.search_expr.length > 0) {
        var students_filtered = [];
        var expr = this.$store.state.search_expr.toLowerCase();

        for (var i = 0; i < this.$store.state.students.length; i++) {
          var si = this.$store.state.students[i];

          if (
            si.name.toLowerCase().includes(expr) ||
            si.surename.toLowerCase().includes(expr) ||
            si.personal_id.toLowerCase().includes(expr) ||
            si.email.toLowerCase().includes(expr)
          ) {
            students_filtered.push(si);
          }
        }
        return students_filtered;
      } else {
        return this.$store.state.students;
      }
    },
    get_book_borrowers: function() {
      var borrowed = [];
      for (var i = 0; i < this.$store.state.students.length; i++) {
        var si = this.$store.state.students[i];

        if (si.books.length > 0) {
          borrowed.push(si);
        }
      }
      return borrowed;
    }
  },
  methods: {
    is_contained: function(obj, list) {
      return list.some(listElement => {
        return listElement === obj;
      });
    },
    remove_by_attr: function(arr, attr, value) {
      return arr.filter(element => {
        return element[attr] !== value;
      });
    },
    toggle_row: function(row) {
      this.$store.commit("select_row", row);
      if (this.is_contained(row, this.$store.state.selected_students)) {
        this.$store.commit(
          "set_selected_students", 
          this.remove_by_attr(
            this.$store.state.selected_students, "id", row.id)
        );
      } else {
        this.$store.commit("add_selected_student", row);
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
}
</style>
