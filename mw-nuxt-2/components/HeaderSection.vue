<script setup>
  


</script>



<template>
  <div class="container mx-auto px-8">
    <div class="flex flex-row items-center w-full justify-between py-4 text-gray-100 dark:text-gray-100">
      
      <div class="">
        <nuxt-link :to="{ name: 'index' }">
          <img src="/mw-logo.webp" class="h-12">          
        </nuxt-link>
      </div>

      <div class="flex flex-row items-center gap-2 md:gap-4 ">
        <div>
          <nuxt-link :to="{ name: 'index' }" class="font-semibold italic uppercase text-xs md:text-lg">Главная</nuxt-link>
        </div>
        <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
        <div class="">
          <nuxt-link :to="{ name: 'exx' }" class="font-semibold italic uppercase text-xs md:text-lg">EXX</nuxt-link>
        </div>
        <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
        <div class="">
          <nuxt-link :to="{ name: 'about' }" class="font-semibold italic uppercase text-xs md:text-lg">Ссылки</nuxt-link>
        </div>
      </div>

    </div>
  </div>
</template>