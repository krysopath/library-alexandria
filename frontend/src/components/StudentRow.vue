<template>
  <tr v-if="is_contained(student, this.$store.state.selected_students)" bgcolor="#ADD8E6">
    <td>{{student.name}} {{student.surename}}</td>
    <td>{{student.personal_id}}</td>
    <td>{{student.email}}</td>
    <td>{{student.books.length}}</td>
    <td></td>
  </tr>
  <tr v-else>
    <td>{{student.name}} {{student.surename}}</td>
    <td>{{student.personal_id}}</td>
    <td>{{student.email}}</td>
    <td>{{student.books.length}}</td>
    <td></td>
  </tr>
</template>

<script>
export default {
  name: "StudentRow",
  props: {
    student: { type: Object }
  },
  data() {
    return {
      students: {}
    };
  },
  created() {},
  computed: {
    selected_rows: function() {
      return this.$store.state.selected_students;
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
