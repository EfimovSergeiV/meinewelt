<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const messages = ref([])
const input = ref('')
const isGenerating = ref(false)

let socket = null

function connectSocket() {
  socket = new WebSocket('ws://localhost:8000/ws/chat')

  socket.onopen = () => {
    console.log('WebSocket connected')
  }

  socket.onmessage = (event) => {
    const data = event.data

    if (data === '[[END]]') {
      isGenerating.value = false
      return
    }

    const last = messages.value[messages.value.length - 1]

    if (!last || last.role !== 'assistant') {
      messages.value.push({
        role: 'assistant',
        content: data,
      })
    } else {
      last.content += data
    }
  }

  socket.onclose = () => {
    console.log('WebSocket disconnected')
  }

  socket.onerror = (err) => {
    console.error('WebSocket error', err)
  }
}

function sendMessage() {
  if (
    !input.value.trim() ||
    !socket ||
    socket.readyState !== WebSocket.OPEN ||
    isGenerating.value
  ) {
    return
  }

  const text = input.value.trim()

  messages.value.push({
    role: 'user',
    content: text,
  })

  messages.value.push({
    role: 'assistant',
    content: '',
  })

  socket.send(text)
  input.value = ''
  isGenerating.value = true
}

onMounted(() => {
  connectSocket()
})

onBeforeUnmount(() => {
  if (socket) {
    socket.close()
  }
})
</script>

<template>
  <div class="min-h-screen  text-white p-6">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-3xl font-bold mb-6">Агент</h1>

      <div class="bg-zinc-900 rounded-2xl p-4 h-[70vh] overflow-y-auto mb-4 space-y-4 border border-zinc-800">
        <div
          v-for="(msg, i) in messages"
          :key="i"
          class="whitespace-pre-wrap"
          :class="msg.role === 'user' ? 'text-blue-300' : 'text-zinc-100'"
        >
          <span class="font-bold">
            {{ msg.role === 'user' ? 'Ты:' : 'Агент:' }}
          </span>
          {{ msg.content }}
        </div>
      </div>

      <div class="flex gap-2">
        <input
          v-model="input"
          type="text"
          placeholder="Пиши свою херню..."
          class="flex-1 rounded-xl bg-zinc-800 border border-zinc-700 px-4 py-3 outline-none"
          @keydown.enter="sendMessage"
        >
        <button
          class="px-5 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 transition"
          @click="sendMessage"
        >
          Отправить
        </button>
      </div>
    </div>
  </div>
</template>
