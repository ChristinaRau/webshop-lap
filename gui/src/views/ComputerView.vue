<template>
    <Button @click="showCreationDialog = true">Add</Button>
    <div class="surface-ground px-4 py-5 md:px-6 lg:px-8">
        <div class="grid">
            <div
                v-for="model in computerBaseModels"
                :key="model.id"
                class="col-12 md:col-6 lg:col-3">
                <div class="surface-card shadow-2 p-3 border-round" @click="selectComputerBaseModel(model)">
                    <div class="flex justify-content-between mb-3">
                        <div>
                            <span class="block text-500 font-medium mb-3">
                                PC
                            </span>
                            <div class="text-900 font-medium text-xl">
                                {{ model.name }}
                            </div>
                        </div>
                        <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width:2.5rem;height:2.5rem">
                            <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
                        </div>
                    </div>
               
                    <span class="text-500">{{ model.description }}</span>
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
        <img :src="imageUrl"/>
        <span class="font-bold text-2xl text-900">
            {{ selectedItem.price }}€
        </span>
        <div>{{ selectedItem.storageGigabyte + ' GB' }} Festplatte</div>
        <div>{{ selectedItem.ramGigabyte }} GB RAM</div>
        <div></div>
        <div class="flex justify-content-end gap-2">
            <Button
                type="button"
                label="Close"
                severity="secondary"
                @click="visible = false"></Button>
            <Button
                type="button"
                label="Add to cart"
                severity="primary"
                @click="addToCart"></Button>
        </div>
    </Dialog>
    <Dialog
        modal
        :visible="showCreationDialog"
        header="Add computer base model"
        :draggable="false"
        :closable="false"
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
import { ComputerBaseModel } from '@/utils/classes/ComputerBaseModel';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import { useCart } from '../stores/cartStore';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';
import FileUpload, { type FileUploadUploadEvent } from 'primevue/fileupload';
const computerBaseModels = ref<ComputerBaseModel[]>([]);
const selectedItem = ref<ComputerBaseModel>(new ComputerBaseModel("", 0, 0, 0, ""));
const visible = ref(false);
const host = import.meta.env.VITE_API_HOST;
const { items, size, add } = useCart();

const showCreationDialog = ref(false);
const checkInputValid = ref(false);
const uploadUrl = __API_URL__ + "/upload";
const uploadedFileUrl = ref("");
const newComputer = ref<ComputerBaseModel>(new ComputerBaseModel(
    "",
    0,
    0,
    0,
    ""
));

function addToCart() {
    add(selectedItem.value);
    //items.value.push(selectedItem.value)
    visible.value = false;
}

function reloadList() {
    ComputerBaseModel.getList().then((result) => {
        computerBaseModels.value = result;
    });
}

onMounted( async () => {
    reloadList();

});

function selectComputerBaseModel(baseModel: ComputerBaseModel) {
    selectedItem.value = baseModel;
    console.log(baseModel);
    visible.value = true;
}

function onUpload(event: FileUploadUploadEvent) {
    console.log("upload");
    console.log(event);
    uploadedFileUrl.value = JSON.parse(event.xhr.response).link;
    newComputer.value.imagePath = JSON.parse(event.xhr.response).filename;
}

function saveNewComputer() {
    checkInputValid.value = true;

    if (newComputer.value.isValid()) {
        newComputer.value.create().then((response) => {
            if (response.ok) {
                reloadList();
                showCreationDialog.value = false;
            }
        });      
    }
    
}

const imageUrl = computed(() => {
    return __API_URL__ + "/uploads/" + selectedItem.value.imagePath;
})
</script>