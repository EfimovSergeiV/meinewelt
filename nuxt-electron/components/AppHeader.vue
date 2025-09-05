<script setup>
  import PrimaryButton from '~/components/btn/PrimaryButton.vue'




</script>


<template>
  <header>
    <div class="container mx-auto px-4 py-2">
      <nav class="flex flex-row gap-4">

        <nuxt-link :to="{ name: 'index' }"><PrimaryButton :text="`Home`" /></nuxt-link>
        <nuxt-link :to="{ name: 'three' }"><PrimaryButton :text="`ThreeJS`" /></nuxt-link>
        <nuxt-link :to="{ name: 'charts' }"><PrimaryButton :text="`ChartsJS`" /></nuxt-link>
        <nuxt-link :to="{ name: 'about' }"><PrimaryButton :text="`About`" /></nuxt-link>

      </nav>
    </div>

  </header>
</template>
