<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>{{jobsShow}}</span>
        <el-button style="float: right; padding: 3px 0" type="text" @click="change">切换</el-button>
      </div>
      <el-collapse v-model="activeJob" accordion>
        <el-collapse-item v-for="job in Jobs[jobsShow]" :key="job.大职业" :title="job.大职业" :name="job.大职业">
          <div v-for="(subjob,index) in job.subjobs" :key=index>
            {{subjob.子职业}} -------------------------------- {{subjob.薪资}}
          </div>
        </el-collapse-item>
      </el-collapse>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeName: 'second',
      jobsShow: '热门职业',
      activeJob: 'a',
      Jobs: {}
    }
  },
  methods: {
    change () {
      if (this.jobsShow === '热门职业') {
        this.jobsShow = '稀缺职业'
      } else {
        this.jobsShow = '热门职业'
      }
    },
    getJobs () {
      const that = this
      this.$http.get('/Jobs').then(result => {
        that.Jobs = result.data.Jobs
        console.log(result.data)
      }, result => {
        console.log('Failed')
      })
    }
  },
  created () {
    this.getJobs()
  }
}
</script>

<style>
    .text {
      font-size: 14px;
    }
    .item {
      margin-bottom: 18px;
    }
    .clearfix:before,
    .clearfix:after {
      display: table;
      content: "";
    }
    .clearfix:after {
      clear: both
    }
    .box-card {
      width: 600px;
      position: absolute;
      top: 30%;
      left: 50%;
      transform: translate(-50%, -15%);
      box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
      filter: alpha(opacity=50);
      opacity: 0.9;
    }
</style>
