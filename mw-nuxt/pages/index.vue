<script setup>

  const { data: test } = await useFetch(`https://api.glsvar.ru/c/prods/?brnd=3`)



</script>


<template>
  <div class="py-4">
    <div class="grid grid-cols-1 gap-4">

      <div class="bg-gray-700/70 backdrop-blur-md border border-gray-500 px-4 py-4 rounded-2xl">
        
        <div class="flex pb-4">
          <p class="uppercase font-semibold italic text-2xl border-b border-white ">Проекты в сети:</p>

        </div>

        <div class="flex flex-wrap gap-x-8 gap-y-4">
          <div class="grid grid-cols-1 gap-0.5">
            <a href="https://glsvar.ru" target="_blank" class="uppercase italic font-semibold text-lg">glsvar.ru</a>
            <p class="text-sm">Магазин сварочного оборудования</p>
          </div>
          <div class="grid grid-cols-1 gap-0.5">
            <a href="https://glsvar.kz" target="_blank" class=" uppercase italic font-semibold text-lg">glsvar.kz</a>
            <p class="text-sm">Магазин сварочного оборудования в Казахстане</p>
          </div>
          <div class="grid grid-cols-1 gap-0.5">
            <a href="https://pskovshevron.ru" target="_blank" class="uppercase italic font-semibold text-lg">pskovshevron.ru</a>
            <p class="text-sm">2-страничник про шевроны</p>
          </div>
          <div class="grid grid-cols-1 gap-0.5">
            <a href="https://weldingeu.com" target="_blank" class="uppercase italic font-semibold text-lg">weldingeu.com</a>
            <p class="text-sm">Заглушка для сайта</p>
          </div>
          <div class="grid grid-cols-1 gap-0.5">
            <a href="https://api.glsvar.ru/getsubscriebe" target="_blank" class="uppercase italic font-semibold text-lg">/getsubscriebe</a>
            <p class="text-sm">Генератор подписи email</p>
          </div>
          
        </div>
      </div>

      <div class="bg-gray-700/70 backdrop-blur-md border border-gray-500 px-4 py-4 rounded-2xl">
        <p class="uppercase font-semibold italic text-sm md:text-2xl py-2">В разработке:</p>

        <div class="flex flex-wrap gap-8">
          <a href="https://wr.meinewelt.ru" target="_blank" class="text-center uppercase italic font-semibold text-lg">weldingrail.meinewelt.ru</a>
        </div>
      </div>

      <div class="bg-gray-700/70 backdrop-blur-md border border-gray-500 px-4 py-4 rounded-2xl">
        <p class="uppercase font-semibold italic text-sm md:text-2xl py-2">Остальное:</p>

        <div class="flex flex-wrap gap-8">
          <a href="" target="_blank" class="text-center uppercase italic font-semibold text-lg"></a>
        </div>
      </div>

      <FromAuthor />

    </div>
  </div>
</template>