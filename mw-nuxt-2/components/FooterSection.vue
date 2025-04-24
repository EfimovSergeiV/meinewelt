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
  <div class="text-gray-100 dark:text-gray-100">
    <div class="py-2 bottom-0">

      <div class="container mx-auto px-8">
        <div class="flex items-center justify-center gap-8 py-4">
          <div class="">
            <nuxt-link :to="{ name: 'index' }">Главная</nuxt-link>
          </div>
          <div class="">
            <nuxt-link :to="{ name: 'links' }">Блог</nuxt-link>
          </div>
          <div class="">
            <nuxt-link :to="{ name: 'links' }">Ссылки</nuxt-link>
          </div>
        </div>


      <ClientOnly>
        <div class="">
          <div class="grid grid-cols-1 gap-1 text-center text-xs text-gray-300/95 mb-0.5">
            <p class="">PWA Installed: {{ $pwa?.isPWAInstalled }} / Built Date: {{ date }}</p>
            <p class="">PWA state: {{ $pwa }}</p>
          </div>
        </div>

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
      </ClientOnly>
      <!-- <div v-show="$pwa.needRefresh"> -->


      <div>
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