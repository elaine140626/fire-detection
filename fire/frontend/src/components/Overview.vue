<template>
  <div class="overview-main">
    <el-card class="overview-voltage-card" slot="header">
      <span>设备安装</span>
      <div id="voltage-chart" style="height: 100%;"></div>
    </el-card>
    <el-card class="overview-install-card" slot="header">
      <span>设备在线</span>
      <div id="install-chart">
      </div>
    </el-card>
    <el-card class="overview-map-card" style="margin: 0; padding: 0;">
      <el-popover
        ref="popover-message"
        trigger="manual">
        <el-card>
          <h4>设备序列号</h4>
          {{deviceOnShow.serial_number}}
          <h4>提示信息</h4>
          {{deviceOnShow.hint}}
          <h4>视频地址</h4>
          {{deviceOnShow.video_url}}
          <h4>经纬度</h4>
          ({{deviceOnShow.location_x}}, {{deviceOnShow.location_y}})
        </el-card>
        <div id="map-chart" slot="reference" ></div>
      </el-popover>
    </el-card>
    <el-card class="overview-amount-card" slot="header">
      <span>装置数量</span>
      <div id="amount-chart" class="flex-center">
        <div style="display: block; align-items: center; height: auto;">
          <div style="display: block; align-items: center; height: auto;">
              <h4>未读消息: {{messageUnread}}</h4>
            <el-progress :percentage="messagePercentage" :format="MessageFormat"  color="red" style="height:auto;"></el-progress>
          </div>
          <div style="display: block; align-items: center; height: auto;">
            <h4>设备在线: {{deviceOnline}}</h4>
            <el-progress :percentage="devicePercentage"  color="green" style="height:auto;"></el-progress>
          </div>
        </div>
      </div>
    </el-card>
    <el-card class="overview-wheather-card" slot="header">
      <span>微气象</span>
      <div id="wheather-chart"></div>
    </el-card>
    <el-card class="overview-message-card" slot="header">
      <span>报警信息</span>
      <el-carousel
        @change="HandleChange"
        ref="messageCarousel"
        height="30%"
        :autoplay="false"
        type="card"
        direction="vertical"
        indicator-position="outside" >
        <el-carousel-item v-for="message in messages" :key="message.id" class="flex-center">
          {{message.content}}
          <span style="font-size: 13px;">{{message.c_time}}</span>
        </el-carousel-item>
      </el-carousel>
    </el-card>
    <el-card class="overview-img-card">
      <span>预警图片</span>
      <el-carousel @change="HandleChange" :autoplay="autoPlay" ref="imgCarousel" style="align-items: center">
        <el-carousel-item v-for="message in messages" :key="message.id" class="flex-cente r">
          <el-image
            :src="message.img_url"
            style="max-height: 80%;"
            fit="cover"></el-image>
        </el-carousel-item>
      </el-carousel>
    </el-card>
    <el-drawer
      ref="videoDrawer"
      title="设备实时监控"
      :visible.sync="drawer"
      size="85%"
      :destroy-on-close="true"
      @opened="InitVideo"
      direction="btt">
      <video id="myPlayer" controls  playsInline webkit-playsinline>
      </video>
    </el-drawer>
  </div>
</template>

