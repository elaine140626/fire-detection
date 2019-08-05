<template>
  <div id="app">
    <el-container style="height: 100%;">
      <el-header>
        <base-header></base-header>
      </el-header>
      <el-main style="display: flex;justify-content: center;align-items: center;">
          <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import BaseHeader from '@/components/BaseHeader'
export default {
  name: 'App',
  components: {
    BaseHeader
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
}
#app {
  height: 100vh;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url("../../static/img/altitude-clouds-cold-933054-small.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
</style>
