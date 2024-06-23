<script setup>

  const { data: test } = await useFetch(`https://api.glsvar.ru/c/prods/?brnd=3`)


</script>


<template>
  <div class=" py-4">

    <FromAuthor />


  </div>
</template>