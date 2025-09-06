export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0,
    valueKw: 0
  }),
  actions: {
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    },
    incKw() {
      this.valueKw += 5
    },
    decKw() {
      this.valueKw -= 5
    }
  }
})