<template>
    <div class="surface-ground px-4 py-5 md:px-6 lg:px-8">
        <div class="grid">
            <div
                v-for="product in products"
                :key="product.id"
                class="col-12 md:col-6 lg:col-3">
                <div class="surface-card shadow-2 p-3 border-round" @click="selectProduct(product)">
                    <div class="flex justify-content-between mb-3">
                        <div>
                           
                            <div class="text-900 font-medium text-xl">
                                {{ product.name }}
                            </div>
                        </div>
                       <div>
                        <Image :src="getImageUrl(product)" width="150"></Image>
                       </div>
                    </div>
               
                    <span class="text-500">€ {{ product.price }}</span>
                </div>
            </div>
       
        </div>
    </div>
    <Dialog
        v-model:visible="visible"
        :draggable="false"
        modal
        :header="selectedItem.name"
        :style="{ width: '25rem' }">
        <span class="p-text-secondary block mb-5">
            {{ selectedItem.description }}
        </span>
        <img :src="imageUrl" class="max-h-80 m-auto"/>
        <span class="font-bold text-2xl text-900">
            {{ selectedItem.price }}€
        </span>
        <div v-for="detail in selectedItem.productDetails" :key="detail.id">
            <strong>{{ detail.name }}:</strong> {{ detail.value }}
        </div>

        <div></div>
        <div class="flex justify-content-end gap-2">
            <Button
                type="button"
                label="Schließen"
                severity="secondary"
                @click="visible = false"></Button>
            <Button
                type="button"
                label="In den Warenkorb"
                severity="primary"
                @click="addToCart"></Button>
        </div>
    </Dialog>
    
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



function addToCart() {
    add(selectedItem.value);
    //items.value.push(selectedItem.value)
    visible.value = false;
}

function reloadList() {
    Product.getList().then((result) => {
        products.value = result;
    });
}

onMounted( async () => {
    reloadList();

});

function selectProduct(product: Product) {
    selectedItem.value = product;
    console.log(product);
    visible.value = true;
}

const imageUrl = computed(() => {
    return __API_URL__ + "/uploads/" + selectedItem.value.imagePath;
})

function getImageUrl(product: Product) {
    return __API_URL__ + "/uploads/" + product.imagePath;
}
</script>