
<script>
  export default {

  }
</script>

<template>
  <main class="main">
    <section class="intro">
        <div class="wrapper">
            <h1 class="intro_title fade-up__text-500">UMBRELLA</h1>
            <p class="intro_subtitle fade-up__text-800">С заботой о вашем времени</p>
        </div>
        <img src="../../assets/png/doc.png" alt="Doctor" className="Doctor fade-up__text-800"/>
    </section>   
    <img src="../../assets/png/IntroShest/Bolshoi.png" alt="Bolshoi" className="Bolshoi fade-up__text-1000"/>
    <img src="../../assets/png/IntroShest/srednii.png" alt="Srednii" className="Srednii fade-up__text-1100"/>
    <img src="../../assets/png/IntroShest/Malenkii.png" alt="Malenkii" className="Malenkii fade-up__text-1200"/>
    <img src="../../assets/png/IntroShest/verhnii.png" alt="verhnii" className="verhnii fade-up__text-1300"/>

    <div className="cards">
      <div className="container">

        <div class="cards-holder">

          <div className="card fade-up__text-1300">
            <div className="card-image">
              <img className ='cardimg' src="../../assets/png/time.png"/>
            </div>
            <div className="card-title">
                БЫСТРОТА
            </div>
        </div>

        <div className="card fade-up__text-1300">
          <div className="card-image">
            <img className ='cardimg' src="../../assets/png/cool.png"/>
          </div>
          <div className="card-title">
                НАДЁЖНОСТЬ
          </div>
        </div>

        <div className="card fade-up__text-1300">
          <div className="card-image">
            <img className ='cardimg' src="../../assets/png/Shest1.png"/>

          </div>
          <div className="card-title">
                ФУНКЦИОНАЛЬНОСТЬ
          </div>
        </div>
        </div>
        


      </div>
    </div>
</main>
</template>

<style scoped>

.cards {
  z-index: 2;
}
.cards-holder{
  display:flex;
  justify-content: center;
}
.card {
  box-shadow: 10px 10px 40px 20px #0000001A;
  width: 349px;
  height: 200px;
  margin-left: 150px;
  background-color: #fff;
  margin-top: -120px;
  z-index: 2;
  border-radius: 25px;

}
.card-image, .card-title {
  display: flex;
  justify-content: center;
}
.card-image {
  padding-top:10px;
}
.card-title {
  font-family: 'Montserrat', light;
  padding-top: 20px;
  font-size: 25px;
  color:#0092C9;
}
.Doctor {
    position: absolute;
    top: 5%;
    right: -2%;
    margin: 0 auto;
    display: flex;
    
}
.Bolshoi, .Srednii, .Malenkii, .verhnii {
  position: absolute;
  margin: 0 auto;
  display: flex;
}

.Bolshoi {
  right: -15%;
  bottom: -15%;
}

.Srednii {
  bottom: 2%;
  right: 13%
}

.Malenkii {
  bottom:5%;
  right:28%;
}

.verhnii {
  bottom:34%;
  right:7%;
  z-index: -1;
}
</style>