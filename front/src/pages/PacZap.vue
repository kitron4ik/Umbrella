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
                                <a href="/ZapPac" class="header_link">Пациенты на запись</a>
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
        <main class="PacZap">
            <section class="DocZap">
                    <h5 className ="Zapis">Пациенты на запись</h5>
                    <div className="CardName">
                        <p className = "Names">Гетьман Владислав Сергеевич</p>
                        <p className ="Time">10:15</p>
                    </div>
            </section>
        </main>
    </div>
</template>


<style scoped>

.Time {
    text-align: center;
    display: flex;
    margin: 25% 0 0 28%;
    font-size: 100px;
}
.Names {
    display: flex;
    margin: 2% 0 0 8%
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
export default {

}
</script>

