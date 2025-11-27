<script setup>
import EditorSection from '~/components/EditorSection.vue';
import ThreeExample from '~/components/ThreeExample.vue';





</script>


<template>
  
  
  <div class="container mx-auto px-4 py-8">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <SocketChat />
      <ThreeExample />
    </div>


    <div class="">
      <EditorSection />
    </div>

  
  
  </div>

</template>