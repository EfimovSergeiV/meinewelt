<script setup>
  // If you want to use it in setup, import from the nuxtApp.
  const { $pwa } = useNuxtApp()
  const date = useAppConfig().buildDate
  // const toast = useToast()

  onMounted(() => {
    if ($pwa.offlineReady)
      // toast.success('App ready to work offline')
     alert('App ready to work offline')
  })
</script>


<template>
  <div class="">
    <div class="absolute w-screen left-0 bottom-0">

      <div class="container mx-auto ">
        <div class="flex items-center justify-center gap-8 py-4">
          <div class="">
            <nuxt-link :to="{ name: 'index' }">Главная</nuxt-link>
          </div>
          <div class="">
            <p>Блог</p>
          </div>
          <div class="">
            <nuxt-link :to="{ name: 'links' }">Ссылки</nuxt-link>
          </div>
        </div>



      <ClientOnly>
        PWA Installed: {{ $pwa }}
        PWA Installed: {{ $pwa?.isPWAInstalled }}
      </ClientOnly>
      <!-- <div v-show="$pwa.needRefresh"> -->


        <div>
          <div v-show="$pwa.needRefresh">
            {{ $pwa }}
            <span>
              New content available, click on reload button to update.
            </span>

            <button @click="$pwa?.updateServiceWorker()">
              Reload
            </button>
          </div>      
        </div>



      <div>
        <div>Built Date: {{ date }}</div>

        <div v-if="$pwa?.offlineReady || $pwa?.needRefresh" class="pwa-toast" role="alert">
          <div class="message">
            <span v-if="$pwa.offlineReady">
              App ready to work offline
            </span>
            <span v-else>
              New content available, click on reload button to update.
            </span>
          </div>
            <button
              v-if="$pwa.needRefresh"
              @click="$pwa.updateServiceWorker()"
            >
              Reload
            </button>
            <button @click="$pwa.cancelPrompt()">
              Close
            </button>




            <div v-if="$pwa?.showInstallPrompt && !$pwa?.offlineReady && !$pwa?.needRefresh" class="pwa-toast" role="alert">
              <div class="message">
                <span>
                  Install PWA
                </span>
              </div>
              
              <button @click="$pwa.install()">
                Install
              </button>
              <button @click="$pwa.cancelInstall()">
                Cancel
              </button>
            </div>

          </div>
        </div>


      </div>
    </div>

  </div>
</template>