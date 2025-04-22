<template>
  <div class="container mx-auto">
    <div class="flex items-center justify-end gap-8 py-4">
      <div class="">
        <nuxt-link :to="{ name: 'index' }">Главная</nuxt-link>
      </div>
      <div class="">
        <p>Блог</p>
      </div>
      <div class="">
        <nuxt-link :to="{ name: 'links' }">Ссылки</nuxt-link>
      </div>
    </div>
  </div>
</template>