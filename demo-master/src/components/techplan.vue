<template>
  <div class="container">
    <div class="title">计划信息管理</div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>计划信息管理</el-breadcrumb-item>
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
          @click="addPlan"
        >添加计划信息</el-button>
      </div>
      <!-- 一张表 -->
      <el-table
        :data="tecPlanList"
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
          prop="subject"
          label="计划信息"
          align="center"
        ></el-table-column>
        <el-table-column
          label="是否完成"
          align="center"
        >
          <template slot-scope="scope">
            <el-tag :type="isFinished(scope.row.status)">{{ FinishedOrNot(scope.row.status) }}</el-tag>
          </template>
        </el-table-column>
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

    <!-- 添加计划对话框 -->
    <el-dialog
      title="添加计划信息"
      :visible.sync="addVisible"
      width="40%"
      center
    >
      <el-form
        ref="addTecPlanRef"
        :model="addTecPlanData"
        label-width="120px"
        :rules="addRules"
      >
        <el-form-item
          label="计划标题"
          prop="subject"
        >
          <el-input v-model="addTecPlanData.subject"></el-input>
        </el-form-item>
        <el-form-item
          label="备注"
          prop="remarks"
        >
          <el-input v-model="addTecPlanData.remarks"></el-input>
        </el-form-item>
        <el-form-item
          label="科室"
          prop="department_id"
        >
          <el-select
            v-model="depart_value"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="item in depart_options"
              :key="item.value"
              :label="item.department_name"
              :value="item.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <!-- <el-form-item
          label="完成情况"
          prop="weekno_term"
        >
          <el-switch
            style="display: block"
            v-model="isComplated"
            active-color="#13ce66"
            inactive-color="#ff4949"
            active-text="是"
            inactive-text="否"
            @change="switchChange"
          >
          </el-switch>
        </el-form-item> -->
        <el-form-item
          label="周次"
          prop="weekno_no"
        >
          <el-select
            v-model="term_value"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item,index) in term_options"
              :key="index"
              :label="item"
              :value="index"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="cancelAdd">取 消</el-button>
        <el-button
          type="primary"
          @click="addTecPlanment"
        >确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改计划对话框 -->
    <el-dialog
      title="修改计划信息"
      :visible.sync="editVisible"
      width="40%"
      center
    >
      <el-form
        ref="editTecPlanRef"
        :model="editTecPlanData"
        label-width="120px"
        :rules="addRules"
      >
        <el-form-item
          label="计划标题"
          prop="subject"
        >
          <el-input v-model="editTecPlanData.subject"></el-input>
        </el-form-item>
        <el-form-item
          label="备注"
          prop="remarks"
        >
          <el-input v-model="editTecPlanData.remarks"></el-input>
        </el-form-item>
        <el-form-item
          label="科室"
          prop="department_id"
        >
          <el-select
            v-model="depart_value1"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="item in depart_options"
              :key="item.id"
              :label="item.department_name"
              :value="item.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="完成情况"
          prop="weekno_term"
        >
          <el-switch
            style="display: block"
            v-model="editisComplated"
            active-color="#13ce66"
            inactive-color="#ff4949"
            active-text="是"
            inactive-text="否"
          >
          </el-switch>
        </el-form-item>
        <el-form-item
          label="周次"
          prop="weekno_no"
        >
          <el-select
            v-model="term_value1"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="(item,index) in term_options"
              :key="index"
              :label="item"
              :value="index"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="editVisible = false">取 消</el-button>
        <el-button
          type="primary"
          @click="editTecPlanment"
        >确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    var validate = (rule, value, callback) => {
      const reg = /[^\u4E00-\u9FA5A-Za-z,，.。!！0-9 ?？_]/g
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
      tecPlanList: [],
      addVisible: false,
      editVisible: false,
      addTecPlanData: {
        subject: '',
        remarks: '',
        department_id: ''
      },
      editTecPlanData: {
        subject: '',
        remarks: '',
        department_id: ''
      },
      id: '',
      depart_value: '',
      term_value: '',
      depart_options: [],
      term_options: [],
      isComplated: false,
      editisComplated: true,
      status: '',
      editstatus: '',
      depart_value1: '',
      term_value1: '',
      addRules: {
        subject: [
          { required: true, message: '请输入正确格式', trigger: ['blur', 'change'] },
          { validator: validate }
        ]
      }
    }
  },
  methods: {
    addPlan () {
      this.getDepartmentList()
      this.getTecWeekList()
      this.addVisible = true
    },
    async getDepartmentList () {
      const { data: res } = await this.$http.get('api/department')
      if (res.status !== 'successed') {
        return this.$message.error('获取科室信息失败！')
      }
      this.depart_options = res.results
    },
    async getTecWeekList () {
      const { data: res } = await this.$http.get('api/teachweek/queryweeks')
      if (res.status !== 'successed') {
        return this.$message.error('获取教学周信息失败！')
      }
      console.log(res.results)
      this.term_options = res.results
    },
    async getTecPlanList () {
      const { data: res } = await this.$http.get('api/teachplan')
      if (res.status !== 'successed') {
        return this.$message.error('获取教学周信息失败！')
      }
      this.tecPlanList = res.results
    },

    handleSelectionChange () { },
    // 编辑计划
    editTecPlanment () {
      this.$refs.editTecPlanRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请输入完整信息!')
        }
        var readyData = {
          subject: this.editTecPlanData.subject,
          remarks: this.editTecPlanData.remarks,
          department_id: this.depart_value1,
          status: this.editisComplated,
          week_no: this.term_value1
        }
        const { data: res } = await this.$http.put('api/teachplan/edit/' + this.id, readyData)
        if (res.status !== 'successed') {
          return this.$message.error('修改计划失败')
        }
        this.$message.success('修改计划成功')
        this.getTecPlanList()
        this.editVisible = false
        this.$refs.editTecPlanRef.resetFields()
      })
    },
    // 添加计划
    async addTecPlanment () {
      this.$refs.addTecPlanRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('请输入完整信息!')
        }
        var readyData = {
          subject: this.addTecPlanData.subject,
          remarks: this.addTecPlanData.remarks,
          department_id: this.depart_value,
          status: this.isComplated,
          week_no: this.term_value
        }
        const { data: res } = await this.$http.post('api/teachplan/add', readyData)
        if (res.status !== 'successed') {
          return this.$message.error('添加计划失败')
        }
        this.$message.success('添加计划成功')
        this.getTecPlanList()
        this.addVisible = false
        this.$refs.addTecPlanRef.resetFields()
      })
    },

    // 取消添加对话框
    cancelAdd () {
      this.addVisible = false
      this.$refs.addTecPlanRef.resetFields()
    },

    handleDelete (row) {
      // 二次确认删除
      this.$confirm('确定要删除 ' + row.subject + ' 吗？', '提示', {
        type: 'warning'
      })
        .then(async () => {
          await this.$http.post('api/teachplan/delete/' + row.id)
          this.$message.success('删除成功')
          this.getTecPlanList()
        })
        .catch(() => { })
    },

    handleEdit (row) {
      this.getDepartmentList()
      this.getTecWeekList()
      this.editTecPlanData.subject = row.subject
      this.editTecPlanData.remarks = row.remarks
      this.editisComplated = row.status
      this.depart_value1 = Number(row.department_id)
      this.editisComplated = row.status
      this.term_value1 = row.week_no
      this.id = row.id
      this.editVisible = true
    },
    switchChange () {
      if (this.isComplated === true) {
        this.status = 1
      } else {
        this.status = 0
      }
    },
    switchChange1 () {
      if (this.editisComplated === true) {
        this.editstatus = 1
      } else {
        this.editstatus = 0
      }
    },
    isFinished (status) {
      if (status) {
        return 'success'
      } else {
        return 'danger'
      }
    },
    FinishedOrNot (status) {
      if (status) {
        return '已完成'
      } else {
        return '未完成'
      }
    }
  },
  mounted () {
    this.getTecPlanList()
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
