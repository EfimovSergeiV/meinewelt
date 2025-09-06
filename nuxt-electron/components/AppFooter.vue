<script setup>
  import { useRoute } from 'vue-router'
  const route = useRoute()



</script>


<template>
  <footer class="text-white py-4 select-none">
    <div class="container mx-auto text-center">
      <p class="text-xs"><span class="text-base">{{ route.name }}</span> - Powered by Nuxt 3 & Electron</p>
      <p class="text-xs">&copy; 2023 MeineWelt GmbH. All rights reserved.</p>
    </div>
  </footer>
</template>


