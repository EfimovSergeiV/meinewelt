<script setup>
  import PrimaryButton from '~/components/btn/PrimaryButton.vue'
  
  const colorMode = useColorMode()



</script>


<template>
  <header>
    <div class="container mx-auto px-4 py-2">
      <nav class="flex flex-row gap-4">

        <nuxt-link :to="{ name: 'index' }"><PrimaryButton :text="`Home`" :width="`w-36`" /></nuxt-link>
        <nuxt-link :to="{ name: 'three' }"><PrimaryButton :text="`ThreeJS`" :width="`w-36`" /></nuxt-link>
        <nuxt-link :to="{ name: 'charts' }"><PrimaryButton :text="`ChartsJS`" :width="`w-36`" /></nuxt-link>
        <nuxt-link :to="{ name: 'about' }"><PrimaryButton :text="`About`" :width="`w-36`" /></nuxt-link>


        <div id="color-mode" class="">
          <PrimaryButton :text="`Оформление по умолчанию`" :width="`w-80`" v-if="$colorMode.preference === 'system'" @click="$colorMode.preference = 'dark'" class="" />
          <PrimaryButton :text="`Ночное оформление`" :width="`w-80`" v-if="$colorMode.preference === 'dark'" @click="$colorMode.preference = 'light'" class="" />
          <PrimaryButton :text="`Дневное оформление`" :width="`w-80`" v-if="$colorMode.preference === 'light'" @click="$colorMode.preference = 'system'" class="" />
        </div>


      </nav>
    </div>

  </header>
</template>
