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
                            <a href="/pp" class="header_link">Мой профиль</a>
                        </li>
                        <li class="header_item">
                            <a href="/zp" class="header_link">Записаться на приём</a>
                        </li>
                        <li class="header_item">
                            <a href="/MyCard" class="header_link" id="openRegister">Моя карточка</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="three">
        <section id="func">
            <div class="functia">
                <h4 class="MyCard">Моя карта</h4>
                <img src="../assets/png/card.png" alt="card" class="card"/>
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
    .MyCard{
    max-width: 50vh;
    font-family: 'Montserrat', light;
    color:#05b8d8;
    margin: 0 auto;
    font-size: 64px;
    font-weight: 275;
    text-align: center;
    line-height: 78px;
    margin-top: 55px;
    box-sizing: border-box;
    border-bottom: 1px solid rgb(31, 191, 219);
    max-width:max-content;
    margin-bottom: 36px;
    }
</style>