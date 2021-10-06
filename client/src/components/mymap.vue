<template>
  <div>
    <div class="home">
      <div class="map" id="map"></div>
    </div>
    <div class="regions">
      <el-tag
      v-for="item in address"
      :key="item.pos"
      closable
      :disavle-transitions="false"
      @close="handleClose(item)"
      type="danger">{{item.pos}}</el-tag>
    </div>
    <el-button @click="submitAddress()" type="primary" style="position:absolute; left: 100%;transform: translate(-120%, 50%); padding: 10px;">提交</el-button>
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
      address: [],
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
      this.map.addEventListener('click', function (e) {
        map.clearOverlays()
        const icon0 = new BMap.Icon('http://api0.map.bdimg.com/images/marker_red_sprite.png', new BMap.Size(64, 64), { anchor: new BMap.Size(18, 32), imageSize: new BMap.Size(36, 25) })
        const myMarker = new BMap.Marker(new BMap.Point(e.point.lng, e.point.lat), { icon: icon0 })
        map.addOverlay(myMarker)
        const point = new BMap.Point(e.point.lng, e.point.lat)
        const gc = new BMap.Geocoder()
        gc.getLocation(point, function (rs) {
          const addComp = rs.addressComponents
          console.log(addComp.province)
          let ifexist = 0
          for (let j = 0; j < that.address.length; j++) {
            if (that.address[j].pos === addComp.province) {
              ifexist = 1
            }
          }
          if (!ifexist) {
            const locData = {
              lng: '',
              lat: '',
              pos: ''
            }
            locData.lng = e.point.lng
            locData.lat = e.point.lat
            locData.pos = addComp.province
            that.address.push(locData)
          }
        })
      })
    },
    handleClose (item) {
      this.address.splice(this.address.indexOf(item), 1)
    },
    submitAddress () {
      this.$confirm('即将提交, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$store.commit('setProvinces', this.address)
          // console.log(this.$store.state.provinces)
          this.$message({
          type: 'success',
          message: '提交成功!'
          })
          this.$router.push('/query')
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消提交'
          })
        })
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
  top: 20%;
  transform: translate(-50%, -70%);
}
</style>
