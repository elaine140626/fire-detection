<template>
  <el-card
    shadow="hover"
    style="background: rgba(255,255,255,.7); border: 0; min-width: 500px; width: 50%; max-height: 100%;overflow-y: auto"
  >
    <h3>设置</h3>
    <el-form
      ref="form"
      :model="form"
      label-width="100px"
    >
      <el-collapse v-model="activeNames" style="background: transparent;">
        <el-collapse-item title="用户配置 UserConfiguration" name="user">
          <el-form-item label="手机号">
            <el-input v-model="form.info.telephone" size="small"></el-input>
          </el-form-item>
          <el-form-item label="电子邮件">
            <el-input v-model="form.info.email" size="small"></el-input>
          </el-form-item>
          <el-divider></el-divider>
          <el-form-item label="微信ID">
            <el-input v-model="form.info.wechatOpenId" size="small"></el-input>
          </el-form-item>
          <el-divider></el-divider>
          <el-form-item label="布局设置">
            <el-select v-model="form.info.layout" placeholder="请选择视频页面的布局">
              <el-option label="1 x N" value="1"></el-option>
              <el-option label="2 x N" value="2"></el-option>
              <el-option label="4 x N" value="4"></el-option>
              <el-option label="6 x N" value="6"></el-option>
            </el-select>
          </el-form-item>
        </el-collapse-item>
        <el-collapse-item title="视频设置 VideoConfiguration" name="video">
          <el-form-item
            v-for="video in form.videos"
            :key="video.id"
            :prop="video.video_url"
            :label="'视频' + video.id"
            :rules="{
              required: true, message: '视频地址不能为空', trigger:'blur'
            }"
          >
            <el-input v-model="video.video_url" class="video-input"></el-input><el-button @click.prevent="removeVideo(video)">删除</el-button>
          </el-form-item>
          <el-form-item class="" style="justify-content: flex-end">
            <el-button @click="addVideo">新增视频</el-button>
          </el-form-item>
        </el-collapse-item>
      </el-collapse>
      <el-divider></el-divider>
      <el-form-item style="margin-left: 0;" class="flex-center conf-form-button">
        <el-button type="primary" @click="onSubmit">修改</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script>
export default {
  name: 'Conf',
  data () {
    return {
      form: {
        info: {
          telephone: '',
          email: '',
          wechatOpenId: '',
          layout: ''
        },
        videos: []
      },
      activeNames: []
    }
  },
  methods: {
    removeVideo (video) {
      let index = this.form.videos.indexOf(video)
      if (index !== -1) {
        this.form.videos.splice(index, 1)
      }
    },
    addVideo (video) {
      this.form.videos.push({
        video_url: '',
        id: '新增'
      })
    }
  },
  mounted () {
    this.$axios.get(this.urlHead + '/api/user/info/')
      .then((e) => {
        if (e.data.code === 0) {
          this.form.info = e.data.data
        } else {
          this.$notify({
            message: '获取用户配置失败' + e.data.msg,
            type: 'warning'
          })
        }
      })
      .catch(() => {
        this.$notify({
          message: '请求用户配置错误',
          type: 'warning'
        })
      })
    this.$axios.get(this.urlHead + '/api/videos')
      .then((e) => {
        if (e.data.code === 0) {
          this.form.videos = e.data.data
        } else {
          this.$notify({
            message: '获取视频信息失败' + e.data.msg,
            type: 'warning'
          })
        }
      })
      .catch(() => {
        this.$notify({
          message: '请求视频信息失败',
          type: 'warning'
        })
      })
  }
}
</script>

<style>
.el-collapse-item__header {
  background: transparent;
}
.el-collapse-item__wrap {
  background: transparent;
}
.video-input {
  width: 450px;
}
.el-form-item {
  display: flex;
  justify-content: flex-start;
}
.conf-form-button {
  justify-content: center;
}
.conf-form-button .el-form-item__content {
  margin-right: 100px;
}
</style>
