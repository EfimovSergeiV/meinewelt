<script setup>
  import BubbleChart from '~/components/charts/BubbleChart.vue'
  import ChartSimple from '~/components/charts/ChartSimple.vue'
  import MultiAxisLineChart from '~/components/charts/MultiAxisLineChart.vue'
  import ProgressiveLineChart from '~/components/charts/ProgressiveLineChart.vue'
  import WatchChart from './charts/WatchChart.vue'

</script>

<template>

  <div class="container mx-auto px-4">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-6">
      <div class="bg-white px-4 py-2 rounded-lg shadow-md">
        <ChartSimple />
      </div>
      <div class="bg-white px-4 py-2 rounded-lg shadow-md">
        <BubbleChart />
      </div>
      <div class="bg-white px-4 py-2 rounded-lg shadow-md">
        <MultiAxisLineChart />
      </div>
      <div class="bg-white px-4 py-2 rounded-lg shadow-md">
        <ProgressiveLineChart />
      </div>
      <div class="bg-white px-4 py-2 rounded-lg shadow-md">
        <WatchChart />
      </div>
    </div>
  </div>


</template>