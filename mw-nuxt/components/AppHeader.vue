<script setup>



</script>


<template>
  <div class="bg-gray-700/70 backdrop-blur-md px-2 rounded-b-2xl border-b border-l border-r border-gray-500 py-4 lg:py-2">
    <div class="flex items-center justify-between gap-2">
      
      <div class="">
        <nuxt-link :to="{ name: 'index' }">
          <img src="/mw-logo.webp" class="w-[120px] md:w-[220px]" />
        </nuxt-link>
      </div>

      <div class="flex gap-4">
        <nuxt-link class="uppercase font-semibold italic text-sm md:text-xl" to="/">Главная</nuxt-link>
        <nuxt-link class="uppercase font-semibold italic text-sm md:text-xl" to="/">Разработка</nuxt-link>
        <nuxt-link class="uppercase font-semibold italic text-sm md:text-xl" to="/about">О Проекте</nuxt-link>        
      </div>

      <div class="">

      </div>

    </div>
  </div>
</template>