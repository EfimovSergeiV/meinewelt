<script setup lang="ts">
  const counter = useCounterStore()

    import PrimaryButton from '~/components/btn/PrimaryButton.vue'
    import DangerButton from '~/components/btn/DangerButton.vue'

</script>

<template>
  <div class="container mx-auto px-4 py-2">

    <div class="flex flex-wrap gap-8 mt-24">

      <div class="">
        <p class="text-white">О программе</p>
        <div class="py-8 px-4">
          <p class="text-gray-300 hover:text-cyan-500">nuxt 3.6.5</p>
          <p class="text-gray-300 hover:text-cyan-500">nuxt-electron 0.7.0</p>
          <p class="text-gray-300 hover:text-cyan-500">electron 29.3.0</p>        
        </div>
      </div>

      <div class="">
        <p class="text-white">Count: {{ counter.count }}</p>
        <div class="py-8 px-4 flex gap-4">
          <PrimaryButton :text="`Добавить`" @click="counter.increment" />
          <DangerButton :text="`Убрать`" @click="counter.decrement" />     
        </div>
      </div>

    
    
    
    </div>




    
  </div>
</template>
