<script setup>
  import { onMounted } from 'vue'
  import gsap from 'gsap'
  import ScrollSmoother from 'gsap/ScrollSmoother'

  useSeoMeta({
    title: 'ABT : MEINEWELT.RU',
    description: 'ABT : MEINEWELT.RU',
    keywords: 'ABT : MEINEWELT.RU',
    ogLocale: 'ru_RU',
    ogTitle: 'ABT : MEINEWELT.RU',
    ogDescription: 'ABT : MEINEWELT.RU',
  })

  onMounted(() => {
    gsap.registerPlugin(ScrollSmoother)

    ScrollSmoother.create({
      smooth: 1.5,
      effects: true
    })
  })

  const aboutText = ref("Я DevOps-инженер и разработчик с фокусом на построении устойчивых и масштабируемых систем. Соединяю разработку и инфраструктуру в единую управляемую среду: от архитектуры приложения до продакшн-развёртывания. Работаю с Python-экосистемой, проектирую backend-сервисы на базе Django и REST API, строю frontend-приложения на Nuxt. В DevOps-части занимаюсь контейнеризацией, CI/CD, настройкой reverse-proxy, TLS, сетевой изоляцией и мониторингом. Предпочитаю Linux-инфраструктуру, декларативные конфигурации и автоматизацию процессов. Моя цель — создавать системы, которые легко разворачиваются, масштабируются и поддерживаются.")

</script>


<template>
  <div class="text-white mx-auto px-4 container">
    
    <div class="h-screen flex items-center justify-center">
      <div class="">
        <div><p class="text-8xl uppercase font-semibold">About me</p></div>
      </div>
    </div>
    
    <div class="h-screen flex items-center justify-center">
      <div class=" w-1/2">
        <div v-gsap.whenVisible.animateText class="text-2xl font-semibold text-white "><p>{{ aboutText }}</p></div>
          <p class="text-sm text-end mt-8">(c) Writed by ChatGPT</p>
      </div>
    </div>
    
    <div class="h-screen flex items-center justify-center">
      <article v-gsap.whenVisible.from="{ scale: 0.8, height: 0, padding: 0 }">
        <!-- <div v-gsap.whenVisible.from="{ y: 100 }"></div> -->
        <div v-gsap.whenVisible.delay-1000.stagger.from="{ opacity: 0, x: -40 }" class="text-2xl text-center font-semibold">
          <p class="text-center">mail@efimovsergei.ru</p>
          <p>meinewelt.ru</p>
          <p>efimovsergei.ru</p>
        </div>
      </article>
    </div>

  </div>
</template>
