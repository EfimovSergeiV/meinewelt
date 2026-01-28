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
</script>


<template>
  <div class="text-white mx-auto px-4 container">
    
    <div class="h-screen flex items-center justify-center">
      <div class="">
        <div><p class="text-8xl uppercase font-semibold">scroll me down</p></div>
      </div>
    </div>
    
    <div class="h-screen flex items-center justify-center">
      <div class="">
        <div v-gsap.whenVisible.animateText class="text-8xl uppercase font-semibold"><p>Hallo meine welt</p></div>
      </div>
    </div>
    
    <div class="h-screen flex items-center justify-center">
      <article v-gsap.whenVisible.from="{ scale: 0.8, height: 0, padding: 0 }">
        <!-- <div v-gsap.whenVisible.from="{ y: 100 }"></div> -->
        <div v-gsap.whenVisible.delay-1000.stagger.from="{ opacity: 0, x: -40 }" class="text-8xl uppercase font-semibold">
          <p>Hallo meine welt</p>
          <p>Hallo meine welt</p>
          <p>Hallo meine welt</p>
        </div>
      </article>
    </div>

  </div>
</template>
