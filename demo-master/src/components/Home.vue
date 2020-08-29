<template>
  <el-container
    class="home_container"
    :style="'height:'+fullHeight+'px;'"
  >
    <!-- 头部区域 -->
    <el-header>
      <div class="title">
        <span>东北林业大学教务处工作计划</span>
      </div>
      <!-- <el-button
        type="danger"
        @click="logout"
      >退出</el-button> -->
    </el-header>
    <!-- 页面主题区域 -->
    <el-container>
      <!-- 侧栏导肮区域 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <!-- 菜单区域 -->
        <div
          class="zhedie_button"
          @click="setCollapse"
        >
          <span>|||</span>
        </div>
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#323744"
          text-color="#fff"
          active-text-color="#00B5E5"
          unique-opened
          :collapse="isCollapse"
          :collapse-transition="false"
          router
          :default-active="activePath"
        >
          <!-- 一级菜单 -->
          <el-submenu
            :index="item.id+''"
            v-for="item in menulist"
            :key="item.id"
          >
            <!-- 一级菜单模板区域 -->
            <template slot="title">
              <!-- 图标 -->
              <i :class="iconObj[item.id]"></i>
              <span>{{ item.authName }}</span>
            </template>
            <!-- 二级菜单 -->
            <el-menu-item
              :index="'/'+subitem.path"
              v-for="subitem in item.children"
              :key="subitem.id"
              @click="setActivePath('/'+subitem.path)"
            >
              <!-- 二级菜单模板区域 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-menu"></i>
                <span>{{ subitem.authName }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 左侧内容主题 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      id: '',
      fullHeight: document.documentElement.clientHeight,
      // 左侧菜单数据
      menulist: [
        { id: '1', authName: '教学管理', children: [{ id: '1', authName: '教学周信息管理', path: 'techweek' }, { id: '2', authName: '科室信息管理', path: 'department' }, { id: '3', authName: '计划信息管理', path: 'techplan' }] },
        { id: '2', authName: '用户设置' }
      ],
      iconObj: {
        1: 'el-icon-user-solid',
        2: 'el-icon-s-tools'
      },
      isCollapse: false,
      activePath: ''
    }
  },
  watch: {
    fullHeight (val) { // 监控浏览器高度变化
      if (!this.timer) {
        this.fullHeight = val
        this.timer = true
        const that = this
        setTimeout(function () {
          that.timer = false
        }, 400)
      }
    }
  },
  mounted () {
    this.get_bodyHeight()
  },
  methods: {
    async logout () {
    },
    setCollapse () {
      this.isCollapse = !this.isCollapse
    },
    setActivePath (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = window.sessionStorage.getItem('activePath')
    },
    get_bodyHeight () { // 动态获取浏览器高度
      const that = this
      window.onresize = () => {
        return (() => {
          window.fullHeight = document.documentElement.clientHeight
          that.fullHeight = window.fullHeight
        })()
      }
    }
  }
}
</script>

<style scoped>
.title {
  margin-left: 30px;
}
/* .home_container {
  height: 1000px;
} */
.el-header {
  background: rgb(60, 141, 188);
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #e8edf2;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}
.el-aside {
  background: rgb(34, 45, 50);
  height: 100%;
}
.el-main {
  background: #e8edf2;
  height: 100%;
  widows: 100%;
}
.iconfont {
  padding: 10px;
}
.el-menu {
  border-right: 0px;
}
.zhedie_button {
  font-size: 10px;
  line-height: 24px;
  color: #ffffff;
  text-align: center;
  background: rgb(34, 45, 50);
  letter-spacing: 0.2em;
  cursor: pointer;
}
</style>
