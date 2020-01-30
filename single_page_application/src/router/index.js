import Vue from 'vue'
import Router from 'vue-router'
import page01 from '@/components/page01'
import page02 from '@/components/page02'
import page03 from '@/components/page03'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: page01
    },
    {
      path: '/page02',
      component: page02
    },
    {
      path: '/page03',
      component: page03
    }
  ]
})
