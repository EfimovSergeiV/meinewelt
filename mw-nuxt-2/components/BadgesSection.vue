<script setup>

  const skillsList = [
    { id: 1, title: "GNU/Linux" },
    { id: 1, title: "Debian" },
    { id: 1, title: "Python" },
    { id: 1, title: "Django" },
    { id: 1, title: "FastAPI" },
    { id: 1, title: "JavaScript" },
    { id: 1, title: "Vue" },
    { id: 1, title: "NuxtJS" },
    { id: 1, title: "TaillwindCSS" },
  ]


</script>

<template>
  <div class="flex flex-wrap gap-4">
    <div v-for="skill in skillsList" :key="skill.id" class="">
      <div class="">
        <p>{{ skill.title }}</p>
      </div>
    </div>

  </div>

</template>