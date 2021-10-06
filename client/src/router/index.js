import Vue from 'vue'
import VueRouter from 'vue-router'
import Query from '../components/Query.vue'
import Map from '../components/mymap.vue'
import Result from '../components/Result.vue'
import CollegeQuery from '../components/CollegeQuery.vue'
import CollegeRank from '../components/CollegeRank.vue'
import Jobs from '../components/Jobs.vue'
import HomePage from '../components/HomePage.vue'
import About from '../components/About.vue'

Vue.use(VueRouter)

const originalReplace = VueRouter.prototype.replace
VueRouter.prototype.replace = function replace (location) {
    return originalReplace.call(this, location).catch(err => err)
}

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

const routes = [
  {
    path: '',
    redirect: '/HomePage'
    },
  {
    path: '/query',
    component: Query
    },
  { path: '/mymap', component: Map },
  { path: '/queryCollege', component: CollegeQuery },
  { path: '/result', component: Result },
  { path: '/collegeRank', component: CollegeRank },
  { path: '/Jobs', component: Jobs },
  { path: '/HomePage', component: HomePage },
  { path: '/aboutus', component: About }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
