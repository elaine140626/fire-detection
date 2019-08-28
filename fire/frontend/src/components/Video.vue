<template>
  <video
    controls
    playsInline
    webkit-playsinline
    autoplay
    :key="video.id"
    :id="'myPlayer' + video.id"
  >
    <source :src="video.video_url">
  </video>
</template>

<script>
import EZUIKit from '../../libs/ezuikit.js'
export default {
  name: 'RtmpPlayer',
  props: {
    video: {
      id: '',
      video_url: ''
    },
    height: {
      type: Number,
      default: 300
    },
    width: {
      type: Number,
      default: 300
    }
  },
  data () {
    return {
      thePlayer: undefined
    }
  },
  mounted () {
    let thePlayer = new EZUIKit.EZUIPlayer('myPlayer' + this.video.id)
    thePlayer.play()
    thePlayer.opt.height = this.height
    thePlayer.opt.width = this.width
  },
  watch: {
    height: {
      immediate: true,
      handler () {
        let embed = document.getElementById('myPlayer' + this.video.id).firstChild.lastChild
        embed.height = this.height
      }
    },
    width: {
      immediate: true,
      handler () {
        let embed = document.getElementById('myPlayer' + this.video.id).firstChild.lastChild
        embed.width = this.width
      }
    }
  }
}
</script>

<style scoped>

</style>
