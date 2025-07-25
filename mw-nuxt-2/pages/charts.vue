<script setup lang="ts">
  import ChartSimple from '@/components/charts/ChartSimple.vue'
  import BubbleChart from '@/components/charts/BubbleChart.vue'
  import MultiAxisLineChart from '@/components/charts/MultiAxisLineChart.vue'


  const copyToClipboard = () => {
    const text = 'pnpm add vue-chartjs chart.js'

    navigator.clipboard.writeText(text)
      .then(() => {
        console.log('Скопировано в буфер обмена!')
        alert('Команда скопирована в буфер обмена!')
      })
      .catch((err) => {
        console.error('Ошибка копирования:', err)
      })
  }
</script>


<template>
  <div class="container mx-auto p-4">
    <div class="">
      <div class="mb-6 grid grid-cols-1 gap-2">
        <p class="text-white text-xl">Chart.js</p>
        <button class="flex mt-2" @click="copyToClipboard">
          <p class="text-white text-xs bg-gray-600 px-4 py-1 rounded-md">pnpm add vue-chartjs chart.js</p>
        </button>
        
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-6">
        <div class="bg-white px-4 py-2 rounded-lg shadow-md">
          <ChartSimple />
          <button class="mt-4 text-xs text-blue-600" @click="copyToClipboard">Скопировать код</button>
        </div>
        <div class="bg-white px-4 py-2 rounded-lg shadow-md">
          <BubbleChart />
          <button class="mt-4 text-xs text-blue-600" @click="copyToClipboard">Скопировать код</button>
        </div>
        <div class="bg-white px-4 py-2 rounded-lg shadow-md">
          <MultiAxisLineChart />
          <button class="mt-4 text-xs text-blue-600" @click="copyToClipboard">Скопировать код</button>
        </div>
      
      
      
      </div>
    </div>


  </div>
</template>