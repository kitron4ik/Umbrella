<template>
    <div>
        <component :is="headerComponent"></component>
        <main class="PacZap">
            <section class="DocZap">
                    <h5 className ="Zapis">Пациенты на запись</h5>
                    <a href="">
                        <div className="CardName">
                            <p className = "Names">Гетьман Владислав Сергеевич</p>
                            <p className ="Time">10:15</p>
                        </div>
                    </a>
                    
            </section>
        </main>
    </div>
</template>


<style scoped>
a {
    text-decoration: none;
}
.Time {
    text-align: center;
    display: flex;
    margin: 25% 0 0 28%;
    font-size: 100px;
}
.Names {
    display: flex;
    margin: 2% 0 0 8%;
    
}
.Zapis {
        font-family: 'Montserrat', light;
        color:#05b8d8;
        margin: 0 auto;

        font-size: 64px;
        font-weight: 275;
        /* text-align: center;
        line-height: 78px;
        margin-top: 0px; */
        box-sizing: border-box;
        border-bottom: 1px solid rgb(31, 197, 219);
        max-width: 700px;
        margin-bottom: 25px;
        
}
.CardName {
    background-color: rgb(201, 250, 250);
    border-radius: 25px;
    box-sizing: border-box;
    border: 1px solid rgb(31, 197, 219);
    font-family: 'Montserrat', light;
    margin: 0 auto;
    color:#05b8d8;
    font-size: 25px;
    height: 500px;
    width: 500px;
    max-height: 500px;
    cursor: pointer;
}

.PacZap {
    background: linear-gradient(135.00deg, rgba(31, 166, 219, 0.2),rgba(0, 0, 0, 0) 37.405%,rgba(0, 0, 0, 0) 69.975%,rgba(31, 181, 219, 0.2) 100%),rgba(255, 255, 255, 0);
}
.DocZap {
    height: 100vh;
    padding-top: 75px;
    font-size: 144px;
}
</style>

<script>
import HeaderDoc from '../../components/Headers/HeaderDoc.vue';

export default {
    components: {
        HeaderDoc,
    },
    computed: {
    headerComponent() {
      return this.role === 'пациент' ? 'HeaderPac' : 'HeaderDoc';
    },
  },
}
</script>

