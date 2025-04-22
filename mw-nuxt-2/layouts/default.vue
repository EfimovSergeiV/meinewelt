<script setup>
// If you want to use it in setup, import from the nuxtApp.
const { $pwa } = useNuxtApp()
const date = useAppConfig().buildDate
// const toast = useToast()

  onMounted(() => {
    if ($pwa.offlineReady)
      // toast.success('App ready to work offline')
     alert('App ready to work offline')
  })
</script>

<template>
  <div>

    <NuxtPwaAssets />

    <div class="">
      <div class="min-h-screen ">
        <HeaderSection />

        <slot />
        <FooterSection class="" />
      </div>
      


    </div>

    
  </div>
</template>