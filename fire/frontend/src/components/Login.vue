<template>
  <el-card>
    <h2>登录</h2>
    <el-form label-position="left">
      <el-form-item label="用户名">
        <el-input v-model="user"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input show-password v-model="password"></el-input>
      </el-form-item>
    </el-form>
    <el-button type="primary" @click="OnLogin">登录</el-button>
  </el-card>
</template>

<script>
import BlurCard from '@/components/BlurCard'
export default {
  name: 'Login',
  components: {
    BlurCard
  },
  data () {
    return {
      user: '',
      password: ''
    }
  },
  methods: {
    OnLogin () {
      this.$axios.post(this.urlHead + '/api/user/login/', {
        username: this.user,
        password: this.password,
        withcredential: true
      })
        .then((e) => {
          console.log(e)
          this.$notify({
            title: '成功',
            message: e.data,
            type: 'success',
            duration: 2500
          })
          this.$router.push('test')
        })
        .catch((e) => {
          this.$notify({
            title: '失败',
            message: e.data,
            type: 'warning',
            duration: 2500
          })
        })
    }
  }
}
</script>

<style scoped>
.el-input{
  width: 400px;
  max-width: 80%;
}
.el-card {
  background: rgba(255, 255, 255, .9);
  border: 0;
  padding: 10px 30px;
}
.el-form-item__label {
  color: #f3f3f3;
  font-size: 20px;
}
</style>
