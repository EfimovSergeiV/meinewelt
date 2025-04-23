<script setup>
  const config = useRuntimeConfig()


  const skills = await $fetch(`${ config.public.baseURL }bl/skills/`, { method: 'GET' }).catch((error) => error.data)

</script>


<template>
  <div class="container mx-auto">
    
    <div class="text-gray-100 dark:text-gray-100">

      <div class="flex items-center justify-center">
        <img src="/profile-img.jpg" class="profile-img h-48 text-blue-600" >
      </div>

      <div class="grid grid-cols-1 gap-2">
        <div class="flex items-center justify-center">
          <p class="text-2xl font-semibold">S2NULLNULLACHTUNDFÜNFZIG</p>
        </div>
        <div class="flex items-center justify-center">
          <p class="text-2xl font-semibold">Сергей Ефимов</p>
        </div>
      </div>

      <BadgesSection :skills="skills" class="flex items-center justify-center py-8" />

    </div>

  </div>
</template>