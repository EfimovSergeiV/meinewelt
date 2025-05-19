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
    <p class="text-white text-2xl">Test yandex metrika</p>

    <div class="mt-6">
      <div class="flex items-center gap-6">
        <p class="text-white text-xl font-semibold">Latest button clicked:</p>
        <p class="text-white text-xl">{{ latestButton }} {{ counterButton }}</p>
      </div>

      <div class="grid grid-cols-3 gap-8 my-8">
        <button class="bg-blue-600 rounded-md text-white py-4 hover:bg-blue-600/90 active:bg-blue-700/90 transition duration-300" @click="firstButton(); changeLatest(`first btn`)">First button</button>
        <button class="bg-blue-600 rounded-md text-white py-4 hover:bg-blue-600/90 active:bg-blue-700/90 transition duration-300" @click="secondButton(); changeLatest(`second btn`)">Second button</button>
        <button class="bg-blue-600 rounded-md text-white py-4 hover:bg-blue-600/90 active:bg-blue-700/90 transition duration-300" @click="thirdButton(); changeLatest(`third btn`)">Third button</button>
      </div>

    </div>
  </div>
</template>