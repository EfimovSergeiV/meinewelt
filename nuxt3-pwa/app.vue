<template>
  <div>
    <VitePwaManifest />    
    <NuxtRouteAnnouncer />

    <NuxtLayout>
      <NuxtLoadingIndicator :color="'repeating-linear-gradient(to right,#38bdf8 0% ,#0369a1 100%)'" :height="1" />
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
