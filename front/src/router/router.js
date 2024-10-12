import Main from "@/pages/Main.vue";
import { createRouter, createWebHistory } from "vue-router"
import DoctorPage from "@/pages/DoctorPage.vue";
import Pacient from "@/pages/Pacient.vue";
import PacZap from "@/pages/PacZap.vue";
import drGr from "@/pages/drGr.vue";
import spCard from "@/pages/spCard.vue";
import ZapPrim from "@/pages/ZapPrim.vue";
import MyCard from "@/pages/MyCard.vue";


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
        component: drGr
    },
    {
        path: '/spCard',
        component: spCard
    },
    {
        path: '/zp',
        component: ZapPrim
    },
    {
        path: '/MyCard',
        component: MyCard
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL),
})

export default router;