<template>
  <div>
    <el-carousel :interval="4000" type="card" height="300px">
      <el-carousel-item>
        <img style="width: 100%;" src="../assets/1.jpg"/>
      </el-carousel-item>
      <el-carousel-item>
        <img style="width: 100%;" src="../assets/2.jpg"/>
      </el-carousel-item>
      <el-carousel-item>
        <img style="width: 100%;" src="../assets/3.jpg"/>
      </el-carousel-item>
      <el-carousel-item>
        <img style="width: 100%;" src="../assets/4.jpg"/>
      </el-carousel-item>
    </el-carousel>
    <div class="m-header">
      <div class="box_left">
        <span class="left_top"></span>
        <span class="left_bottom"></span>
      </div>
      <div class="icon"></div>
      <h1 class="text">越来越好</h1>
      <div class="box_right">
              <span class="right_top"></span>
              <span class="right_bottom"></span>
          </div>
    </div>
    <el-row  type="flex" justify="space-around">
      <el-col :span="6">
        <el-card class="mycard1" shadow="hover">
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="mycard2" shadow="hover">
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="mycard5" shadow="hover">
        </el-card>
      </el-col>
    </el-row>
    <div class="btn">
    <div class="button" @click="btnclick">
      <p>开始志愿查询</p>
    </div>
    </div>
  </div>
</template>

<script>
import { TweenMax, Expo, Back, TimelineLite } from 'gsap'
export default {
  data () {
    return {
      activeName: 'homepage'
      // value: new Date()
    }
  },
  mounted () {
    const c1 = document.getElementsByClassName('el-card')
    const timeline = new TimelineLite()
    timeline.from(c1, 0.3, {
      autoAlpha: 0,
      opacity: 0,
      scale: 0,
      transformOrigin: 'center center',
      stagger: 0.2
    })
  },
  methods: {
    btnclick () {
      const $button = document.querySelector('.button')
      const duration = 0.3
      const delay = 0.08
      console.log(duration, delay)
      TweenMax.from($button, duration, {
          scale: 0,
          rotation: -180,
          y: 300,
          letterSpacing: '100px'
      })
      TweenMax.to($button, duration, { scaleY: 1.6, ease: Expo.easeOut })
      TweenMax.to($button, duration, { scaleX: 1.2, scaleY: 1, ease: Back.easeOut, easeParams: [3], delay: delay })
      TweenMax.to($button, duration * 1.25, { scaleX: 1, scaleY: 1, ease: Back.easeOut, easeParams: [6], delay: delay * 3 })
      this.$store.state.activename = 'first'
      setTimeout(() => {
        this.$router.push('/query')
      }, 600)
    },
    btn () {
      this.$router.push('/query')
    }
  }
}
</script>

<style scoped>
.mycard1 {
  background-image: url(../assets/card1.jpg) !important;
  height: 200px;
  background-size: 100%;
}
.el-card {
  margin: 10px;
  margin-bottom: 40px;
  height: 200px;
  transition: all .5s;
  box-shadow: 10px 10px 5px #000000;
}
.el-card:hover {
  width: 95%;
  /* height: 220px; */
  margin-top: -5px;
}
.mycard2 {
  background-image: url(../assets/card2.jpg) !important;
  height: 200px;
  background-size: 100%;
}
.mycard3 {
  background-image: url(../assets/card3.jpeg) !important;
  height: 200px;
  background-size: 100%;
}
.mycard4 {
  background-image: url(../assets/card4.jpeg) !important;
  height: 200px;
  background-size: 100%;
}
.mycard5 {
  background-image: url(../assets/card5.jpg) !important;
  height: 200px;
  background-size: 100%;
}
.el-calendar {
  opacity: 0.8;
  width: 100%;
}
.fo {
   font-size: 25px
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
.m-header {
  position: relative;
  height: 70px;
  text-align: center;
  color: $color-theme;
}
.text {
  display: inline-block;
  vertical-align: middle;
  color: #4a6266;
  font-size: 25px;
  font-family: 'STXingkai';
  background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);
}
.icon {
  display: inline-block;
  vertical-align: top;
  margin-top: 11px;
  width: 30px;
  height: 32px;
  margin-right: 9px;
  background-image: url(../assets/bg.jpg);
  background-size: 30px 32px;
}
.button {
  border-radius: 3px;
  width: 250px;
  height: 40px;
  background: linear-gradient(to bottom, #4eb5e5 0%,#389ed5 100%); /* W3C */
  border: none;
  border-radius: 5px;
  position: relative;
  border-bottom: 4px solid #2b8bc6;
  color: #fbfbfb;
  font-weight: 600;
  font-family: 'Open Sans', sans-serif;
  text-shadow: 3px 3px 3px rgba(0,0,0,.4);
  font-size: 26px;
  text-align: center;
  text-indent: 5px;
  box-shadow: 3px 3px 3px 3px rgba(0,0,0,.2);
  cursor: pointer;
  display: block;
  margin: 0 auto;
}
.button :hover {
  cursor: pointer;
}
.button:after {
  content: "";
  width: 0;
  height: 0;
  display: block;
  border-top: 20px solid #187dbc;
  border-bottom: 20px solid #187dbc;
  border-left: 16px solid transparent;
  border-right: 20px solid #187dbc;
  position: absolute;
  opacity: 0.6;
  right: 0;
  top: 0;
  border-radius: 0 5px 5px 0;
}
.btn {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  margin-top: 20px;
}
</style>
