<script setup>
  import SpeedRadial from '~/components/radial/SpeedRadial.vue';
  const counter = useCounterStore()

  import PrimaryButton from '~/components/btn/PrimaryButton.vue'
  import DangerButton from '~/components/btn/DangerButton.vue'

</script>

<template>
  <div class="container mx-auto px-4 py-2">

    <div class="flex gap-8 items-center mt-20">
      
      <div class="py-8 flex flex-col gap-6">
        <PrimaryButton :text="`+ 5 Kw`" @click="counter.incKw" />
        <DangerButton :text="`- 5 Kw`" @click="counter.decKw" />     
      </div>

      <SpeedRadial />

      <div class="py-8 flex flex-col gap-6">
        <PrimaryButton :text="`+ 10 Kw`" @click="counter.valueKw += 10" />
        <DangerButton :text="`- 10 Kw`" @click="counter.valueKw -= 10" />     
      </div>

    </div>
 
  </div>
</template>
