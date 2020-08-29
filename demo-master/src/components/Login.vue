<template>
    <div id="container">
    <div class="login">
        <el-form :model="form" :rules="rules" ref="form" label-width="80px">
            <el-form-item label="用户名" prop="name">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="form.password" type="password" show-password></el-input>
            </el-form-item>
            <el-form-item label="权限" prop="qx">
                <el-radio-group v-model="form.qx">
                    <el-radio :label="1">管理员</el-radio>
                    <el-radio :label="2">用户</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item>
                <el-button @click="submitHandle">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
    </div>
</template>
<script>
    export default {
        name: "Login",
        data() {
            return {
                form: {
                    name: '',
                    password: '',
                    qx:""
                },
                rules: {
                    name: [
                        { require:true, trigger: 'blur' ,message:'用户名不可以为空'},
                        {min:2,max:10,message:'请输入3-10个字符',trigger:'blur'}
                    ],
                    password: [
                        {  trigger: 'blur',require:true,message:'用户名不可以为空' }
                    ],

                }
            };
        },
        methods:{
            submitHandle(){
                // let data = this.data
                // this.$store.commit('changeToken',data)

                fetch(HOSTNAME+'/admin/login/index',{
                    method:'post',
                    body:JSON.stringify(this.form),
                    headers:{
                        'Content-Type':'application/json'
                    }
                })
                    .then(res=>res.json())
                    .then(data=>{
                        if (data.code==SUCCESS){
                            window.console.log(this);
                            let redirect=this.$route.query.redirect||'mains';
                            this.$message.success(data.msg);
                            sessionStorage.token=data.data.token;
                            sessionStorage.name=data.data.name;
                            this.$router.push({name:redirect});
                        } else if (data.code==FAIL){
                            this.$message.error(data.msg);
                        }
                    })
            }
        }
    }
</script>

<style scoped lang="scss">
    #container{
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        left: 0;
        background-repeat: no-repeat;
        background-size: 100% 100%;
        background-position: center;
    }
    $width:400px;
    $height:350px;
    @mixin centerMid{
        position: absolute;
        left: 50%;
        top:50%;
        transform: translate(-50%,-50%);
    }

    .login{
        width: $width;
        height: $height;
        background-color: rgba(255,255,255,0.5);
        box-shadow:0 0 10px 0 rgba(0,0,0,0.2) ;
        padding: 50px;
        @include centerMid
    }
</style>
