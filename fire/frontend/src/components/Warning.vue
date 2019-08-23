<template>
<div class="warning-main">
<el-card class="warning-table-container" body-style="{height:'80%'}">
  <el-table
    :data="messageDisplayed"
    style="width: 100%; height: 100%;"
    max-height="95%"
    :cell-style="cellStyle"
    >
    <el-table-column prop="c_time" align="center" header-align="center" width="370">
      <template slot="header" slot-scope="scope">
        <el-date-picker
          v-model="dateRange"
          type="daterange"
          unlink-panels
          value-format="yyyy-MM-dd"
          range-separator="至"
          start-placeholder="开始时间"
          end-placeholder="结束时间">
        </el-date-picker>
      </template>
    </el-table-column>
    <el-table-column
      prop="content"
      label="预警详情"
      header-align="center"
      align="center"
    ></el-table-column>
    <el-table-column prop="device_number" align="center" header-align="center">
      <template slot="header" slot-scope="scope">
        <el-select v-model="selectDeviceId" placeholder="设备ID" :clearable="true">
          <el-option
            v-for="device in devices"
            :key="device.id"
            :label="device.id"
            :value="device.id"></el-option>
        </el-select>
      </template>
    </el-table-column>
    <el-table-column prop="device_hint" label="设备标识" align="center" header-align="center"></el-table-column>
    <el-table-column align="center" header-align="center">
      <template slot="header" slot-scope="scope">
        <el-select v-model="approvalStatus" placeholder="审核状态" :clearable="true">
          <el-option label="已审核" :value="true"></el-option>
          <el-option label="未审核" :value="false"></el-option>
        </el-select>
      </template>
      <template slot-scope="scope" style="align-items: center;">
        <el-tag v-if="scope.row.deal" type="success">已审核</el-tag>
        <el-tag v-else type="danger">未审核</el-tag>
      </template>
    </el-table-column>
    <el-table-column label="告警图片" align="center" header-aligh="center">
      <template slot-scope="scope">
        <el-image :src="scope.row.img_url" >
        </el-image>
      </template>
    </el-table-column>
  </el-table>
</el-card>
</div>
</template>

<script>
export default {
  name: 'Warning',
  data () {
    return {
      currentPage: 1,
      messagePerPage: 10,
      messages: [{'id': 1, 'content': '这是一条告警信息', 'img_url': 'http://a.hiphotos.baidu.com/image/h%3D300/sign=a62e824376d98d1069d40a31113eb807/838ba61ea8d3fd1fc9c7b6853a4e251f94ca5f46.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': true, 'c_time': '2019-06-26'}, {'id': 2, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428914.6071951.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 3, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428915.6183162.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 4, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428921.801521.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': true, 'c_time': '2019-06-26'}, {'id': 5, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428922.8135169.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': true, 'c_time': '2019-06-26'}, {'id': 6, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 7, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428923.8265727.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 8, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428924.8973463.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 9, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428925.974638.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}, {'id': 10, 'content': '这是一条告警信息', 'img_url': 'http://188.131.241.21/static/untrack/1558428928.0553596.jpg', 'device_number': 1, 'device_hint': 'n3', 'deal': false, 'c_time': '2019-06-26'}],
      devices: [{'id': 1, 'serial_number': 'C02411653', 'location_x': 120.697792, 'location_y': 36.369133, 'hint': 'n3', 'video_url': 'rtmp://rtmp01open.ys7.com/openlive/f01018a141094b7fa138b9d0b856507b'}],
      dateRange: '',
      selectDeviceId: '',
      approvalStatus: '',
      cellStyle: {
        justifyItems: 'center'
      }
    }
  },
  method: {
  },
  computed: {
    filterMessage () {
      let ret = []
      this.messages.forEach(message => {
        console.log(this.dateRange)
        if (this.dateRange && (this.dateRange[0] > message.c_time || message.c_time > this.dateRange[1])) return
        if (this.selectDeviceId && this.selectDeviceId !== message.device_number) return
        if (this.approvalStatus && this.approvalStatus !== message.deal) return
        ret.push(message)
      })
      return ret
    },
    messageDisplayed () {
      return this.filterMessage.slice((this.currentPage - 1) * this.messagePerPage, this.currentPage *
        this.messagePerPage)
    },
    pageNumber () {
      return Math.ceil(this.filterMessage.length / this.messagePerPage)
    }
  }
}
</script>

<style scoped>
.el-card {
  max-height: 100%;
  background-color: rgba(255,255,255,.6);
  border: 0;
}
.warning-main {
  max-height: 100%;
  width: 100%;
  align-self: baseline;
}
.warning-table-container {
  height: 100%;
  width: 100%;
}
td .cell {
  display: flex;
  justify-items: center;
}
</style>
