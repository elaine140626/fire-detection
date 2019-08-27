<template>
    <div style="height: 100%; width: 100%;">
      <el-row>
        <el-col :span="4">
          <video id="myPlayer" ref='video' controls playsinline webkit-playsinline autoplay height="300" width="300"
                 src="rtmp://rtmp01open.ys7.com/openlive/dcc39c775b5945028a69b4b6953f4369">
          </video>
        </el-col>
        <el-col :span="20">
          2
        </el-col>
      </el-row>
    </div>
</template>

<script>
import EZUIKit from '../../libs/ezuikit.js'
export default {
  name: 'Monitor',
  data () {
    return {
      videos: []
    }
  },
  mounted () {
    let player = new EZUIKit.EZUIPlayer('myPlayer')
    console.log(player)
  }
}
</script>

<style scoped>
.el-col {
  max-height: 100%;
}
</style>
