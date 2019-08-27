<template>
<div class="warning-main">
<el-card class="warning-table-container" body-style="{height:'80%'}" v-loading.fullscreen.lock="isLoading">
  <el-table
    :data="messageDisplayed"
    ref="multipleTable"
    style="width: 100%; height: 100%;"
    max-height="95%"
    :cell-style="cellStyle"
    @cell-click="handleCellClick"
    @selection-change="handleSelectionChange"
    >
    <el-table-column type="selection" width="55"></el-table-column>
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
  <el-row>
    <el-col align="middle">
      <el-pagination
        background
        layout="prev, pager, next"
        v-bind:current-page="currentPage"
        :total="filterMessage.length"
        :page-size="messagePerPage"
        @current-change="handleCurrentChange"
        @prev-click="handleCurrentChange"
        @next-click="handleCurrentChange"
        ></el-pagination>
    </el-col>
    <el-col align="right">
      <el-button
        type="success"
        :disabled="messagesSelected.length === 0"
        @click="handleProve(true)"
      >
        预警正确
      </el-button>
      <el-button
        type="danger"
        :disabled="messagesSelected.length === 0"
        @click="handleProve(false)"
      >
        预警错误
      </el-button>
    </el-col>
  </el-row>
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
      messages: [],
      messagesSelected: [],
      devices: [],
      dateRange: '',
      selectDeviceId: '',
      approvalStatus: '',
      cellStyle: {
        justifyItems: 'center'
      },
      isLoading: true
    }
  },
  methods: {
    handleCurrentChange (currentChange) {
      console.log('This is current change')
      this.currentPage = currentChange
    },
    handleSelectionChange (selections) {
      this.messagesSelected = selections
    },
    handleCellClick (row) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    handleProve (status) {
      let messageIds = []
      for (let i = 0; i < this.messagesSelected.length; i++) {
        messageIds.push(this.messagesSelected[i].id)
      }
      this.$axios.post(this.urlHead + '/api/messages/approve',
        {
          'params': {
            'message_ids': messageIds,
            'approve_status': status
          }
        })
        .then((e) => {
          if (e.data.code === 0) {
            this.$notify({
              message: '审核成功',
              type: 'success'
            })
            this.messagesSelected.forEach(message => {
              message.deal = true
            })
          } else {
            this.$notify({
              message: '审核失败' + e.data.msg,
              type: 'danger'
            })
          }
        })
        .catch(() => {
          this.$notify({
            message: '请求错误',
            type: 'danger'
          })
        })
    }
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
  },
  mounted () {
    this.$axios.get(this.urlHead + '/api/messages/')
      .then((e) => {
        this.isLoading = false
        this.messages = e.data.data
      })
      .catch((e) => {
        this.isLoading = false
        this.$notify({
          message: '获取数据失败: \n ' + e.data.msg,
          type: 'danger'
        })
      })
    this.$axios.get(this.urlHead + '/api/devices/all')
      .then((e) => {
        this.isLoading = false
        this.devices = e.data.data
      })
      .catch((e) => {
        this.isLoading = false
        this.$notify({
          message: '获取设备列表失败 \n ' + e.data.msg,
          type: 'danger'
        })
      })
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
