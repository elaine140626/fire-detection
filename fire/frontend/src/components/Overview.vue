<template>
  <div class="overview-main">
    <el-card class="overview-voltage-card" slot="header">
      <span>设备安装</span>
      <div id="voltage-chart" style="height: 100%;"></div>
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
import BMap from 'BMap'
var echarts = require('echarts')
export default {
  name: 'Overview',
  data () {
    return {
    }
  },
  mounted: function () {
    var voltageChart = echarts.init(document.getElementById('voltage-chart'))
    var installChart = echarts.init(document.getElementById('install-chart'))
    var sensorChart = echarts.init(document.getElementById('wheather-chart'))
    let option = {
      // backgroundColor: '#2c343c',
      title: {
        // text:'设备安装数量统计图'
      },
      tooltip: {},
      legend: {
        data: ['用户来源']
      },
      xAxis: {
        data: ['110', '110kV', '220kV']
      },
      yAxis: {
        name: 'Amount'
      },
      series: [{
        name: '设备数量',
        type: 'bar',
        data: [22, 3, 16],
        itemStyle: {
          color: 'rgb(9, 38, 78)',
          barBorderRadius: [5, 5, 0, 0],
          opacity: 0.5
        },
        labelLine: {
          normal: {
            lineStyle: {
              color: 'rgba(255, 255, 255, 0.3)'
            },
            smooth: 0.2,
            length: 10,
            length2: 20
          }
        }
      }],
      barWidth: 30
    }
    let option2 = {
      // backgroundColor: transparent,
      optical: 0.5,

      title: {
        // text:'装备在线统计图',
        // left: 'center',
        // top: 20,
        // textStyle: {
        //     color: '#ccc'
        // }
      },

      tooltip: {
        trigger: 'item',
        formatter: '{a}  --- {b} : {c} ({d}%)'
      },

      visualMap: {
        show: false,
        min: 80,
        max: 600,
        inRange: {
          colorLightness: [0, 1]
        }
      },
      series: [
        {
          name: '设备数量',
          type: 'pie',
          radius: ['55%', '10%'],
          minAngle: 3,
          center: ['50%', '50%'],
          data: [
            {value: 335, name: '在线'},
            {value: 0, name: '离线'}
          ].sort(function (a, b) {
            return a.value - b.value
          }),
          label: {
            normal: {
              textStyle: {
                color: 'rgba(255, 255, 255, 0.3)'
              }
            }
          },
          labelLine: {
            normal: {
              lineStyle: {
                color: 'rgba(255, 255, 255, 0.3)'
              },
              smooth: 0.2,
              length: 20,
              length2: 50
            }
          },
          itemStyle: {
            normal: {
              color: 'rgba(48, 228, 183,0.2)',
              shadowBlur: 200,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
          // animationType: 'scale',
          // animationEasing: 'elasticOut',
        }
      ]
    }
    let option3 = {
      // title: {
      //     text: '微气象'
      // },
      tooltip: {},
      legend: {
        data: ['此刻 ( Present )', '昨天 ( Yesterday )']
      },
      radar: {
        // shape: 'circle',
        radius: '70%',
        name: {
          textStyle: {
            color: '#fff',
            backgroundColor: '#999',
            borderRadius: 3,
            padding: [3, 5]
          }
        },
        indicator: [
          {name: '风向', max: 360},
          {name: '雨量', max: 50},
          {name: '风速', max: 10},
          {name: '气压', max: 1500}
        ]
      },
      series: [{
        name: '昨日 vs 此刻（Yesterday vs At present）',
        type: 'radar',
        // areaStyle: {normal: {}},
        data: [
          {
            value: [15, 1.1, 0.5, 1230],
            name: '此刻 ( Present )'
          },
          {
            value: [285, 10, 0.7, 1300],
            name: '昨天 ( Yesterday )'
          }
        ]
      }]
    }

    voltageChart.setOption(option)
    installChart.setOption(option2)
    sensorChart.setOption(option3)

    window.onresize = function () {
      voltageChart.resize()
      installChart.resize()
      sensorChart.resize()

      // var mapScipt = document.createElement('script')
      // mapScipt.src = 'http://api.map.baidu.com/api?v=3.0&ak=QsGnMSGuvCa3B680i1DHAL3cDG8COE3e'
      // document.body.appendChild(mapScipt)
    }
    var map = new BMap.Map('map-chart')
    var point = new BMap.Point(120.697792, 36.369133)
    map.centerAndZoom(point, 15)
  },
  methods: {
    ResizeChart () {
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
.el-card {
  display: grid;
}
.el-card__body {
  align-self: stretch;
}
.el-card__body div{
  height: 100%;
  width: 100%;
}
</style>
