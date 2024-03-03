<script setup>

  const { data: test } = await useFetch(`https://api.glsvar.ru/c/prods/?brnd=3`)
  
  const land = ref('')
  const operator = ref('')
  const region = ref('')
  const number = ref('')

  const fullnumber = ref('')

  watch([land, operator, region, number], (val) => {
    if (land.value == '7' || land.value == '8' ) {
      document.getElementById('operator').focus()
      if (land.value == '7') {
        land.value = '+7'
      }
    }
    if (operator.value.length == 3) {
      document.getElementById('region').focus()
    }
    if (region.value.length == 3) {
      document.getElementById('number').focus()
    }
    number.value = number.value.replace(/(\d{2})(\d{2})/, '$1-$2')
    
  })

  watch(fullnumber, (val) => {
    if (fullnumber.value[0] == '8') {
      if (fullnumber.value.length == 4) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\d{3})/, '$1 ($2) ')
      }
      if (fullnumber.value.length == 13) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\s\()(\d{3})(\))(\s)(\d{3})(\d{2})/, '$1 ($3) $6-$7')
      }

      if (fullnumber.value.length == 11) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})/, '$1 ($2) $3-$4-$5')
      }      
    }

    if (fullnumber.value[0] == '7' || fullnumber.value.slice(0, 2) == '+7'){
      if (fullnumber.value.length == 4) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\d{3})/, '+$1 ($2) ')
      }
      if (fullnumber.value.length == 5) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\d{3})/, '$1 ($2) ')
      }
      if (fullnumber.value.length == 14) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\s\()(\d{3})(\))(\s)(\d{3})(\d{2})/, '$1 ($3) $6-$7')
      }
      
      if (fullnumber.value.length == 11) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\d{3})(\d{3})(\d{2})/, '+$1 ($2) $3-$4')
      }   
      if (fullnumber.value.length == 12) {
        fullnumber.value = fullnumber.value.replace(/(\d{1})(\d{3})(\d{3})(\d{2})/, '$1 ($2) $3-$4')
      }      
    }
    

  })


</script>


<template>
  <div class="py-4">
    <div class="grid grid-cols-1 gap-4">

      <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-2 gap-4">
        
        <div>
          <div class="bg-gray-700 border border-gray-500 px-4 py-4 rounded-2xl">
            <div  class="h-[200px] "> 
              
              <div class="flex">
                <div class="flex bg-white text-gray-800">
                  <input id="land" v-model="land" maxlength="2" type="text" class="w-8 text-center bg-white text-gray-800" placeholder="">
                  (<input id="operator" v-model="operator" maxlength="3" type="text" class="w-10 text-center bg-white text-gray-800" placeholder="">)
                  <input id="region" v-model="region" maxlength="3" type="text" class="w-10 text-center bg-white text-gray-800" placeholder="">
                  <input id="number" v-model="number" maxlength="5" type="text" class="w-12 text-center bg-white text-gray-800" placeholder="">
                </div>
              </div>
              
              <div class="grid grid-cols-1 gap-2 mt-4">
                <p>{{ fullnumber }} ({{ fullnumber.length }})</p>
                <input type="text" v-model="fullnumber" maxlength="18" class="text-gray-300" placeholder="">
              </div>
                   
            </div>      
          </div>      
        </div>
        
        <div v-for="i in 3" :key="i">
          <div class="bg-gray-700 border border-gray-500 px-4 py-4 rounded-2xl">
            <div v-for="i in 6" :key="i" class="">
              <p class="">
                This is the index page
              </p>      
            </div>      
          </div>      
        </div>
      </div>

      <div class="grid grid-cols-1 gap-4">
        <div v-for="i in 1" :key="i">
          <div class="bg-gray-700 border border-gray-500 px-4 py-4 rounded-2xl">
            <div v-for="i in 6" :key="i" class="">
              <p class="">
                This is the index page
              </p>      
            </div>      
          </div>      
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4">
        <div v-for="i in 6" :key="i">
          <div class="bg-gray-700 border border-gray-500 px-4 py-4 rounded-2xl">
            <div v-for="i in 6" :key="i" class="">
              <p class="">
                This is the index page
              </p>      
            </div>      
          </div>
        </div>
      </div>

    </div>
  </div>
</template>