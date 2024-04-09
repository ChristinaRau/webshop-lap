<template>
    <div class="surface-ground px-4 py-5 md:px-6 lg:px-8">
        <h2 class="text-2xl font-bold text-gray-900  sm:text-3xl pb-5">Warenkorb</h2>

        <div class="grid">
            <div
                v-for="product in items"
                :key="product.id"
                class="col-12 md:col-6 lg:col-3">
                <div class="surface-card shadow-2 p-3 border-round">
                    <div class="flex justify-content-between mb-3">
                        <div>
                           
                            <div class="text-900 font-medium text-l">
                                {{ product.name }}
                            </div>
                        </div>
                        <div>
                            <Image :src="getImageUrl(product)" width="50"></Image>
                        </div>
                    </div>
               
                    <span class="text-500">€ {{ product.price }}</span>
                </div>
            </div>
            
        </div>

        <Button>Bestellen</Button>
    </div>
   
    
</template>
<script setup lang="ts">
import { computed, onMounted, reactive, ref } from 'vue';
import { Product } from '@/utils/classes/Product';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import Image from 'primevue/image';
import { useCart } from '../stores/cartStore';
const products = ref<Product[]>([]);
const selectedItem = ref<Product>(new Product("", 0, 0, 0, ""));
const visible = ref(false);
const { items, size, add } = useCart();





const imageUrl = computed(() => {
    return __API_URL__ + "/uploads/" + selectedItem.value.imagePath;
});

function getImageUrl(product: Product) {
    return __API_URL__ + "/uploads/" + product.imagePath;
}
</script>