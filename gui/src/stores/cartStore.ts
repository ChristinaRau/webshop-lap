import { ref, computed, unref } from 'vue';
import { defineStore } from 'pinia';
import { Product } from '@/utils/classes/Product.js';

export const useCart = defineStore("cart", () => {
    const items = ref<Product[]>([]);

    function add(item: Product) {
        console.log(item)
        console.log(items.value)
        items.value.push(item);
    }

    const size = computed(() => {
        return items.value.length;
    })

    return { items, add, size }
})