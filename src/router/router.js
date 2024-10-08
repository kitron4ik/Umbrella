import Main from "@/pages/Main.vue";
import { createRouter, createWebHistory } from "vue-router"
import DoctorPage from "@/pages/DoctorPage.vue";
import Pacient from "@/pages/Pacient.vue";
import PacZap from "@/pages/PacZap.vue";
import DrGr from "@/pages/drGr.vue";


const routes = [
    {
        path: '/',
        component: Main
    },
    {
        path: '/dp',
        component: DoctorPage
    },
    {
        path: '/pp',
        component: Pacient
    },
    {
        path: '/pz',
        component: PacZap
    },
    {
        path: '/docGr',
        component: DrGr
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL),
})

export default router;