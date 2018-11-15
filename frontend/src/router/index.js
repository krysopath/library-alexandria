import Vue from "vue";
import Router from "vue-router";

const routerOptions = [
  { path: "/", component: "Home" },
  { path: "/books", component: "Books" },
  { path: "/students", component: "Students" }
];

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  };
});

Vue.use(Router);

export default new Router({
  routes,
  mode: "hash"
});
