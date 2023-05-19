import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import VueTreeList from 'vue-tree-list'

const app = createApp(App)

app.use(router)
// app.use(VueTreeList)
app.mount('#app')

import "bootstrap/dist/js/bootstrap.js"