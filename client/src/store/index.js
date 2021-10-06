import Vue from 'vue'
import Vuex from 'vuex'
// import radios from './modules/radios.js'

Vue.use(Vuex)

const item1 = {
      major: '专业',
      rank: 500,
      possibility: 5
    }
    const item2 = {
      major: '专业',
      rank: 550,
      possibility: 3.6
    }
    const item3 = {
      major: '专业',
      rank: 530,
      possibility: 1
    }
    const item4 = {
      major: '专业',
      rank: 515,
      possibility: 2.4
    }

const state = {
  activename: 'first',
  // activenum
  activenum: 0,
  // 排名
  rank: '',
  // 类别
  category: '',
  // 所选省份的列表
  provinces: [],
  // 查询的结果
  res: {
    colleges: ['南京大学', '东南大学', '南京航空航天大学', '南京师范大学'],
    col_majors: {
        南京大学: Array(20).fill(item1),
        东南大学: Array(20).fill(item2),
        南京航空航天大学: Array(20).fill(item3),
        南京师范大学: Array(20).fill(item4)
       }
  },
  all: 'false'
}

const getters = {
  provincesGet () {
    const loc = []
    for (let j = 0; j < state.provinces.length; j++) {
      loc.push(state.provinces[j].pos)
    }
    return loc
  }
}

const mutations = {
  // 设置省份列表
  setProvinces (state, provinces) {
    state.provinces = provinces
    console.log(state)
  }
}

const actions = {
  setPro (context) {
    context.commit('setProvinces')
  }
}

const modules = {
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions,
  modules
})
