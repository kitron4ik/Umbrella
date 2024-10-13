
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
    <main class="three">
        <section id="func">
            <div class="functia">
                <h4 class="fanc animate-on-scroll">Функционал</h4>
                <img src="../../assets/png/card.png" alt="card" class="card animate-on-scroll"/>
                <img src="../../assets/png/TriuShest/BolN.png" alt="BolN" className="BolN animate-on-scroll"/>
                <img src="../../assets/png/TriuShest/MalN.png" alt="MalN" className="MalN animate-on-scroll"/>
            </div>
        </section>
    </main>
</template>

<style scoped>
.BolN, .MalN {
    margin:0 auto;
    position: absolute;
}

.Boln {
    position: absolute;
    top:90%;
    right: -10%;
}

.MalN {
    top:205%;
    right:0%;
}
</style>