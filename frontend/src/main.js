import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuex from "vuex";

Vue.config.productionTip = false;
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    count: 0,
    selected: {},
    selected_rows: [],
    selected_books: [],
    selected_students: [],
    search_expr: "",
    students: {},
    books: {},
    selected_category: ""
  },
  mutations: {
    set_search_expr(state, expr) {
      state.search_expr = expr;
    },
    set_selected_books(state, rows) {
      state.selected_books = rows;
    },
    add_selected_book(state, item) {
      state.selected_books.push(item);
    },
    set_selected_students(state, rows) {
      state.selected_students = rows;
    },
    add_selected_student(state, item) {
      state.selected_students.push(item);
    },
    store_students(state, data) {
      state.students = data;
    },
    store_books(state, data) {
      state.books = data;
    },
    select_row(state, item) {
      state.selected = item;
    },
    select_a_category(state, item) {
      state.selected_category = item
    }
  }
});

new Vue({
  el: "#app",
  router,
  store,
  render: h => h(App)
}).$mount("#app");
