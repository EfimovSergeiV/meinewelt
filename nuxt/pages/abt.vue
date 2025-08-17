<script setup>
  const ctx = useNuxtApp()



  const firstButton = () => {
    if (import.meta.client) {
      ctx.$metrika.reachGoal('FIRST_BUTTON')
    }
  }

  const secondButton = () => {
    if (import.meta.client) {
      ctx.$metrika.reachGoal('SECOND_BUTTON')
    }
  }

  const thirdButton = () => {
    if (import.meta.client) {
      ctx.$metrika.reachGoal('THIRD_BUTTON')
    }
  }

  const latestButton = ref("")
  const counterButton = ref(null)
  const changeLatest = (latest) => {
    if ( latestButton.value === latest ) {
      counterButton.value = counterButton.value + 1
    } else {
      latestButton.value = latest
      counterButton.value = null     
    }
  }

</script>

<template>
  <div class="container mx-auto px-4 py-8">

    <div class="grid grid-cols-1 gap-4 ">
      <div class="flex">
        <p class="text-white text-2xl font-semibold px-2 py-1">В этом проекте я обкатываю и учусь технологиям</p>
      </div>
      <div class="flex">
        <p class="text-white text-xl px-2 py-1">Связаться со мной, пригласить поучавствовать в каком то проекте, можно по почте <a href="mailto:efimovsergeiv@gmail.com" target="_blank" class="text-white underline">efimovsergeiv@gmail.com</a></p>
      </div>
      <div class="mt-6 flex items-center gap-4">
        <p class="text-white text-xl px-2 py-1">Так же я в соцсетях:</p>
        <a href="https://vk.com/s2nullnullachtundfunfzig" target="_blank" class="text-white text-xl font-semibold underline px-2 py-1">VK.RU</a>
        <a href="https://www.facebook.com/s2nnauf/" target="_blank" class="text-white text-xl font-semibold underline px-2 py-1">Facebook</a>
      </div>
    </div>



    <div class="mt-6 hidden">
      <div class="flex items-center gap-6">
        <p class="text-white text-xl font-semibold">Latest button clicked:</p>
        <p class="text-white text-xl">{{ latestButton }} {{ counterButton }}</p>
      </div>

      <div class="grid grid-cols-3 gap-8 my-8">
        <button id="first-btn" class="bg-blue-600 rounded-md text-white py-4 hover:bg-blue-600/90 active:bg-blue-700/90 transition duration-300" @click="firstButton(); changeLatest(`first btn`)">Like 1</button>
        <button id="second-btn" class="bg-blue-600 rounded-md text-white py-4 hover:bg-blue-600/90 active:bg-blue-700/90 transition duration-300" @click="secondButton(); changeLatest(`second btn`)">Like 2</button>
        <button id="third-btn" class="bg-blue-600 rounded-md text-white py-4 hover:bg-blue-600/90 active:bg-blue-700/90 transition duration-300" @click="thirdButton(); changeLatest(`third btn`)">Like 3</button>
      </div>

    </div>
  </div>
</template>