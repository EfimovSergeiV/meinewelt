<script setup>
  // const config = useRuntimeConfig()

  // If you want to use it in setup, import from the nuxtApp.
  // const { $pwa } = useNuxtApp()
  // const date = useAppConfig().buildDate
  // const toast = useToast()


  // onMounted(() => {
  //   if ($pwa.offlineReady)
  //     // toast.success('App ready to work offline')
  //    alert('App ready to work offline')
  // })

import { onMounted } from 'vue'
import gsap from 'gsap'
import ScrollSmoother from 'gsap/ScrollSmoother'

onMounted(() => {
  gsap.registerPlugin(ScrollSmoother)

  ScrollSmoother.create({
    smooth: 1.5,
    effects: true
  })
})

</script>

<template>
  <div>

    <div
      class="fixed inset-0 -z-10
            bg-no-repeat bg-cover bg-center
            bg-[url('movie-bg.webp')]
            dark:bg-[url('movie-bg.webp')]" />


    <div id="smooth-wrapper">
      <div id="smooth-content" class="min-h-screen flex flex-col justify-between">

        <NuxtPwaAssets />

        <HeaderSection />
          <slot />
        <FooterSection />

      </div>
    </div>

  </div>
</template>