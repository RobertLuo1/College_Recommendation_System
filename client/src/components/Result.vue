<template>
  <div>
    <div class="box">
      <el-container style="border-radius: 10px; border: 2px solid #eee">
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
          <el-header style="text-align: center; background-color: #dcdde2;">
            <span style="text-align: right; font-size: 18px; ">
              <i class="el-icon-menu" style="margin-left:5px"></i>学校
            </span>
          </el-header>
          <el-menu active-text-color='#000000' style="height: 480px;">
            <el-menu-item v-for="item in options" :key="item" :index="item" @click="getCol(item)">
              <template slot="title" :content="item"><i class="el-icon-s-flag"  style="color: #000000;"></i>{{item}}</template>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-container>
          <el-header style="text-align: right; font-size: 12px">
            <el-radio-group v-model="radio" @change="labelchanged(radio)">
              <el-radio label="985">985</el-radio>
              <el-radio label="211">211</el-radio>
              <el-radio label="双一流">双一流</el-radio>
              <el-radio label="全部">全部</el-radio>
            </el-radio-group>
          </el-header>
          <el-main>
            <el-table :data="tableData[selectCol]" border stripe style="width: 600px; padding: 0;" max-height="480px">
              <el-table-column prop="major" label="专业" width="220">
              </el-table-column>
              <el-table-column prop="rank" label="预测排名" width="150">
              </el-table-column>
              <el-table-column prop="possibility" label="推荐指数" width="220">
                <template slot-scope="{row}">
                  <el-rate
                    v-model="row.possibility"
                    disabled
                    show-score
                    text-color="#ffd965"
                    :colors="colors"
                    score-template="{value}">
                  </el-rate>
                </template>
              </el-table-column>
            </el-table>
          </el-main>
        </el-container>
      </el-container>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    const opts = this.$store.state.res.colleges
    return {
      activeName: 'first',
      tableData: this.$store.state.res.col_majors,
      options: opts,
      oldoptions: opts,
      selectCol: opts[0],
      radio: '全部',
      currentIndex: opts[0],
      colors: ['#99A9BF', '#F7BA2A', '#FF9900']
    }
  },
  methods: {
    getCol (item) {
      this.selectCol = item
    },
    async labelchanged (radio) {
      const datapac = {
        flag: radio,
        colleges: this.oldoptions
      }
      const { data: res } = await this.$http.post('/result', datapac)
      console.log(res)
      if (res.status_code === 200) {
        this.options = res.colleges
        this.selectCol = this.options[0]
        this.currentIndex = this.options[0]
      }
    }
  }
}
</script>

<style>
  .el-header {
      background-color: #cad9eb;
      color: #333;
      line-height: 60px;
      filter: alpha(opacity=50);
      opacity: 0.9;
    }
    .el-aside {
      color: #333;
    }
    .el-container {
      background-color: #e8e8e8;
      filter: alpha(opacity=50);
      opacity: 0.95;
    }
    .box {
      position: absolute;
      left: 50%;
      top: 20%;
      transform: translate(-50%, -10%);
    }
</style>
