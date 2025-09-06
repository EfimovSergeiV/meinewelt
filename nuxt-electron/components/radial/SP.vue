<script setup lang="ts">
  import PrimaryButton from '../btn/PrimaryButton.vue'
  import DangerButton from '../btn/DangerButton.vue'

  import { Chart as ChartJS, ArcElement, Tooltip } from 'chart.js'
  import { Doughnut } from 'vue-chartjs'
  import { ref, computed } from 'vue'


ChartJS.register(ArcElement, Tooltip)

const speed = ref(0)
const maxSpeed = 180

const percent = computed(() => speed.value / maxSpeed * 100)

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
  <div>
    <div class="flex flex-col items-center relative">
      <!-- Круглый спидометр -->
      <Doughnut 
        :data="chartData" 
        :options="chartOptions" 
        class="w-[250px] h-[250px]" 
      />

      <!-- Значение скорости в центре -->
      <div 
        class="absolute top-1/2 left-1/2 
              -translate-x-1/2 -translate-y-1/2 
              text-xl font-bold"
      >
        {{ speed }} km/h
      </div>

    </div>


    <div class="flex justify-center gap-2 mt-4">
      <DangerButton @click="speed = Math.max(0, speed - 10)" :text="`-10`" />
      <PrimaryButton @click="speed = Math.min(maxSpeed, speed + 10)" :text="`+10`" />

    </div>
  </div>
</template>

