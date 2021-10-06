<template>
  <div id="app">
    <el-tabs v-model="activeName" @tab-click="handelclick" class="tabs">
      <!-- <el-tab-pane label="首页" name="homepage"></el-tab-pane> -->
      <el-tab-pane label="志愿查询" name="first"></el-tab-pane>
      <el-tab-pane label="热门职业" name="second"></el-tab-pane>
      <el-tab-pane label="大学排名" name="third"></el-tab-pane>
      <el-tab-pane label="关于我们" name="aboutUs"></el-tab-pane>
    </el-tabs>
    <!-- 路由占位符 -->
    <router-view></router-view>
  </div>
</template>

<script>
import { TimelineLite } from 'gsap'
export default {
  name: 'app',
  data () {
        return {
            activeName: this.$store.state.activename
        }
    },
  watch: {
      $route (to, from) {
        const r = document.getElementById('app')
        const timeline = new TimelineLite()
        timeline.from(r, 0.3, {
          autoAlpha: 0,
          opacity: 0,
          scale: 0.5,
          transformOrigin: 'center center'
        })
        timeline.to(r, 0.3, {
          autoAlpha: 1,
          opacity: 1,
          scale: 1,
          transformOrigin: 'center center'
        })
      }
    },
    methods: {
      handelclick (tab, event) {
        console.log(tab)
        if (tab.name === 'first') {
          this.$router.push('/query')
          this.$store.state.activename = 'first'
        } else if (tab.name === 'second') {
          this.$router.push('/Jobs')
          this.$store.state.activename = 'second'
        } else if (tab.name === 'third') {
          this.$router.push('/collegeRank')
          this.$store.state.activename = 'third'
        } else if (tab.name === 'aboutUs') {
          this.$router.push('/aboutus')
          this.$store.state.activename = 'aboutUs'
        } else if (tab.name === 'homepage') {
          this.$router.push('/homepage')
          this.$store.state.activename = 'homepage'
        }
      }
    }
}
</script>

<style scoped>
  .el-tabs {
    background-image: linear-gradient(to top, #d5d4d0 0%, #d5d4d0 1%, #eeeeec 31%, #efeeec 75%, #e9e9e7 100%) !important;
  }
</style>
