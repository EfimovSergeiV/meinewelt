<template>
  <div class="bg-gray-600">

    <div class="container px-4 mx-auto ">
      <div class="min-h-screen grid grid-cols-1 content-between">
        <AppHeader />
        <slot />
        <AppFooter />
      </div>
    </div>

  </div>

</template>