<script>
  export default {
    mounted() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('show');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1
    });

    elements.forEach(el => {
      observer.observe(el);
    });
  }
  }
</script>

<template>
    <main class="two">
      <section id="twourto">
        <h5 class="about animate-on-scroll">О нас</h5>
        <div class="opis animate-on-scroll">
          <h4 class="vracham animate-on-scroll">Помощь лечащим врачам</h4>
          <h2 class="opisvrach animate-on-scroll">
            Врачам будет легче заполнять медицинские карты, что позволит сократить
            время, а также поможет автоматизировать процессы, например:
            заполнение колонок заболеваний при помощи блоков, создание готовой
            справки для пациента с заранее прописанным ФИО и датой, когда и чем он болел.
          </h2>
          <h4 class="pacient animate-on-scroll">Помощь пациентам</h4>
          <h2 class="opisclient animate-on-scroll">
            У пациентов будет доступ к своей карточке, и им не нужно будет забирать
            её из регистратуры. Также там будут отображаться лекарства, которые выписал доктор.
          </h2>
        </div>
        <img src="../../assets/png/TwoutroShest/Lbol.png" alt="Lbol" class="Lbol animate-on-scroll"/>
        <img src="../../assets/png/TwoutroShest/LMal.png" alt="LMal" class="LMal animate-on-scroll"/>
        <img src="../../assets/png/TwoutroShest/LSred.png" alt="LSred" class="LSred animate-on-scroll"/>
        <img src="../../assets/png/TwoutroShest/Rbol.png" alt="Rbol" class="Rbol animate-on-scroll"/>
        <img src="../../assets/png/TwoutroShest/Rmal.png" alt="Rmal" class="Rmal animate-on-scroll"/>
      </section>
    </main>
</template>
  

<style scoped>


.Lbol, .LMal, .LSred, .Rbol, .Rmal {
    margin:0 auto;
    position: absolute;
}
.Rbol {
    right: -8%;
    top: 115%
}

.Rmal {
    right: 18%;
    top: 105%
}

.Lbol {
    left:15%;
    top: 160%

}

.LMal {
    left:3%;
    top: 160%
}
    .about {
    
    font-family: 'Montserrat', light;
    color:#00C9C9;
    margin: 0 auto;
    font-size: 64px;
    font-weight: 275;
    text-align: center;
    line-height: 78px;
    margin-top: 55px;
    box-sizing: border-box;
    max-width: 200px;
    margin-bottom: 36px;

}

.opis {
    
    font-family: 'Montserrat', light;
    height: 75vh;
    max-width: 1440px;
    margin: 0 auto;
    color:#00C9C9;
    
}

.vracham {
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    border-radius: 0 0 25px 25px;
    font-family: 'Montserrat', light;
    color:#00C9C9;
    font-size: 48px;
    font-weight: 300;
    line-height: 59px;
    box-sizing: border-box;
    max-width: max-content;
}

.opisvrach {
    font-family: 'Montserrat', light;
    font-size: 36px;
    font-weight: 275;
    line-height: 44px;
    max-width: 1150px;
    color:#00C9C9;
    margin-top: 10px;
    
}

.pacient {
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    border-radius: 0 0 25px 25px;
    font-family: 'Montserrat', light;
    color:#00C9C9;
    font-size: 48px;
    font-weight: 300;
    line-height: 59px;
    box-sizing: border-box;

    max-width: max-content;
    margin-left: 48%;
}

.opisclient {
    font-family: 'Montserrat', light;
    font-size: 36px;
    font-weight: 275;
    line-height: 44px;
    max-width: 600px;
    color:#05b8d8;
    margin-left: 700px;
}
</style>