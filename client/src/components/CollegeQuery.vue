<template>
  <div>
    <div class="home">
      <div class="map" id="map"></div>
    </div>
    <el-button @click="retQuery" type="warning" style="position:absolute; left: 100%;transform: translate(-120%, 50%); padding: 10px;">返回</el-button>
  </div>
</template>
<script>
import BMap from 'BMap'
export default {
  name: 'Home',
  data () {
    return {
      map: Object,
      mapVisible: false,
      iconUrl: 'http://api0.map.bdimg.com/images/marker_red_sprite.png'
    }
  },
  mounted () {
    const _this = this
    this.$nextTick(() => {
      _this.initMap()
    })
  },
  methods: {
    // 初始化地图
    initMap: function () {
      this.map = new BMap.Map('map', { minZoom: 5, maxZoom: 25 })
      this.map.centerAndZoom(new BMap.Point(114.311754, 30), 5)
      this.map.enableScrollWheelZoom(true)
      const map = this.map
      const that = this
      this.map.addEventListener('click', async function (e) {
        map.clearOverlays()
        const icon0 = new BMap.Icon('http://api0.map.bdimg.com/images/marker_red_sprite.png', new BMap.Size(64, 64), { anchor: new BMap.Size(18, 32), imageSize: new BMap.Size(36, 25) })
        const myMarker = new BMap.Marker(new BMap.Point(e.point.lng, e.point.lat), { icon: icon0 })
        map.addOverlay(myMarker)
        const point = new BMap.Point(e.point.lng, e.point.lat)
        const gc = new BMap.Geocoder()
        let pro = ''
        const d = { region: '' }
        gc.getLocation(point, function (rs) {
          const addComp = rs.addressComponents
          pro = addComp.province
          d.region = pro
        })
        setTimeout(async () => {
          console.log(d.region)
          const { data: res } = await that.$http.post('/queryCollege', JSON.stringify(d))
          const college = res.content
          let cols = ''
          for (let j = 0; j < college.length; j++) {
            cols += college[j] + '\t'
          }
          console.log(cols)
          that.$alert(cols, '查询结果', {
            confirmButtonText: '确定',
            callback: action => {
              that.$message({
                type: 'info',
                message: '查询结束'
              })
            }
          })
        }, 100)
      })
    },
    retQuery () {
      this.$router.push('/query')
    }
  }
}

</script>
<style scoped>
.home{
  height: 80%;
  width: 80%;
  border-radius: 20px;
  position: absolute;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -30%);
}
.map {
  height: 100%;
  width: 100%;
}
.el-tag + .el-tag {
  margin-left: 10px;
}
.regions {
  margin: 20px;
  height: 100px;
  width: 80%;
  position: absolute;
  left: 50%;
  top: 10%;
  transform: translate(-50%, -70%);
}
</style>
