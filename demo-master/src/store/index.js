import Vue from 'vue'
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";


Vue.use(Vuex)


let store = new Vuex.Store({

  //数据的唯一来源
  state: {
    loginInfo: {},          // 登录用户的信息
    allPaths: [],           // 允许访问的所有路由 用于权限控制
  },
  getters: {
    isLogin: state => {
      return state.loginInfo && state.loginInfo.access_token
    },
    //登录token=》access_token
    token: state => {
      return state.loginInfo.access_token || ""
    },
    //登录用户信息=》auth_info
    userInfo: state => {
      return state.loginInfo.auth_info || {}
    },
  },

  //状态修改的唯一方法
  mutations: {
    changeToken(state, loginInfo) {
      state.loginInfo = loginInfo;
    },
  },
  actions: {},
  plugins: [createPersistedState()]
})
export default store
