// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
  },
  
  modules: [
    '@nuxtjs/tailwindcss',
    ['@nuxtjs/color-mode', { classSuffix: '' }],
    '@tresjs/nuxt',
    '@pinia/nuxt',
    ['nuxt-electron', {
      build: [
        {
          // Main-Process entry file of the Electron App.
          entry: 'electron/main.ts',
        },
        {
          entry: 'electron/preload.ts',
          onstart(args: any) {
            // Notify the Renderer-Process to reload the page when the Preload-Scripts build is complete, 
            // instead of restarting the entire Electron App.
            args.reload()
          },
        },
      ],
      // Ployfill the Electron and Node.js API for Renderer process.
      // If you want use Node.js in Renderer process, the `nodeIntegration` needs to be enabled in the Main process.
      // See 👉 https://github.com/electron-vite/vite-plugin-electron-renderer
      renderer: {},
    }],
  ],

  css: [
    // '~/assets/css/tailwind.css',
    '~/assets/main.css',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  // colorMode config moved to modules array above

  ssr: false, // #43
})
