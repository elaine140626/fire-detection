<template>
  <blur-card v-bind:thePadding="30">
    <h2>登录</h2>
<!--    <el-form label-position="top">-->
<!--      <el-form-item label="用户名">-->
<!--        <el-input></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="密码">-->
<!--        <el-input></el-input>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
    <el-form label-position="left" label-width="80px">
      <el-form-item label="名称">
        <el-input ></el-input>
      </el-form-item>
      <el-form-item label="活动区域">
        <el-input ></el-input>
      </el-form-item>
      <el-form-item label="活动形式">
        <el-input></el-input>
      </el-form-item>
    </el-form>
  </blur-card>
</template>

<script>
import BlurCard from '@/components/BlurCard'
export default {
  name: 'Login',
  components: {
    BlurCard
  }
}
</script>

<style scoped>
.el-input{
  width: 400px;
}
</style>
