// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-04-13',
  devtools: { enabled: true },

  app: {
    head: {
      title: 'Главный сварщик',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        // { 
        //   hid: 'description', 
        //   name: 'description', 
        //   content: 'Купить высококачественное сварочное оборудование. Мы являемся официальным дистрибьютором ведущих брендов. Большой выбор, гарантия качества.' 
        // },
        // { 
        //   hid: 'keywords', 
        //   name: 'keywords', 
        //   content: 'сварочное оборудование, оборудование для сварки, купить электроды, купить проволоку, купить источник, купить сварочный инвертор' 
        // },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ],
    },

    pageTransition: { 
      name: 'page', 
      mode: 'out-in' 
    },

  },

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