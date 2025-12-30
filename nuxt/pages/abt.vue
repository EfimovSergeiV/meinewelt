<template>
  <ClientOnly>
    <section
      v-gsap.timeline.pinned="{
        scrollTrigger: {
          start: 'top top',
          end: '+=200%',
          scrub: true
        }
      }"
      class="relative h-[200vh] flex flex-col items-center justify-center overflow-hidden bg-black text-white"
    >
      <div
        v-gsap.add.to="{ width: '800px', duration: 1, ease: 'power2.out' }"
        class="Dot bg-indigo-500 w-32 h-32 rounded-full mb-12"
      />

      <p
        v-gsap.add.fromTo="[
          { opacity: 0, y: 32 },
          { opacity: 1, y: 0, duration: 1, ease: 'power2.out' }
        ]"
        v-gsap.add.to="{ opacity: 0, y: -32, duration: 1, ease: 'power2.inOut', delay: 0.5 }"
        class="text-6xl font-bold mb-4"
      >
        New era of
      </p>

      <p
        v-gsap.add.withPrevious.fromTo="[
          { opacity: 0, y: 32 },
          { opacity: 1, y: 0, duration: 1, ease: 'power2.out' }
        ]"
        v-gsap.add.to="{ opacity: 0, y: -32, duration: 1, ease: 'power2.inOut', delay: 0.5 }"
        class="text-6xl font-bold"
      >
        animation
      </p>
    </section>
  </ClientOnly>
</template>
