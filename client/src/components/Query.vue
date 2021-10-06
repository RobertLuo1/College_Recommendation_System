<template>
  <div>
    <div class="login_container">
      <!-- <div class="mytitle">高考志愿填报系统</div> -->
      <div class="login_box">
        <!-- 头像区 -->
        <div class="avatar_box">
          <img src="../assets/logo2.webp"/>
        </div>
        <el-steps :active="activeNum" finish-status="success" simple style="margin-top: 60px; height: 10px;">
          <el-step title="类别"></el-step>
          <el-step title="排名" ></el-step>
          <el-step title="省份" ></el-step>
        </el-steps>
        <!-- 查询表单区域 -->
        <el-form ref="queryFormRef" :rules="queryFormRules" :model="queryform" class="login_form" label-width="40px" style="position: relative; top:7%;">
          <!-- 文理科 -->
          <el-form-item label="类别">
            <el-select v-model="queryform.category" filterable placeholder="请选择您的类别" collapse-tags @change="getactivenum0">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <!-- 省份排名 -->
          <el-form-item label="排名">
            <el-input prefix-icon="iconfont el-icon-zypaiming" v-model="queryform.rank" placeholder="请输入排名" @change="getactivenum1"></el-input>
          </el-form-item>
          <!-- 地区偏好 -->
          <el-form-item label="省份">
            <el-input id="regions" prefix-icon="iconfont el-icon-zywxbdingwei" :placeholder="$store.getters.provincesGet" disabled style="width: 50%;" @change="getactivenum2"></el-input>
            <el-button @click="map" type="warning" size="small" style="margin: 0 10px;">地图</el-button>
            <el-button @click="queryCollege" type="warning" size="mini" style="margin: 0 0px;">查询大学</el-button>
            <el-button @click="All" type="success" size="mini" style="margin: 10 10px;">全国</el-button>
          </el-form-item>
          <!-- 查询按钮 -->
          <el-form-item class="btns">
            <el-button type="primary" @click="query">查询</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted () {
      this.$store.state.activename = 'first'
  },
  data () {
    return {
      activeNum: this.$store.state.activenum,
      activeName: 'first',
      // 查询表单中的数据绑定对象
      queryform: {
        rank: this.$store.state.rank,
        regions: this.$store.state.provinces,
        category: this.$store.state.category,
        currentLocation: {
          lng: 120.27,
          lat: 32.59,
          pos: '江苏省'
        },
        all: this.$store.state.all
      },
      // 查询表单验证规则对象
      queryFormRules: {
        // 查询排名规则
        rank: [
          { required: true, message: '请输入排名!', trigger: 'blur' }
        ],
        regions: [
          { required: true, message: '请选择地区!', trigger: 'blur' }
        ]
      },
      options: [{
        value: '文科',
        label: '文科'
      }, {
        value: '理科',
        label: '理科'
      }]
    }
  },
  methods: {
    getactivenum0 () {
      this.activeNum = 1
      this.$store.state.activenum = 1
    },
    getactivenum1 () {
      this.activeNum = 2
      this.$store.state.activenum = 2
    },
    getactivenum2 () {
      this.activeNum = 2
      this.$store.state.activenum = 2
    },
    query () {
      this.$refs.queryFormRef.validate(async valid => {
        if (!valid) return
        console.log(this.queryform)
        const { data: res } = await this.$http.post('/query', JSON.stringify(this.queryform))
        console.log(res)
        // 查询成功，跳转页面
        if (res.status_code === 200) {
          this.$store.state.res = res
          this.$message({
            type: 'success',
            message: '查询成功'
          })
          this.$router.push('/result')
        } else if (res.status_code === 500) {
          this.$message({
            type: 'warning',
            message: '查询失败,请输入正确的数据'
          })
        }
      })
    },
    map () {
      this.$store.state.rank = this.$data.queryform.rank
      this.$store.state.category = this.$data.queryform.category
      this.$router.push('/mymap')
    },
    queryCollege () {
      this.$store.state.rank = this.$data.queryform.rank
      this.$store.state.category = this.$data.queryform.category
      this.$router.push('/queryCollege')
    },
    All () {
      this.$store.state.all = 'true'
      this.$data.queryform.all = 'true'
      const re = document.getElementById('regions')
      re.placeholder = '全国'
    }
  }
}
</script>

<style lang="less" scoped>
  .mytitle{
    width: 100%;
    padding: 15px 0;
    font-size: 40px;
    font-family:"宋体";
    text-align: center;
    font-weight:normal;
    color: #91c89a;
  }
  .login_container{
    height: 100%;
  }
  .login_box{
    width: 600px;
    height: 370px;
    filter: alpha(opacity=50);
    opacity: 0.9;
    border-radius: 20px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -40%);
    box-shadow: 0 15px 20px rgba(0,0,0,.2);
    background-color:#a3c3d1;
    background-image:
    radial-gradient(white, rgba(255, 255, 255, 0.22) 3px, transparent 40px),
    radial-gradient(white, rgba(255,255,255,.20) 4px, transparent 30px),
    radial-gradient(white, rgba(255,255,255,.15) 5px, transparent 40px),
    radial-gradient(white, rgba(255,255,255,.25) 3px, transparent 30px);
    background-size: 550px 550px, 350px 350px, 250px 250px, 150px 150px;
    background-position: 0 0, 40px 60px, 130px 270px, 70px 100px;
  }
  .avatar_box{
    height: 100px;
    width: 100px;
    border: solid 1px #eee;
    border-radius: 50%;
    padding: 2px;
    box-shadow: 0 0 6px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #dde;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
  .login_form {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 10px;
    box-sizing: border-box;
  }
  .btns {
    display: flex;
    justify-content: flex-end;
  }
  .tabs {
    background-color: #eeeeee;
    padding: 0 20px;
    height: 40px;
    box-sizing: border-box;
    line-height: 40px;
    list-style: none;
    font-size: 15px;
    font-weight: 500;
    position: relative;
  }
</style>
