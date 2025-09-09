<script setup>
  import CircleControl from '~/components/radial/CircleControl.vue'
  import SemicircleControl from './components/radial/SemicircleControl.vue'
  import PrimaryButton from './components/btn/PrimaryButton.vue'
  import DangerButton from './components/btn/DangerButton.vue'
  
  const counter = useCounterStore()
  const route = useRoute()

  import { onMounted } from 'vue'

  onMounted(async () => {
    const time = await window.ipcRenderer.invoke('app-start-time')
    console.log('App start time:', time)
  })

  onMounted(() => {
    if (window.electronAPI) {
      window.electronAPI.onNavigate((route) => {
        navigateTo(route)
      })
    }
  })
</script>


<template>
  <div>

    <div class="bg-fixed bg-no-repeat bg-cover bg-center bg-[url('movie-bg.webp')] dark:bg-[url('movie-bg.webp')] min-h-screen">

      <div class="flex flex-col justify-between min-h-screen bg-gray-100/50 dark:bg-gray-900/50 backdrop-blur-sm">
        <AppHeader />
        <NuxtPage />


        <div>
          <div v-if="route.name !== 'three'" class="container mx-auto px-4 py-2">
            
            <div class="flex items-end justify-between ">
              <div class="c">
                <div class="">
                  <div class="flex gap-8 items-center mt-20">
                    
                    <div class="py-8 flex flex-col gap-6">
                      <PrimaryButton :text="`+ 5 Kw`" :width="`w-36`" @click="counter.incKw" />
                      <DangerButton :text="`- 5 Kw`" :width="`w-36`" @click="counter.decKw" />     
                    </div>

                    <CircleControl />

                    <div class="py-8 flex flex-col gap-6">
                      <PrimaryButton :text="`+ 10 Kw`" :width="`w-36`" @click="counter.valueKw += 10" />
                      <DangerButton :text="`- 10 Kw`" :width="`w-36`" @click="counter.valueKw -= 10" />     
                    </div>

                  </div>
                </div>
              </div>

              <div class="">
                <div class="">
                  <div class="flex gap-8 items-center mt-20">
                    
                    <SemicircleControl />
                    <SemicircleControl />
                    <SemicircleControl />

                  </div>
                </div>
              </div>
            </div>
          </div>

        <AppFooter />

        </div>



      </div>

    </div>

  </div>
</template>

