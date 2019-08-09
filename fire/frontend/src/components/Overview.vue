<template>
  <div class="overview-main">
    <el-card class="overview-voltage-card" slot="header">
      <span>设备安装</span>
      <div id="voltage-chart"></div>
    </el-card>
    <el-card class="overview-install-card" slot="header">
      <span>设备在线</span>
      <div id="install-chart"></div>
    </el-card>
    <el-card class="overview-map-card">
      <div id="map-chart"></div>
    </el-card>
    <el-card class="overview-amount-card" slot="header">
      <span>装置数量</span>
      <div id="amount-chart"></div>
    </el-card>
    <el-card class="overview-wheather-card" slot="header">
      <span>微气象</span>
      <div id="wheather-chart"></div>
    </el-card>
    <el-card class="overview-message-card" slot="header">
      <span>报警信息</span>
    </el-card>
    <el-card class="overview-img-card">
      <span>预警图片</span>
    </el-card>
  </div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'Overview',
  data () {
    return {
      voltageChart: echarts.init(document.getElementById('voltage-chart')),
      installChart: echarts.init(document.getElementById('install-chart')),
      sensorChart: echarts.init(document.getElementById('amount-chart'))
    }
  },
  mounted () {

  },
  methods: {
    InitChart () {

    }
  }
}
</script>

<style scoped>
.overview-main {
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-template-rows: repeat(2,1fr);
  grid-template-areas:
    "voltage map map message"
    "install amount wheather img";
  grid-gap: 20px;
}
.overview-amount-card{
  grid-area: amount;
}
.overview-voltage-card{
  grid-area: voltage;
}
.overview-map-card{
  grid-area: map;
}
.overview-message-card{
  grid-area: message;
}
.overview-install-card{
  grid-area: install;
}
.overview-wheather-card{
  grid-area: wheather;
}
.overview-img-card{
  grid-area: img;
}
.overview-main .el-card {
  background-color: rgba(255, 255, 255, .4);
  border: 0;
}
</style>
