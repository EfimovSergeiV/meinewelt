<script setup>
// If you want to use it in setup, import from the nuxtApp.
const { $pwa } = useNuxtApp()
// const toast = useToast()

  onMounted(() => {
    if ($pwa.offlineReady)
      // toast.success('App ready to work offline')
     alert('App ready to work offline')
  })
</script>

<template>
  <div class="">
    
    <div class="flex gap-4">
      <div class="">
        <NuxtLink to="/" class="text-lg text-red-500">Home</NuxtLink>
      </div>
      <div class="">
        <NuxtLink to="/about" class="text-lg text-red-500">About</NuxtLink>
      </div>

    </div>

    <slot />

    <ClientOnly>
      PWA Installed: {{ $pwa }}
      PWA Installed: {{ $pwa?.isPWAInstalled }}
    </ClientOnly>
  
    
        <!-- <div v-show="$pwa.needRefresh"> -->
    <div>
      <div v-show="$pwa?.needRefresh">
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
      <div>
        <div
          v-if="$pwa?.offlineReady || $pwa?.needRefresh"
          class="pwa-toast"
          role="alert"
        >
          <div class="message">
            <span v-if="$pwa.offlineReady">
              App ready to work offline
            </span>
            <span v-else>
              New content available, click on reload button to update.
            </span>
          </div>
          <button
            v-if="$pwa?.needRefresh"
            @click="$pwa.updateServiceWorker()"
          >
            Reload
          </button>
          <button @click="$pwa.cancelPrompt()">
            Close
          </button>
        </div>
        <div
          v-if="$pwa?.showInstallPrompt && !$pwa?.offlineReady && !$pwa?.needRefresh"
          class="pwa-toast"
          role="alert"
        >
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
</template>