<script>
import EZUIKit from '../../libs/ezuikit.js'
import BMap from 'BMap'
var echarts = require('echarts')
export default {
  name: 'Overview',
  data () {
    return {
      drawer: false,
      device: [],
      messages: [{'id': 1, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428914.6071951.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': true, 'c_time': '2019-06-26'}, {'id': 2, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428914.6071951.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 3, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428915.6183162.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 4, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428921.801521.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': true, 'c_time': '2019-06-26'}, {'id': 5, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428922.8135169.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': true, 'c_time': '2019-06-26'}, {'id': 6, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 7, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428923.8265727.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 8, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428924.8973463.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 9, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428925.974638.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 10, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428928.0553596.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}],
      deviceOnShow: {
        'serial_number': undefined,
        'hint': undefined,
        'location_x': undefined,
        'location_y': undefined,
        'video_url': undefined
      },
      videoOnShow: '',
      autoPlay: true,
      messageUnread: 0,
      messageAmount: 0,
      deviceOnline: 0,
      deviceAmount: 0
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
    }
    this.$refs['popover-message'].doClose()
    var map = new BMap.Map('map-chart')
    var point = new BMap.Point(120.697792, 36.369133)
    map.centerAndZoom(point, 15)

    this.$axios.get(this.urlHead + '/api/devices/all')
      .catch(() => {
        this.$notify({
          message: '无法获取设备信息',
          type: 'warning'
        })
      })
      .then((e) => {
        this.device = e.data.data
        console.log(e)
        this.deviceAmount = this.device.length
        this.deviceOnline = this.device.length
        for (let i = 0; i < this.device.length; i++) {
          let thePoint = new BMap.Point(this.device[i]['location_x'], this.device[i]['location_y'])
          let theMarker = new BMap.Marker(thePoint)

          map.addOverlay(theMarker)

          theMarker.addEventListener('mouseover', () => {
            this.deviceOnShow = this.device[i]
            this.$refs['popover-message'].doShow()
            console.log(this.$refs['popover-message'])
          })

          theMarker.addEventListener('mouseout', () => {
            this.$refs['popover-message'].doClose()
          })

          theMarker.addEventListener('click', () => {
            this.ShowVideo(this.device[i].video_url)
          })
        }
      })
    this.GetMessages()
    this.GetMessageInfo()
  },
  methods: {
    /**
     * @return {string}
     */
    MessageFormat (percentage) {
      return percentage === 0 ? '无' : `${percentage}%`
    },
    ShowVideo (videoUrl) {
      this.drawer = true
      this.videoOnShow = videoUrl
    },
    InitVideo () {
      var myPlayer = document.getElementById('myPlayer')
      var source = document.createElement('source')
      var drawBody = document.getElementsByClassName('el-drawer__body')[0]
      source.setAttribute('src', this.videoOnShow)
      myPlayer.appendChild(source)

      let thePlayer = new EZUIKit.EZUIPlayer('myPlayer')
      console.log('im here')
      thePlayer.play()
      console.log(thePlayer)
      console.log(this.$refs.videoDrawer)
      thePlayer.opt.height = drawBody.clientHeight
      thePlayer.opt.width = drawBody.clientWidth
    },
    GetMessageInfo () {
      this.$axios.get(this.urlHead + '/api/messages/info/')
        .then((e) => {
          if (e.data.code === 0) {
            this.messageAmount = e.data.data.total
            this.messageUnread = e.data.data.unread
          } else {
            this.$notify({
              message: e.data.msg,
              type: 'warning'
            })
          }
        })
        .catch((e) => {
          console.log(e)
          this.$notify({
            message: '获取报警信息详情失败',
            type: 'warning'
          })
        })
    },
    GetMessages () {
      this.$axios.get(this.urlHead + '/api/messages/?limit=10&type=all')
        .then((e) => {
          console.log(e.data)
          if (e.data.code === 0) {
            this.messages = e.data.data
          } else {
            this.$notify({
              message: e.data.msg,
              type: 'warning'
            })
          }
        })
        .catch((e) => {
          console.log(e)
          this.$notify({
            message: '无法获取报警信息',
            type: 'warning'
          })
        })
    },
    HandleChange (currentIndex, lastIndex) {
      this.$refs.imgCarousel.setActiveItem(currentIndex)
      this.$refs.messageCarousel.setActiveItem(currentIndex)
    }
  },
  computed: {
    devicePercentage: function () {
      return this.deviceAmount === 0 ? 0 : Math.ceil(this.deviceOnline * 100 / this.deviceAmount)
    },
    messagePercentage: function () {
      return this.messageAmount === 0 ? 0 : Math.ceil(this.messageUnread * 100 / this.messageAmount)
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
  background-color: rgba(255, 255, 255, .6);
  border: 0;
  min-height: 300px;
}
.el-card {
  display: grid;
}
.el-card span {
  margin: 5px;
}
.el-card__body {
  align-self: stretch;
  max-height: 100%;
}
.el-card__body div{
  height: 100%;
  width: 100%;
}
.overview-message-card .el-carousel .is-active{
  background: rgba(249, 246, 142, 0.82);
}
.el-carousel__item {
  margin-top: 5px;
}
@media screen and (max-width: 1200px) {
  .overview-main {
    position: relative;
    top: 0;
    grid-template-columns: repeat(3,1fr);
    grid-template-rows: repeat(3,1fr);
    grid-template-areas:
      "message img voltage"
      "map map map"
      "amount wheather install";
    overflow-y: auto;
  }
  .overview-main .el-card {
    height: 50vh;
  }
}
@media screen and (max-width: 1000px) {
  .overview-main {
    position: relative;
    top: 0;
    grid-template-columns: repeat(2,1fr);
    grid-template-rows: repeat(4,1fr);
    grid-template-areas:
      "message img"
      "map map"
      "voltage install"
      "amount wheather";
  }
}
@media screen and (max-width: 768px) {
  .overview-main {
    position: relative;
    top: 0;
    grid-template-columns: repeat(1,1fr);
    grid-template-rows: repeat(7,1fr);
    grid-template-areas:
      "message"
      "img"
      "map"
      "voltage"
      "install"
      "amount"
      "wheather";
  }
}
</style>
