import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
// import VueTreeList from 'vue-tree-list'

import VNetworkGraph from "v-network-graph"

const app = createApp(App)
app.use(router)
app.use(VNetworkGraph)
app.component('VueDatePicker', VueDatePicker)
// app.use(VueTreeList)
app.mount('#app')

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://127.0.0.1:5000/';  // the FastAPI backend

import "bootstrap/dist/js/bootstrap.js"