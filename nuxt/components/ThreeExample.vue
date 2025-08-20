<script setup>
import { Scene, PerspectiveCamera, WebGLRenderer, AmbientLight, DirectionalLight, Box3, Vector3 } from 'three'
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'

let renderer
const experience = ref(null)

const scene = new Scene()

// свет
const ambient = new AmbientLight(0xffffff, 1)
scene.add(ambient)

const dirLight = new DirectionalLight(0xffffff, 1)
dirLight.position.set(5, 10, 7.5)
scene.add(dirLight)

// камера
const camera = new PerspectiveCamera(45, 1, 0.1, 1000)
camera.position.set(0, 0, 4)
scene.add(camera)

// загрузка модели
const gltfLoader = new GLTFLoader()
gltfLoader.load('/PotPlant.glb', (gltf) => {
  const model = gltf.scene

  // нормализация размера в 250×250
  const box = new Box3().setFromObject(model)
  const size = new Vector3()
  box.getSize(size)
  const maxDim = Math.max(size.x, size.y, size.z)
  const scale = 2.5 / maxDim // коэффициент подгонки
  model.scale.setScalar(scale)

  // центрирование
  const center = box.getCenter(new Vector3())
  model.position.sub(center.multiplyScalar(scale))

  scene.add(model)
})

function updateRenderer() {
  renderer.setSize(250, 250)
  renderer.render(scene, camera)
}

function setRenderer() {
  if (experience.value) {
    renderer = new WebGLRenderer({ canvas: experience.value, alpha: true, antialias: true })
    renderer.setClearColor(0x000000, 0) // прозрачный фон
    updateRenderer()
  }
}

onMounted(() => {
  setRenderer()
  loop()
})

const loop = () => {
  updateRenderer()
  requestAnimationFrame(loop)
}
</script>

<template>
  <div class="flex items-center justify-center">
    <div class="w-[250px] h-[250px]">
      <canvas ref="experience" />
    </div>
  </div>
</template>
