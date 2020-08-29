import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import techweek from '../components/techweek.vue'
import techplan from '../components/techplan.vue'
import department from '../components/department.vue'
import departecplan from '../components/departecplan.vue'
import Login from '../components/Login.vue'

Vue.use(VueRouter)

const routes = [
  // 后台路由
  {
    path: '/login',
    component: Login
  },
  {
    path: '/',
    component: Home,
    redirect: 'techweek',
    // 子路由
    children: [
      { path: '/techweek', component: techweek, meta: { title: '教学周管理' } },
      { path: '/techplan', component: techplan, meta: { title: '教学计划管理' } },
      { path: '/department', component: department, meta: { title: '科室信息管理' } },
      { path: '/department/departechplan', component: departecplan }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL, // 去掉url中的#
  routes
})

export default router
