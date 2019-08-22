<template>
  <el-row id="the-base-header">
    <el-row class="hidden-lg-and-up">
      <h2>
        山大i-Learn智能烟火检测系统
      </h2>
    </el-row>
    <el-row type="flex" align="middle" class="hidden-sm-and-down">
      <el-col :span="14" class="hidden-md-and-down">
        <h2>
          山大i-Learn智能烟火检测系统
        </h2>
      </el-col>
      <el-col  class="hidden-sm-and-down">
        <el-button @click="routeTo('overview')">
          系统总览
        </el-button>
        <el-button @click="routeTo('monitor')">
          监控可视化
        </el-button>
        <el-button @click="routeTo('warning')">
          告警分析
        </el-button>
        <el-button>
          日志管理
        </el-button>
        <el-button>
          推送系统
        </el-button>
        <el-button @click="routeTo('config')">
          系统配置
        </el-button>
      </el-col>
      <el-col :span="4">
        <el-dropdown trigger="hover">
        <span>
          username <i class="el-icon-user el-icon--right"></i>
        </span>
          <el-dropdown-menu>
            <el-dropdown-item>
              aaa
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-row>
    <el-row>
      <el-col class="hidden-md-and-up" :span="2">
        <el-dropdown trigger="click" class="el-dropdown-link" @command="routeTo">
          <el-button>
            <i class="el-icon-menu"></i>
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item icon="el-icon-info" command="overview">系统总览</el-dropdown-item>
            <el-dropdown-item icon="el-icon-video-camera" command="monitor">监控可视化</el-dropdown-item>
            <el-dropdown-item icon="el-icon-edit-outline" command="warning">告警分析</el-dropdown-item>
            <el-dropdown-item icon="el-icon-notebook-1">日志管理</el-dropdown-item>
            <el-dropdown-item icon="el-icon-connection">推送系统</el-dropdown-item>
            <el-dropdown-item icon="el-icon-setting" command="conf">系统配置</el-dropdown-item>
            <el-dropdown-item icon="el-icon-switch-button">退出系统</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-row>
  </el-row>
</template>

<script>
export default {
  name: 'BaseHeader',
  data () {
    return {

    }
  },
  methods: {
    routeTo (loc) {
      this.$router.push(loc)
    }
  }
}
</script>

<style>
  #the-base-header {
    background: rgba(255, 255, 255, .3);
  }
  #the-base-header::after{
    background: rgba(255,255,255,1);
    filter: blur(4px);
  }
  #the-base-header h2 {
    color: #f3f3f3;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size: 25px;
  }
  #the-base-header button{
    color: #f3f3f3;
    background: rgba(255,255,255,0);
    border: 0;
  }
  #the-base-header button :hover{
  }
</style>
