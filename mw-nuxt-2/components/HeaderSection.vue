<template>
  <div class="container mx-auto px-8">
    <div class="flex items-center justify-end gap-8 py-4 text-gray-100 dark:text-gray-100">
      <div class="">
        <nuxt-link :to="{ name: 'index' }">Главная</nuxt-link>
      </div>
      <div class="">
        <nuxt-link :to="{ name: 'links' }">Блог</nuxt-link>
      </div>
      <div class="">
        <nuxt-link :to="{ name: 'links' }">Ссылки</nuxt-link>
      </div>
    </div>
  </div>
</template>