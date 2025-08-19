<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

// const wsUrl = "ws://127.0.0.1:8000/chat";
const wsUrl = "wss://api.meinewelt.ru/chat";

const messages = ref([]); // массив сообщений [{text, time}]
const message = ref("");
let socket = null;

const connectWebSocket = () => {
  socket = new WebSocket(wsUrl);

  socket.onopen = () => {
    console.log("WebSocket соединение установлено");
  };

  socket.onmessage = (event) => {

    try {
      const data = JSON.parse(event.data); // [{text, time}, ...]
      messages.value = data;
    } catch (e) {
      console.error("Ошибка парсинга:", e);
    }
  };

  socket.onclose = () => {
    console.log("WebSocket закрыт, переподключение...");
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
  <div class="">
    <div class="flex items-center justify-center">

    <div class="grid grid-cols-1 gap-4">

      <!-- Список сообщений -->
       <div class="">
        <div class="rounded-lg shadow-inner mb-4 grid grid-cols-1 gap-2">
          

          <div v-for="(msg, i) in messages" :key="i" class="">
            <!-- проверяем кратность двум -->
             <div v-if="i % 2 === 0" class="flex justify-end">
              <div class="mb-2 p-2 rounded-lg bg-blue-100/50 w-[500px]">
                <div class="text-sm text-gray-300">{{ msg.time }}</div>
                <div class="text-white">{{ msg.text }}</div>
              </div>                 
             </div>
             <div v-else>
              <div class="mb-2 p-2 rounded-lg bg-green-100/50 w-[500px]">
                <div class="text-sm text-gray-300">{{ msg.time }}</div>
                <div class="text-white">{{ msg.text }}</div>
              </div>
             </div>
          </div>




        </div>        
       </div>


      <!-- Поле ввода -->
      <div class=" ">
        <div>
          <textarea
            v-model="message"
            rows="3"
            class="px-4 py-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 w-full md:w-[600px] bg-white/60"
            placeholder="Напишите сообщение..."
            @keydown.enter.exact.prevent="sendMessage"
          />    
        </div>
        <div>
          <button
            class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            @click="sendMessage"
          >
            Отправить
          </button>          
        </div>


      </div>

    </div>


    </div>

  </div>
</template>
