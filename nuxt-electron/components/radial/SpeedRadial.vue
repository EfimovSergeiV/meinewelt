<script setup lang="ts">
import { Chart as ChartJS, ArcElement, Tooltip } from 'chart.js'
import { Doughnut } from 'vue-chartjs'
import { ref, computed } from 'vue'

const counter = useCounterStore()

ChartJS.register(ArcElement, Tooltip)

const speed = ref(counter.valueKw)
const maxSpeed = 180

const percent = computed(() => counter.valueKw / maxSpeed * 100)

const chartData = computed(() => ({
  datasets: [
    {
      data: [percent.value, 100 - percent.value],
      backgroundColor: ['#155dfc', '#e5e7eb'],
      borderWidth: 0,
      circumference: 360, // полный круг
      rotation: 180,       // начало внизу
      cutout: '60%'
    }
  ]
}))

const chartOptions = {
  responsive: true,
  plugins: {
    tooltip: { enabled: false },
  }
}
</script>

<template>
  <div class="flex flex-col items-center relative select-none">
    <Doughnut :data="chartData" :options="chartOptions" class="w-[250px] h-[250px]" />
    <div class="text-white absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-2xl font-bold">{{ counter.valueKw }} Kw</div>

    <!-- <div class="flex gap-2 mt-4">
      <button @click="speed = Math.max(0, speed - 10)" class="px-3 py-1 border rounded">-10</button>
      <button @click="speed = Math.min(maxSpeed, speed + 10)" class="px-3 py-1 border rounded">+10</button>
    </div> -->
  </div>
</template>
