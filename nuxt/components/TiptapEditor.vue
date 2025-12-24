<!-- eslint-disable vue/no-v-html -->
<template>
  <div>

    <div class="bg-gray-100 px-4 py-8 mt-4 rounded-md grid grid-cols-1 gap-1">
      <div v-if="editor" class="flex flex-wrap gap-1 rounded-sm border border-gray-300 px-0.5 py-0.5">
        <button
          class="bg-red-500 hover:bg-red-600 px-2 text-white rounded-sm"
          :disabled="!editor.can().chain().focus().undo().run()"
          @click="editor?.chain().focus().undo().run()"
        >
          назад
        </button>
        <button
          class="bg-red-500 hover:bg-red-600 px-2 text-white rounded-sm"
          :disabled="!editor.can().chain().focus().redo().run()"
          @click="editor?.chain().focus().redo().run()"
        >
          вперди
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('bold') }"
          :disabled="!editor.can().chain().focus().toggleBold().run()"
          @click="editor?.chain().focus().toggleBold().run()"
        >
          bold
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('italic') }"
          :disabled="!editor.can().chain().focus().toggleItalic().run()"
          @click="editor?.chain().focus().toggleItalic().run()"
        >
          italic
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('strike') }"
          :disabled="!editor.can().chain().focus().toggleStrike().run()"
          @click="editor?.chain().focus().toggleStrike().run()"
        >
          strike
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('code') }"
          :disabled="!editor.can().chain().focus().toggleCode().run()"
          @click="editor?.chain().focus().toggleCode().run()"
        >
          code
        </button>
        
        <button 
          class="bg-red-500 hover:bg-red-600 px-2 text-white rounded-sm"          
          @click="editor?.chain().focus().unsetAllMarks().run()">
          clear marks
        </button>
        <button
          class="bg-red-500 hover:bg-red-600 px-2 text-white rounded-sm"
          @click="editor?.chain().focus().clearNodes().run()">
          clear nodes
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('paragraph') }"
          @click="editor?.chain().focus().setParagraph().run()"
        >
          paragraph
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }"
          @click="editor?.chain().focus().toggleHeading({ level: 1 }).run()"
        >
          h1
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }"
          @click="editor?.chain().focus().toggleHeading({ level: 2 }).run()"
        >
          h2
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }"
          @click="editor?.chain().focus().toggleHeading({ level: 3 }).run()"
        >
          h3
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('heading', { level: 4 }) }"
          @click="editor?.chain().focus().toggleHeading({ level: 4 }).run()"
        >
          h4
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('heading', { level: 5 }) }"
          @click="editor?.chain().focus().toggleHeading({ level: 5 }).run()"
        >
          h5
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('heading', { level: 6 }) }"
          @click="editor?.chain().focus().toggleHeading({ level: 6 }).run()"
        >
          h6
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('bulletList') }"
          @click="editor?.chain().focus().toggleBulletList().run()"
        >
          bullet list
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('orderedList') }"
          @click="editor?.chain().focus().toggleOrderedList().run()"
        >
          ordered list
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('codeBlock') }"
          @click="editor?.chain().focus().toggleCodeBlock().run()"
        >
          code block
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          :class="{ 'is-active': editor.isActive('blockquote') }"
          @click="editor?.chain().focus().toggleBlockquote().run()"
        >
          blockquote
        </button>
        <button 
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          @click="editor?.chain().focus().setHorizontalRule().run()">
          horizontal rule
        </button>
        <button
          class="bg-blue-500 hover:bg-blue-600 px-2 text-white rounded-sm"
          @click="editor?.chain().focus().setHardBreak().run()">
          hard break
        </button>
      </div>

      <TiptapEditorContent :editor="editor" class="editor" />

    </div>



    <div class="mt-4">
      <p class="text-white text-sm">VIEW:</p>
      <div class="text-white rounded bg-gray-800/70 backdrop-blur-md border border-gray-600/70 p-2">
        <div v-html="editor?.getHTML()" />
      </div>
    </div>


    <div class="mt-4">
      <p class="text-white text-sm">JSON:</p>
      <pre class="text-white text-xs bg-gray-800/70 p-2 backdrop-blur-md border border-gray-600/70 rounded">
        {{ editor?.getJSON() }}
      </pre>
    </div>

    <div class="mt-4">
      <p class="text-white text-sm">HTML:</p>
      <pre class="text-white text-xs bg-gray-800/70 p-2 backdrop-blur-md border border-gray-600/70 rounded">
        <code>{{ editor?.getHTML() }}</code>
      </pre>
    </div>

    <p class="text-xs text-white mt-2">const = {{ json }}</p>
  
  </div>
</template>


<script setup>
import { onBeforeUnmount } from 'vue'
import StarterKit from '@tiptap/starter-kit'

const editor = useEditor({
  content: "<p>I'm running Tiptap with Vue.js. 🎉</p>",
  extensions: [StarterKit],
})

const json = computed(() => editor.value?.getJSON())

onBeforeUnmount(() => {
  editor.value?.destroy()
})
</script>


<style lang="css">
  .editor .ProseMirror {
    @apply 
    bg-gray-100
    text-gray-800
    border-gray-300
    pt-4 
    min-h-[200px] 
    outline-none
    rounded-sm
    border
    px-1
    py-0.5;
  }


</style>