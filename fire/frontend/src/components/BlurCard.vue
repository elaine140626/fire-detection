<template>
  <el-card v-bind:style="{ background: 'rgba(255, 255, 255, ' + oo+')' , padding: thePadding }">
    <slot>
    </slot>
  </el-card>
</template>

<script>
export default {
  name: 'BlurCard',
  props: {
    oo: 0.3,
    thePadding: 0
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.el-card {
  border: 0;
}
</style>
