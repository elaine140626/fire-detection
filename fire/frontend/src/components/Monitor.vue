<template>
    <div style="height: 100%; width: 100%;">
      <el-row>
        <el-col :span="4">
          1
        </el-col>
        <el-col :span="20">
          2
        </el-col>
      </el-row>
    </div>
</template>

<script>
export default {
  name: 'Monitor',
  data () {
    return {
      videos: []
    }
  },
  mounted () {
    this.$axios.get('')
      .catch()
      .then()
  }
}
</script>

<style scoped>
.el-col {
  max-height: 100%;
}
</style>
