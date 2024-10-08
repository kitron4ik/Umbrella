<template>
  <div>
    <header class="header">
        <div class="wrapper">
            <div class="header_wrapper">
                <div class="header_logo">
                    <a href="/" class="header_logo_link">
                        <img src="../assets/png/logo.png" alt="logo">
                    </a>
                </div>
                <nav class="header_nav">
                    <ul class="header_list">
                        <li class="header_item">
                            <a href="/dp" class="header_link">Мой профиль</a>
                        </li>
                        <li class="header_item">
                            <a href="/pz" class="header_link">Пациенты на запись</a>
                        </li>
                        <li class="header_item">
                            <a href="/docGr" class="header_link" id="openRegister">Мой график</a>
                        </li>
                        <li class="header_item">
                            <a href="/spCard" class="header_link" id="openLogin">Список карт</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="main">
        <section class="Doc">
            <div className ="WC">
                <h5 className="WelCome">Добро пожаловать в личный кабинет</h5>
            </div>
            <div>
                <input type="text" class="group" v-model="name" placeholder="ФИО" required />
                <input type="email" class="group" v-model="email" placeholder="Email" required />
                <input type="text" class="group" v-model="buildingCode" placeholder="Поликлиника" required />
                <input type="text" class="group" v-model="role" placeholder="Роль" required />
            </div>
            <div className="Cilindr">
                
            </div>
        </section>
    </main>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.Cilindr {
    width: 500px;
    height: 500px;
    display: flex;
    margin: -30vh 0 0 1000px;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    background: rgb(121, 230, 238);
    border-radius: 100%;
}

.WC {
    margin-bottom: 50px;
}
.group {
  display: flex;
  width: 25%;
  margin: 0 0 25px 39vh;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.Doc {
    height: 100vh;
    padding-top: 75px;
    font-size: 144px;
    

}
    .WelCome {
        
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
        max-width: 1250px;
        
    }
</style>