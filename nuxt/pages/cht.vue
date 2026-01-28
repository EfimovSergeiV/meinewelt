<script setup>
import ThreeExample from '~/components/ThreeExample.vue';
import TiptapEditor from '~/components/TiptapEditor.vue';


  useSeoMeta({
    title: 'CHT : MEINEWELT.RU',
    description: 'CHT : MEINEWELT.RU',
    keywords: 'CHT : MEINEWELT.RU',
    ogLocale: 'ru_RU',
    ogTitle: 'CHT : MEINEWELT.RU',
    ogDescription: 'CHT : MEINEWELT.RU',
  })


</script>


<template>
  
  
  <div class="container mx-auto px-4 py-8">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <SocketChat />
      <ThreeExample />
    </div>


    <div class="">
      <TiptapEditor />
    </div>

  
  
  </div>

</template>