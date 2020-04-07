import Vue from 'vue'
import Router from 'vue-router'

import Registry from './views/Registry.vue'
import CreateRegistry from './views/CreateRegistry.vue'
import Index from './views/Index.vue'

Vue.use(Router)

export default new Router({
    routes: [
        { path: '/', name: 'Index', component: Index, props: true },
        { path: '/registry/:registryID', name: 'Registry', component: Registry, props: true },
        { path: '/createregistry', name: 'CreateRegistry', component: CreateRegistry, props: true }
    ],
    mode: 'history'
})