import Vue from 'vue'
import Vuex from 'vuex'
import axios from './plugins/axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    clientes: []
  },
  mutations: {
    CHANGE_CLIENTES (state, payload) {
      state.clientes = payload
    },
    CLEAR_CLIENTES (state, payload) {
      state.clientes = []
    }
  },
  actions: {
    startClientes: context => {
      return axios.get('contabilidade/clientes').then(
        response => {
          context.commit('CHANGE_CLIENTES', response.data)
        }
      )
    }
  }
})
