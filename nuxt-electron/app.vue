<script setup>
  import SpeedRadial from '~/components/radial/SpeedRadial.vue'
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

      <div class="flex flex-col justify-between min-h-screen">
        <AppHeader />
        <NuxtPage />


        <div>
          <div v-if="route.name !== 'three'" class="container mx-auto px-4 py-2">
            
            <div class="flex items-center justify-between ">
              <div class="c">
                <div class="">
                  <div class="flex gap-8 items-center mt-20">
                    
                    <div class="py-8 flex flex-col gap-6">
                      <PrimaryButton :text="`+ 5 Kw`" @click="counter.incKw" />
                      <DangerButton :text="`- 5 Kw`" @click="counter.decKw" />     
                    </div>

                    <SpeedRadial />

                    <div class="py-8 flex flex-col gap-6">
                      <PrimaryButton :text="`+ 10 Kw`" @click="counter.valueKw += 10" />
                      <DangerButton :text="`- 10 Kw`" @click="counter.valueKw -= 10" />     
                    </div>

                  </div>
                </div>
              </div>

              <div class="">
                <div class="">
                  <div class="flex gap-8 items-center mt-20">
                    
                    <div class="py-8 flex flex-col gap-6">
                      <PrimaryButton :text="`+ 5 Kw`" @click="counter.incKw" />
                      <DangerButton :text="`- 5 Kw`" @click="counter.decKw" />     
                    </div>

                    <SpeedRadial />

                    <div class="py-8 flex flex-col gap-6">
                      <PrimaryButton :text="`+ 10 Kw`" @click="counter.valueKw += 10" />
                      <DangerButton :text="`- 10 Kw`" @click="counter.valueKw -= 10" />     
                    </div>

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

