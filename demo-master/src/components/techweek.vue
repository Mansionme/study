<template>
  <div class="container">
    <div class="title">教学周信息管理</div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>教学周信息管理</el-breadcrumb-item>
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
        <!-- 查找按钮 -->
        <el-button
          class="addDepart"
          icon="el-icon-circle-plus-outline"
          type="success"
          @click="addVisible=true"
          v-if = "userInfo == 1"
        >添加教学周信息</el-button>
      </div>
      <!-- 一张表 -->
      <el-table
        :data="tecWeekList"
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
          prop="weekno_term"
          label="教学周信息"
          align="center"
        ></el-table-column>
        <el-table-column
          label="操作"
          align="center"
        >
          <template slot-scope="scope">
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

    <!-- 添加教学周对话框 -->
    <el-dialog
      title="添加教学周"
      :visible.sync="addVisible"
      width="40%"
      center
    >
      <el-form
        ref="addTecWeekRef"
        :model="addTecWeekData"
        label-width="160px"
        :rules="addRules"
      >
        <el-form-item
          label="学期"
          prop="term"
        >
          <el-input
            class="weekno_term"
            v-model="addTecWeekData.term"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="教学周开始_结束日期"
          prop="start_endDate"
        >
          <el-date-picker
            v-model="addTecWeekData.start_endDate"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            value-format="yyyy-MM-dd"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          label="教学周次_学期"
          prop="weekno_term"
        >
          <el-input
            class="weekno_term"
            v-model="addTecWeekData.weekno_term"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="教学周次"
          prop="weekno_no"
        >
          <el-input
            class="weekno_no"
            v-model="addTecWeekData.weekno_no"
          ></el-input>
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="cancelAdd">取 消</el-button>
        <el-button
          type="primary"
          @click="addTecWeekment"
        >确 定</el-button>
      </span>
    </el-dialog>

    <!-- 编辑科室对话框 -->
    <el-dialog
      title="编辑教学周信息"
      :visible.sync="editVisible"
      width="40%"
      center
    >
      <el-form
        ref="editTecWeekRef"
        :model="editTecWeekData"
        label-width="160px"
        :rules="addRules"
      >
        <el-form-item
          label="学期"
          prop="term"
        >
          <el-input
            class="weekno_term"
            v-model="editTecWeekData.term"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="教学周开始_结束日期"
          prop="start_endDate"
        >
          <el-date-picker
            v-model="editTecWeekData.start_endDate"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            value-format="yyyy-MM-dd"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          label="教学周次_学期"
          prop="weekno_term"
        >
          <el-input
            class="weekno_term"
            v-model="editTecWeekData.weekno_term"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="教学周次"
          prop="weekno_no"
        >
          <el-input
            class="weekno_no"
            v-model="editTecWeekData.weekno_no"
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
          @click="editTecWeekment"
        >确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    var validate = (rule, value, callback) => {
      const reg = /[^\d+(,\d\d\d)*-\d+$]/g
      if (reg.test(value)) {
        callback(new Error('请输入正确格式'))
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
      tecWeekList: [],
      addVisible: false,
      editVisible: false,
      addTecWeekData: {
        term: '',
        start_endDate: '',
        weekno_term: '',
        weekno_no: ''
      },
      editTecWeekData: {
        term: '',
        start_endDate: '',
        weekno_term: '',
        weekno_no: ''
      },
      id: '',
      editweek: '',
      term: '',
      editTerm: '',
      addRules: {
        term: [
          { required: true, message: '请输入正确学期', trigger: ['blur', 'change'] },
          { validator: validate }
        ],
        start_endDate: [
          { required: true, message: '请选择开始和结束日期', trigger: 'blur' }
        ],
        weekno_term: [
          { required: true, message: '请输入正确周次学期', trigger: ['blur', 'change'] },
          { validator: validate }
        ],
        weekno_no: [
          { required: true, message: '请输入正确教学周次', trigger: ['blur', 'change'] },
          { validator: validate }
        ]
      }
    }
  },
  methods: {
    async getTecWeekList () {
      const { data: res } = await this.$http.get('api/teachweek')
      if (res.status !== 'successed') {
        return this.$message.error('获取教学周信息失败！')
      }
      this.tecWeekList = res.results
    },

    handleSelectionChange () { },
    // 编辑教学周计划
    editTecWeekment () {
      this.$refs.editTecWeekRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请输入完整信息!')
        }
        var readyData = {
          term: this.editTecWeekData.weekno_term,
          week_start: this.editTecWeekData.start_endDate[0],
          week_end: this.editTecWeekData.start_endDate[1],
          weekno_term: this.editTecWeekData.weekno_term,
          week_no: this.editTecWeekData.weekno_no
        }
        const { data: res } = await this.$http.put('api/teachweek/edit/' + this.id, readyData)
        if (res.status !== 'successed') {
          return this.$message.error('修改教学周失败！')
        }
        this.$message.success('修改教学周成功！')
        this.getTecWeekList()
        this.editVisible = false
        this.$refs.editTecWeekRef.resetFields()
      })
    },
    // 添加教学周计划
    addTecWeekment () {
      this.$refs.addTecWeekRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请输入完整信息!')
        }
        var readyData = {
          term: this.addTecWeekData.weekno_term,
          week_start: this.addTecWeekData.start_endDate[0],
          week_end: this.addTecWeekData.start_endDate[1],
          weekno_term: this.addTecWeekData.weekno_term,
          week_no: this.addTecWeekData.weekno_no
        }
        const { data: res } = await this.$http.post('api/teachweek/add', readyData)
        if (res.status !== 'successed') {
          return this.$message.error('添加教学周失败！')
        }
        this.$message.success('添加教学周成功！')
        this.getTecWeekList()
        this.$refs.addTecWeekRef.resetFields()
        this.addVisible = false
      })
    },
    // 取消添加对话框
    cancelAdd () {
      this.addVisible = false
      this.$refs.addTecWeekRef.resetFields()
    },

    handleDelete (row) {
      // 二次确认删除
      this.$confirm('确定要删除 ' + row.term + ' 吗？', '提示', {
        type: 'warning'
      })
        .then(async () => {
          await this.$http.post('api/teachweek/delete/' + row.id)
          this.$message.success('删除成功')
          this.getTecWeekList()
        })
        .catch(() => { })
    },

    handleEdit (row) {
      this.editTecWeekData.term = row.term
      this.editTecWeekData.weekno_term = row.weekno_term
      this.editTecWeekData.weekno_no = row.week_no
      this.id = row.id
      this.editVisible = true
    },

    async editDepartment () {
      var readyData = { department_name: this.editDepartmentData.department_name }
      const { data: res } = await this.$http.put('api/department/edit/' + this.id, readyData)
      if (res.status !== 'successed') {
        return this.$message.error('编辑失败')
      }
      this.$message.success('编辑成功！')
      this.editVisible = false
      this.getDepartments()
    },

    getWeekCount (date1, date2) {
      console.log(date1 + '-' + date2)
      var _dt2 = new Date(date1)
      var _dt1 = new Date(date2)
      var dt1 = _dt1.getTime()
      var dt2 = _dt2.getTime()
      return parseInt(Math.abs(dt1 - dt2) / 1000 / 60 / 60 / 24 / 7)// 这里是计算天数,如果想获得周数则在该返回值上再除以7
    },
    // 学期输入改变
    termNumChange (val) {
    }
  },
  mounted () {
    this.getTecWeekList()
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
.weekno_no,
.weekno_term {
  width: 220px;
}
</style>
