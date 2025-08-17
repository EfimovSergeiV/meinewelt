<template>
  <div>

    <div class="bg-fixed bg-no-repeat bg-cover bg-center bg-[url('movie-bg.webp')] dark:bg-[url('movie-bg.webp')] min-h-screen">

      <AppHeader />
      <NuxtPage />

    </div>

  </div>
</template>

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
