<script setup>

  const props = defineProps(['text'])


</script>


<template>
  <div class="">
    
    
    
    
    <button class="bg-red-500 active:bg-red-700 border border-rose-300 active:border-rose-200 text-white w-36 px-6 py-2 rounded transition-all duration-100 select-none">
      <p class="text-white">{{ text }}</p>
    </button>




  </div>
</template>