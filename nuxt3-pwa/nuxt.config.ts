// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-04-13',
  devtools: { enabled: true },

  modules: [
    '@nuxt/icon',
    '@nuxt/image',
    '@vite-pwa/nuxt',
    "@nuxtjs/tailwindcss",
  ],

  pwa: {
    manifest: {
      name: "MeineWelt",
      short_name: "MeineWelt",
      theme_color:'#8a8a5e',
      description: "SE HomePage",
      icons: [
        {
          src: 'se.png',
          sizes: "150x150",
          type: "image/png"
        },
      ]
    },
    workbox: {
      navigateFallback: "/",

    },
    devOptions: {
      enabled: true, 
      type: "module"
    }
  },

  css: [
    '~/assets/css/tailwind.css',
    '~/assets/css/main.css',
    // '@mdi/font/css/materialdesignicons.min.css',
  ],

})