import { ref, computed, unref } from 'vue';
import { defineStore } from 'pinia';
import { Product } from '@/utils/classes/Product.js';
import { OrderProduct } from '@/utils/classes/Order.js';

export const useCart = defineStore("cart", () => {
    const items = ref<Product[]>([]);

    function add(item: Product) {
        console.log(item);
        console.log(items.value);
        items.value.push(item);
    }

    const size = computed(() => {
        return items.value.length;
    });

    const createOrderProducts = async function(orderId: number) {
        for (let i = 0; i < items.value.length; i++) {
            console.log(items.value[i]);

            if (items.value[i].id !== undefined) {

                const orderProduct = new OrderProduct(
                    items.value[i].id,
                    orderId
                );
    
                await orderProduct.create().then((response) => {
                    return response.json();
                }).then((data) => {
                    console.log(data);
                });
            }
        }
    };

    const emptyArray = function() {
        const arraySize = items.value.length;

        // emptying the array without reassigning to [] because i don't want to lose the reference
        for (let i = 0; i < arraySize; i++) {
            items.value.pop();
        }
    }

    return { items, add, size, createOrderProducts, emptyArray };
});