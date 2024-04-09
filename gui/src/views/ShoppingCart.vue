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

        <Button @click="showOrderDialog = true">Bestellen</Button>
    </div>
    <Dialog
        modal
        :visible="showOrderDialog"
        header="Bestellung aufgeben"
        :draggable="false"
    >
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="font-semibold w-6rem">Name</label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newComputer.name"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Must not be empty.
                </small>
            </div>
        </div>
        
        <div class="flex align-items-center gap-3 mb-5">
            <label for="desc" class="font-semibold w-6rem">Description</label>
            <InputText
                id="desc"
                v-model="newComputer.description"
                class="flex-auto"
                autocomplete="off" />
        </div>

        <div class="flex align-items-center gap-3 mb-5">
            <label for="desc" class="font-semibold w-6rem">Processor</label>
            <div class="flex flex-col grow">
                <InputText
                    id="desc"
                    v-model="newComputer.processor"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.processor.length == 0" />
                <small v-show="checkInputValid && newComputer.processor.length == 0">
                    Must not be empty.
                </small>
            </div>
        </div>

        <div class="flex align-items-center gap-3 mb-5">
            <label for="desc" class="font-semibold w-6rem">Storage</label>
            <InputNumber
                id="desc"
                v-model="newComputer.storageGigabyte"
                class="flex-auto"
                autocomplete="off" 
                show-buttons
                :step="100"
                :min="0"/>
            GB
        </div>

        <div class="flex align-items-center gap-3 mb-5">
            <label for="desc" class="font-semibold w-6rem">RAM</label>
            <InputNumber
                id="desc"
                v-model="newComputer.ramGigabyte"
                class="flex-auto"
                autocomplete="off"
                show-buttons
                :step="4"
                :min="0" />
            GB
        </div>

        <div class="flex align-items-center gap-3 mb-5">
            <label for="desc" class="font-semibold w-6rem">Price</label>
            <InputNumber
                id="desc"
                v-model="newComputer.price"
                class="flex-auto"
                autocomplete="off"
                show-buttons
                :step="100"
                :min="0"
                mode="currency"
                currency="EUR"
            />
            
        </div>

        <div class="flex align-items-center gap-3 mb-5">
            <label for="desc" class="font-semibold w-6rem">Image</label>
            
            <FileUpload
                mode="basic"
                name="file"
                :url="uploadUrl"
                accept="image/*"
                :max-file-size="1000000"
                auto 
                @upload="onUpload"/>

            <img
                v-if="uploadedFileUrl != ''"
                :src="uploadedFileUrl"
                class="max-w-16 max-h-16"
            />
        </div>

        <div class="flex justify-content-end gap-2">
            <Button
                type="button"
                label="Cancel"
                severity="secondary"
                @click="showCreationDialog = false"></Button>
            <Button
                type="button"
                label="Save"
                @click="saveNewComputer"></Button>
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


const showOrderDialog = ref(false);


const imageUrl = computed(() => {
    return __API_URL__ + "/uploads/" + selectedItem.value.imagePath;
});

function getImageUrl(product: Product) {
    return __API_URL__ + "/uploads/" + product.imagePath;
}
</script>