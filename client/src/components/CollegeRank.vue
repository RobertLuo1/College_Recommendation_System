<template>
  <div>
    <el-carousel indicator-position="none" :interval="3000" height="1100px" style="width: 550px; left: 50%; transform: translate(-50%, 0);">
      <el-carousel-item v-for="item in images" :key="item.id">
        <img :src="item.img_url"/>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeName: 'third',
      images: []
    }
  },
  methods: {
    get_imgs () {
      const that = this
      this.$http.get('/collegeRank').then(result => {
        that.images = result.data.collegeRank
      }, result => {
        console.log('Failed')
      })
    }
  },
  created () {
    this.get_imgs()
  }
}
</script>

<style>
</style>
