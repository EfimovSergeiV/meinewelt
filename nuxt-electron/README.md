# Nuxt 3 + Electron пример

```zsh
# TMP: сетевой принтер DESKTOP-UULPIQ7
```

### Установка и сборка

```zsh
# Установка зависимостей, запуск dev 
npm install
npm run dev


# Building app
npm run build # AppImage for GNU/Linux
npx electron-builder --linux deb    # .deb for Debian's OS
npx electron-builder --win --x64    # .exe for Windows OS


# Чистка RC перед переустановкой в Linux
dpkg --list | grep "^rc"
dpkg --list | grep "^rc" | cut -d " " -f 3 | sudo xargs dpkg --purge

```

### Процесс установки зависимостей

```zsh
# TailwindCSS
npm install --save-dev @nuxtjs/tailwindcss
npx tailwindcss-cli init


# Charts
npm i vue-chartjs chart.js




```