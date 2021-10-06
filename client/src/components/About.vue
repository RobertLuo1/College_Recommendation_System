<template>
  <div>
    <el-row  type="flex" justify="space-around">
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }" style="background-image: linear-gradient(to top, #feada6 0%, #f5efef 100%);">
              <img src="../assets/lw.png" class="image">
              <div style="padding: 14px;">
                <span>一个平平无奇的小fw。</span>
                <el-divider content-position="right">李伟</el-divider>
              </div>
            </el-card>
      </el-col>
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }" style="background-image: linear-gradient(to top, #accbee 0%, #e7f0fd 100%);">
              <img src="../assets/zh.png" class="image">
              <div style="padding: 14px;">
                <span>我是没有假期、不想上课的哭哭肥仔晗</span>
                <el-divider content-position="right">肥仔晗</el-divider>
              </div>
            </el-card>
      </el-col>
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }" style="background-image: linear-gradient(to top, #c79081 0%, #dfa579 100%);">
              <img src="../assets/lby.jpg" class="image">
              <div style="padding: 14px;">
                <span>世界上最快乐的事，莫过于为理想而奋斗。</span>
                <el-divider content-position="right">刘博洋</el-divider>
              </div>
            </el-card>
      </el-col>
      </el-row>
      <el-row  type="flex" justify="space-around">
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }" class="mycl">
              <img src="../assets/lzy.png" class="image">
              <div style="padding: 14px;">
                <span>Diligence Makes Perfect.</span>
                <el-divider content-position="right">罗卓彦</el-divider>
              </div>
            </el-card>
      </el-col>
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }" style="background-image: linear-gradient(to top, #007adf 0%, #00ecbc 100%);">
              <img src="../assets/wzy.jpg" class="image">
              <div style="padding: 14px;">
                <span>最好的政策就是没有政策。</span>
                <el-divider content-position="right">王兆阳</el-divider>
              </div>
            </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
  .mycl {
    /* position: ab solute;
    left: 50%;
    top: 50%; */
    /* transform: translate(-50%, -50%); */
    background-image: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
  }
  .image {
    width: 400px;
  }
  .el-card {
    margin: 10px;
    margin-bottom: 40px;
    height: 400px;
    transition: all .5s;
    box-shadow: 10px 10px 5px #000000 !important;
  }
  .el-card:hover {
    width: 95%;
    /* height: 220px; */
    margin-top: -5px;
    box-shadow: 1px 1px 0.5px #000000 !important;
  }
</style>
