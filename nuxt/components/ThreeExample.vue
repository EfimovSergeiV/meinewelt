<script setup>
  import { TresCanvas, useLoader, useRenderLoop } from '@tresjs/core'
  import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'

  import { OrbitControls } from '@tresjs/cientos'
  import * as THREE from 'three'

  const { scene } = await useLoader(GLTFLoader, '/PotPlant.glb')

  const box = new THREE.Box3().setFromObject(scene)
  const center = box.getCenter(new THREE.Vector3())
  const size = box.getSize(new THREE.Vector3())
  scene.position.sub(center)

  const maxDim = Math.max(size.x, size.y, size.z)
  const fov = 45
  const cameraZ = maxDim / (2 * Math.tan((Math.PI * fov) / 360))

  useRenderLoop().onLoop(() => {
    scene.rotation.y += 0.002
  })
</script>

<template>
  <div class="flex items-center justify-center">
    <div class="w-[400px] h-[400px]">
      <ClientOnly>
        <TresCanvas alpha>
          <TresPerspectiveCamera :position="[0, 0, cameraZ * 2]" :fov="45" />
          <TresAmbientLight :intensity="0.8" />
          <TresDirectionalLight :position="[5, 10, 7.5]" :intensity="1" />

          <primitive :object="scene" />

          <OrbitControls />
        </TresCanvas>
      </ClientOnly>

    </div>


  </div>

</template>
