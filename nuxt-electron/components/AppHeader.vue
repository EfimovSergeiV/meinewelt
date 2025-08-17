<template>
  <header>
    <div class="container mx-auto px-4 py-2">
      <nav class="flex flex-row gap-4">

        <nuxt-link :to="{ name: 'index' }" class="text-gray-100">Home</nuxt-link>
        <nuxt-link :to="{ name: 'about' }" class="text-gray-100">About</nuxt-link>

      </nav>
    </div>

  </header>
</template>
