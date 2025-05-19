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
</script>

<template>
  <!-- <div class="bg-fixed bg-no-repeat bg-cover bg-center bg-[url('movie-bg.webp')] dark:bg-[url('movie-bg.webp')] min-h-screen"> -->
  <div class=" min-h-screen">

    <NuxtPwaAssets />

    <div class="">
      <div class="min-h-screen flex flex-col justify-between">
        <!-- <HeaderSection /> -->
        <slot />
        <!-- <FooterSection /> -->
      </div>
    </div>
    
  </div>
</template>