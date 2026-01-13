<script setup>
  // eslint-disable-next-line no-unused-vars, vue/require-prop-types
  const props = defineProps(['skills',])
  
  
  // const skills = ref(
  //   [
  //     {
  //         "id": 1,
  //         "name": "GNU/Linux",
  //         "skill": true
  //     },
  //     {
  //         "id": 2,
  //         "name": "Debian",
  //         "skill": true
  //     },
  //     {
  //         "id": 3,
  //         "name": "Python",
  //         "skill": true
  //     },
  //     {
  //         "id": 4,
  //         "name": "Django",
  //         "skill": true
  //     },
  //     {
  //         "id": 5,
  //         "name": "FastAPI",
  //         "skill": true
  //     },
  //     {
  //         "id": 6,
  //         "name": "JavaScript",
  //         "skill": true
  //     },
  //     {
  //         "id": 7,
  //         "name": "VueJS",
  //         "skill": true
  //     },
  //     {
  //         "id": 8,
  //         "name": "NuxtJS",
  //         "skill": true
  //     },
  //     {
  //         "id": 9,
  //         "name": "TailwindCSS",
  //         "skill": true
  //     }
  //   ]
  // )

</script>

<template>
  <div class="flex flex-wrap gap-4 text-white dark:text-white">
    
    <div v-for="skill in skills" :key="skill.id" class="">
      <div class="bg-cyan-900/70 border border-cyan-500/50 rounded-full px-6 py-1">
        <p>{{ skill.name }}</p>
      </div>
    </div>

  </div>

</template>