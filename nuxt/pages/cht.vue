<script setup>


  const messageText = ref("")

</script>


<template>
  <div class="container mx-auto px-4 py-8">


    <div class="grid grid-cols-2 gap-4">
      <div>
        <p class="text-white">{{ messageText }}</p>

      </div>      
      
      <div>
        <textarea id="message" v-model="messageText" rows="4" class="px-4 py-2 w-full rounded-xl" placeholder="Напишите что-нибудь..."/>
        <button class="mt-2 px-8 py-2 bg-blue-500 text-white rounded-lg" @click="firstButton">Отправить</button>
      </div>


    </div>



  </div>
</template>