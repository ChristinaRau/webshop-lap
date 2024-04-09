import { ref, computed, unref } from 'vue';
import { defineStore } from 'pinia';

export const useCart = defineStore("cart", () => {
    const items = ref([]);
    const count = ref(0);

    function add(item) {
        console.log(item)
        console.log(items.value)
        items.value.push(item);
        count.value ++;
    }

    const size = computed(() => {
        console.log(items)
        console.log(items.value)
        console.log(items.value.length)
        console.log(items.value.value)
        console.log(unref(items.value))
        console.log(unref(items.value).length)
        return items.value.length;
    })

    return { items, add, size, count }
})