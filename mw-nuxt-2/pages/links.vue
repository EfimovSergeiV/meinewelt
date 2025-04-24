<script setup>

  const links = [
    { id: 1, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 2, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 3, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 4, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 5, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 6, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 7, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 8, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 9, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 10, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
    { id: 11, name: "Chat GPT", description: "AI сервис от OpenAI", img: "/GPT-tech.webp" },
  ]




</script>


<template>
  <div class="container mx-auto">

    <!-- <div class="flex items-center justify-center h-60 text-gray-100 dark:text-gray-100">
      <p class="text-2xl font-semibold">Ты бы дала за такой сайт?)))</p>
    </div> -->

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div v-for="link in links" :key="link.id" class="text-gray-100 dark:text-gray-100">
        <div class="bg-cyan-900/70 border border-cyan-500/50 rounded-xl">
          
          <div class="">
            <img :src="link.img" class="w-full rounded-t-xl" >
            <div class="grid grid-cols-1 gap-4 px-2 py-2">

              
              <div class="">
                <p class="text-2xl">{{ link.name }}</p>
              </div>
              <div class="">
                <p class="text-base">{{ link.description }}</p>
              </div>
            </div>            
          </div>

          
          
        </div>
      </div>


    </div>



  </div>
</template>