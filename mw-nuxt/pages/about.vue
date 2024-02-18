<script setup>

  const { data: test } = await useFetch(`https://api.glsvar.ru/c/prods/?brnd=3`)


</script>


<template>
  <div class="py-4">

    <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4">
      <div v-for="i in 12" :key="i">
      
        <div class="bg-gray-700 border border-gray-500 px-4 py-4 rounded-2xl">
          <div v-for="i in 6" :key="i" class="">
            <p class="">
              This is the about page
            </p>      
          </div>      
        </div>      
      
      </div>
    </div>


  </div>
</template>