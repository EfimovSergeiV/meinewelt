<script setup>
  import ChartSimple from '@/components/charts/ChartSimple.vue'
  import BubbleChart from '@/components/charts/BubbleChart.vue'
  import MultiAxisLineChart from '@/components/charts/MultiAxisLineChart.vue'


  const copyToClipboardCMD = (cmd) => {
    navigator.clipboard.writeText(cmd)
      .then(() => {
        alert('Команда скопирована в буфер обмена!')
      })
      .catch(err => {
        console.error('Ошибка копирования:', err)
        alert('Не удалось скопировать команду')
      })
  }


  const copyToClipboard = async (filename) => {
    try {
      const res = await fetch(`https://raw.githubusercontent.com/EfimovSergeiV/meinewelt/main/mw-nuxt-2/${filename}.vue`)
      if (!res.ok) throw new Error('Файл не найден')
      const text = await res.text()

      await navigator.clipboard.writeText(text)
      alert('Код скопирован в буфер обмена!')
    } catch (err) {
      console.error('Ошибка копирования:', err)
      alert('Не удалось скопировать файл')
    }
  }
</script>


<template>
  <div class="container mx-auto p-4">
    <div class="">
      <div class="mb-6 grid grid-cols-1 gap-2">
        <p class="text-white text-xl">Chart.js</p>
        <button class="flex mt-2" @click="copyToClipboardCMD('pnpm add vue-chartjs chart.js')">
          <p class="text-white text-xs bg-gray-600 px-4 py-1 rounded-md">pnpm add vue-chartjs chart.js</p>
        </button>
        
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-6">
        <div class="bg-white px-4 py-2 rounded-lg shadow-md">
          <ChartSimple />
          <button class="mt-4 text-xs text-blue-600" @click="copyToClipboard('components/charts/ChartSimple')">Скопировать код</button>
        </div>
        <div class="bg-white px-4 py-2 rounded-lg shadow-md">
          <BubbleChart />
          <button class="mt-4 text-xs text-blue-600" @click="copyToClipboard('components/charts/BubbleChart')">Скопировать код</button>
        </div>
        <div class="bg-white px-4 py-2 rounded-lg shadow-md">
          <MultiAxisLineChart />
          <button class="mt-4 text-xs text-blue-600" @click="copyToClipboard('components/charts/MultiAxisLineChart')">Скопировать код</button>
        </div>
      
      
      
      </div>
    </div>


  </div>
</template>