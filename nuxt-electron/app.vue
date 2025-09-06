<script setup>
  import { onMounted } from 'vue'

  onMounted(async () => {
    const time = await window.ipcRenderer.invoke('app-start-time')
    console.log('App start time:', time)
  })

  onMounted(() => {
    if (window.electronAPI) {
      window.electronAPI.onNavigate((route) => {
        navigateTo(route)
      })
    }
  })
</script>


<template>
  <div>

    <div class="bg-fixed bg-no-repeat bg-cover bg-center bg-[url('movie-bg.webp')] dark:bg-[url('movie-bg.webp')] min-h-screen">

      <div class="flex flex-col justify-between min-h-screen">
        <AppHeader />
        <NuxtPage />
        <AppFooter />
      </div>

    </div>

  </div>
</template>

