<template>
  <div class="container">
    <div class="title">科室信息管理</div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>科室信息管理</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card>
      <!-- 搜索 -->
      <div class="search">
        <el-select
          v-model="searchData"
          clearable
          placeholder="请选择"
        >
          <el-option
            v-for="item in searchList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
        <!-- 执行按钮 -->
        <!-- <el-button
          class="zhixin"
          type="primary"
        >执行</el-button> -->
        <!-- 查找按钮
        <el-button
          class="addDepart"
          icon="el-icon-circle-plus-outline"
          type="success"
          @click="addVisible=true"
        >添加科室信息</el-button> -->
      </div>
      <!-- 一张表 -->
      <el-table
        :data="departDataList"
        border
        stripe
        height="400"
        ref="multipleTable"
        header-cell-class-name="table-header"
        @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          width="55"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="department_name"
          label="科室信息"
          align="center"
        ></el-table-column>
        <el-table-column
          label="操作"
          align="center"
        >
          <template slot-scope="scope">
            <el-button
              type="text"
              icon="el-icon-search"
              @click="handleSearch(scope.row)"
            >查看科室计划</el-button>
            <el-button
              type="text"
              icon="el-icon-edit"
              @click="handleEdit(scope.row)"
            >编辑</el-button>
            <el-button
              type="text"
              icon="el-icon-delete"
              class="red"
              @click="handleDelete(scope.row)"
            >删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 添加科室对话框
    <el-dialog
      title="添加科室"
      :visible.sync="addVisible"
      width="40%"
      center
    >
      <el-form
        ref="addDepartmentRef"
        :model="addDepartmentData"
        label-width="100px"
        :rules="addDepartmentRules"
      >
        <el-form-item
          label="科室名称"
          prop="department_name"
        >
          <el-input
            v-model="addDepartmentData.department_name"
            placeholder="请输入科室名称"
          ></el-input>
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="addVisible = false">取 消</el-button>
        <el-button
          type="primary"
          @click="addDepartment"
        >确 定</el-button>
      </span>
    </el-dialog> -->

    <!-- 编辑科室对话框 -->
    <el-dialog
      title="编辑科室"
      :visible.sync="editVisible"
      width="40%"
      center
    >
      <el-form
        ref="editDepartmentRef"
        :model="editDepartmentData"
        label-width="100px"
        :rules="addDepartmentRules"
      >
        <el-form-item
          label="科室名称"
          prop="department_name"
        >
          <el-input
            v-model="editDepartmentData.department_name"
            placeholder="请输入科室名称"
          ></el-input>
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="editVisible = false">取 消</el-button>
        <el-button
          type="primary"
          @click="editDepartment"
        >确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    var validateDepart = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入科室名称'))
      } else {
        callback()
      }
    }
    return {
      searchData: '',
      searchList: [
        { value: '选项1', label: '教学1' },
        { value: '选项2', label: '教学2' },
        { value: '选项3', label: '教学3' }
      ],
      addDepartmentRules: {
        department_name: [
          { required: true, validator: validateDepart, trigger: ['blur', 'change'] }
        ]
      },
      departDataList: [],
      addVisible: false,
      editVisible: false,
      addDepartmentData: {
        department_name: ''
      },
      editDepartmentData: {
        department_name: ''
      },
      id: ''
    }
  },
  methods: {
    async getDepartments () {
      const { data: res } = await this.$http.get('api/department')
      if (res.status !== 'successed') {
        return this.$message.error('获取科室信息失败！')
      }
      this.departDataList = res.results
    },

    handleSelectionChange () { },
    // 添加部门
    addDepartment () {
      this.$refs.addDepartmentRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请输入完整信息!')
        }
        var readyData = { department_name: this.addDepartmentData.department_name }
        const { data: res } = await this.$http.post('api/department/add', readyData)
        if (res.status !== 'successed') {
          return this.$message.error('添加科室失败！')
        }
        this.getDepartments()
        this.addVisible = false
        this.addDepartmentData.department_name = ''
      })
    },

    handleDelete (row) {
      // 二次确认删除
      this.$confirm('确定要删除 ' + row.department_name + ' 吗？', '提示', {
        type: 'warning'
      })
        .then(async () => {
          await this.$http.post('api/department/delete/' + row.id)
          this.$message.success('删除成功')
          this.getDepartments()
        })
        .catch(() => { })
    },

    handleEdit (row) {
      this.editDepartmentData.department_name = row.department_name
      this.id = row.id
      this.editVisible = true
    },

    handleSearch (row) {
      this.$router.push({ path: 'department/departechplan', query: { id: row.id } })
    },

    editDepartment () {
      this.$refs.editDepartmentRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请输入完整信息!')
        }
        var readyData = { department_name: this.editDepartmentData.department_name }
        const { data: res } = await this.$http.put('api/department/edit/' + this.id, readyData)
        if (res.status !== 'successed') {
          return this.$message.error('编辑失败')
        }
        this.$message.success('编辑成功！')
        this.editVisible = false
        this.getDepartments()
      })
    }
  },
  mounted () {
    this.getDepartments()
  }
}
</script>

<style scoped>
.el-main {
  padding: 10px;
}
.container {
  padding: 10px;
}
.title {
  font-size: 30px;
}
.el-breadcrumb,
.el-card,
.el-table {
  margin-top: 15px;
}
.zhixin {
  margin-left: 10px;
}
.addDepart {
  float: right;
}
.red {
  color: rgb(245, 108, 108);
}
</style>
