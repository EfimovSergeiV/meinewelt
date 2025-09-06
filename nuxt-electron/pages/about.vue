<script setup lang="ts">
  const counter = useCounterStore()
</script>

<template>
  <div class="container mx-auto px-4 py-2">

    <div class="flex gap-4 mt-8">

      <p class="text-white">О программе</p>
      <div class="">
        <p class="text-gray-300">nuxt 3.6.5</p>
        <p class="text-gray-300">nuxt-electron 0.7.0</p>
        <p class="text-gray-300">electron 29.3.0</p>        
      </div>

      <p class="text-white">Count: {{ counter.count }}</p>
      <div class="">
        <button class="bg-blue-500/60 text-white px-4 py-2 rounded mr-2" @click="counter.increment">Increment</button>
        <button class="bg-red-500/60 text-white px-4 py-2 rounded" @click="counter.decrement">Decrement</button>      
      </div>
    </div>




    
  </div>
</template>
