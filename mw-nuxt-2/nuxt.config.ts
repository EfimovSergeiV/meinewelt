import cfg from "./conf"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-06-18',
  devtools: { enabled: false },

  vite: {
    server: {
      allowedHosts: ['meinewelt.ru'],
    }
  },

  app: {
    head: {
      title: 'MEINEWELT.RU',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
      ],
      script: [
        {
          async: true,
          src: 'https://mc.yandex.ru/metrika/tag.js'
        },
        {
          hid: 'metrika-init',
          innerHTML: `
            window.ym = window.ym || function() {
              (window.ym.a = window.ym.a || []).push(arguments);
            };
            window.ym.l = +new Date();
            ym(101984567, "init", {
              clickmap:true,
              trackLinks:true,
              accurateTrackBounce:true,
              webvisor:true
            });
          `,
          type: 'text/javascript'
        }
      ],
      __dangerouslyDisableSanitizersByTagID: {
        'metrika-init': ['innerHTML']
      },
      noscript: [
        {
          children: `<div><img src="https://mc.yandex.ru/watch/30996406" style="position:absolute; left:-9999px;" alt="" /></div>`
        }
      ]
    },

    pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/scripts',
    '@vite-pwa/nuxt',
  ],
  css: [
    '~/assets/css/tailwind.css',
    '~/assets/css/main.css',
    // '@mdi/font/css/materialdesignicons.min.css',
  ],

  appConfig: {
    // you don't need to include this: only for testing purposes
    buildDate: new Date().toISOString(),
  },
  
  pwa: {
    mode: 'production',
    strategies: 'generateSW',
    registerType: 'autoUpdate',
    manifest: {
      name: 'MEINEWELT.RU',
      short_name: 'MEINEWELT',
      theme_color: '#ffffff',
    },
    pwaAssets: {
      config: true,
    },
    workbox: {
      globPatterns: ['**/*.{js,css,html,png,svg,ico}'],
    },
    client: {
      installPrompt: true,
    },
    devOptions: {
      enabled: true,
      suppressWarnings: true,
      navigateFallback: '/',
      navigateFallbackAllowlist: [/^\/$/],
    },
  },

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || cfg.BASE_URL,
    },
  },
})