<template>
    <div style="height: 100%; width: 100%;">
      <el-row style="height: 100%;">
        <el-col :span="4">
          <el-table
            :data="videos"
            ref="multipleTable"
            style="width: 100%; height: 100%;"
            max-height="95%"
            @selection-change="handleSelectionChange"
            @cell-click="handleCellClick"
          >
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column label="视频" header-align="center">
              <template slot-scope="scope">
                视频 {{scope.row.id}}
              </template>
            </el-table-column>
          </el-table>
        </el-col>
        <el-col :span="20" style="height: 100%;">
          <div style="height: 100%; margin-left: 5px" id="videoContainer">
            <div style="padding: 7px;
            background: #ffffff; -webkit-border-radius: 3px;-moz-border-radius: 3px;
            border-radius: 3px;
            display: grid; grid-template-columns: 1fr 1fr;"
            >
              <div style="display: flex; align-items: center; justify-content: flex-start; padding-left: 4px">iLearn</div>
              <div style="display: flex; align-items: center; justify-content: flex-end">
                <div>
                  <el-button @click="switchLayout(1)">1xN</el-button>
                  <el-button @click="switchLayout(2)">2xN</el-button>
                  <el-button @click="switchLayout(4)">4xN</el-button>
                  <el-button @click="switchLayout(6)">6xN</el-button>
                </div>
              </div>
            </div>
            <div :class="'grid-' + this.layout" id="theVideos" style="background: rgba(255,255,255,.6); -webkit-border-radius: 3px;-moz-border-radius: 3px;border-radius: 3px; padding: 10px 5px; min-height: 70%;">
              <rtmp-player
                v-for="video in videosOnShow"
                :key="video.id"
                :video="video"
                :width="width"
                :height="width"
              >
              </rtmp-player>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
</template>

<script>
import RtmpPlayer from './Video'
export default {
  name: 'Monitor',
  components: {RtmpPlayer},
  data () {
    return {
      videos: [],
      videosOnShow: [],
      layout: 2,
      padding: 10
    }
  },
  methods: {
    handleCellClick (row) {
      this.$refs.multipleTable.toggleRowSelection(row)
      this.switchPlayerStatus()
    },
    handleSelectionChange (selections) {
      this.videosOnShow = selections
      this.switchPlayerStatus()
    },
    switchPlayerStatus () {
      let theVideos = document.getElementById('theVideos')
      for (let i = 0; i < this.videos.length; i++) {
        this.videos[i].onShow = false
      }
      for (let i = 0; i < this.videosOnShow.length; i++) {
        this.videosOnShow[i].onShow = true
      }
      for (let i = 0; i < this.videos.length; i++) {
        if (this.videos[i].onShow) {
          theVideos.children[i].style.display = 'block'
        } else {
          theVideos.children[i].style.display = 'none'
        }
      }
    },
    switchLayout (newLayout) {
      this.layout = newLayout
    }
  },
  mounted () {
    this.$axios.get(this.urlHead + '/api/videos/')
      .then((e) => {
        this.videos = e.data.data
        this.videosOnShow = this.videos
        this.$refs.multipleTable.toggleAllSelection()
      })
      .catch((e) => {
        this.$notify({
          message: '请求错误' + e,
          type: 'danger'
        })
      })
  },
  computed: {
    width () {
      let videoContainer = document.getElementById('videoContainer')
      return videoContainer.clientWidth / this.layout - this.layout * this.padding
    }
  }
}
</script>

<style scoped>
.el-col {
  max-height: 100%;
}
.el-card {
  justify-items: center;
}
.el-table {
  background: rgba(255, 255, 255, .7);
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-row-gap: 10px;
}
.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-row-gap: 10px;
}
.grid-6 {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-row-gap: 10px;
}
.display-none {
  display: none;
}
</style>
