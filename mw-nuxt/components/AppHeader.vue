<template>
  <div class="bg-gray-700 px-2 rounded-b-2xl">
    <div class="flex items-center justify-between gap-2">
      
      <div class="">
        <nuxt-link :to="{ name: 'index' }">
          <img src="/mw-logo.webp" class="w-[220px]" />
        </nuxt-link>
      </div>

      <div class="flex gap-4">
        <nuxt-link class="uppercase font-semibold italic md:text-xl" to="/">Главная</nuxt-link>
        <nuxt-link class="uppercase font-semibold italic md:text-xl" to="/">Разработка</nuxt-link>
        <nuxt-link class="uppercase font-semibold italic md:text-xl" to="/about">Проект</nuxt-link>        
      </div>

      <div class="">

      </div>

    </div>
  </div>
</template>