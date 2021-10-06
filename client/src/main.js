import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import echarts from 'echarts'
import './plugins/element.js'
// 导入全局样式表
import './assets/css/global.css'
// 导入字体图标
import './assets/icon/iconfont.css'
// 发出请求的包
import axios from 'axios'
// import '../../'
// 配置请求的根路径
axios.defaults.baseURL = 'http://10.208.82.71:5000/'
// axios.defaults.withCredentials = true
Vue.prototype.$http = axios
// Vue.prototype.$echarts = echarts

Vue.config.productionTip = false

Vue.directive('title', {
  inserted: function (el, binding) {
    document.title = '高考志愿推荐系统'
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
