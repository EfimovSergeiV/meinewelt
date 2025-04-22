<template>
  <div class="bg-fixed bg-no-repeat bg-cover bg-[url('bg/welt.webp')] dark:bg-[url('bg/welt.webp')] min-h-screen">
    
    
    <div class=" bg-gradient-to-br from-gray-800/80 via-gray-700/70 to-gray-900/80">
      <div class="container px-4 mx-auto ">
        <div class="min-h-screen grid grid-cols-1 content-between">
          <AppHeader />
          <slot />
          <AppFooter />
        </div>
      </div>

    </div>



  </div>

</template>