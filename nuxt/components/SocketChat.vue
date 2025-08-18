<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const wsUrl = "ws://127.0.0.1:8000/chat";

const messages = ref([]); // массив сообщений [{text, time}]
const message = ref("");
let socket = null;

const connectWebSocket = () => {
  socket = new WebSocket(wsUrl);

  socket.onopen = () => {
    console.log("✅ WebSocket соединение установлено");
  };

  socket.onmessage = (event) => {
    console.log("📩 Получено сообщение:", event.data);
    try {
      const data = JSON.parse(event.data); // [{text, time}, ...]
      messages.value = data;
    } catch (e) {
      console.error("Ошибка парсинга:", e);
    }
  };

  socket.onclose = () => {
    console.log("⚠️ WebSocket закрыт, переподключение...");
    setTimeout(connectWebSocket, 1000);
  };
};

const sendMessage = () => {
  if (socket && socket.readyState === WebSocket.OPEN && message.value.trim()) {
    socket.send(message.value);
    message.value = "";
  }
};

onMounted(() => connectWebSocket());
onBeforeUnmount(() => socket?.close());
</script>

<template>
  <div class="max-w-xl mx-auto p-6 bg-gray-100 rounded-xl shadow">
    <h2 class="text-xl font-bold mb-4">💬 Чат</h2>

    <!-- Список сообщений -->
    <div class="h-64 overflow-y-auto bg-white p-4 rounded-lg shadow-inner mb-4">
      <div
        v-for="(msg, i) in messages"
        :key="i"
        class="mb-2 p-2 rounded-lg bg-blue-100"
      >
        <div class="text-sm text-gray-500">{{ msg.time }}</div>
        <div class="text-gray-800">{{ msg.text }}</div>
      </div>
    </div>

    <!-- Поле ввода -->
    <div class="flex gap-2">
      <textarea
        v-model="message"
        rows="2"
        class="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
        placeholder="Напишите сообщение..."
      />
      <button
        @click="sendMessage"
        class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
      >
        Отправить
      </button>
    </div>
  </div>
</template>
