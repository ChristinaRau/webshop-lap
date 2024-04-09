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
        <div class="mb-4">
            Die mit einem Stern(<span class="text-pink-500">*</span>) markierten Felder müssen ausgefüllt werden.
        </div>
        <div class=" font-bold text-gray-900 mt-2  mb-4">Rechnungsadresse</div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class=" w-10rem">
                Vorname<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.firstName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                Nachname<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                Straße<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                Hausnummer<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                PLZ<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                Ort<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                Land
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                ></InputText>
            </div>
        </div>
        <div class=" font-bold text-gray-900 mt-2  mb-4">Kontaktdaten</div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                E-Mail-Adresse<span class="text-pink-500">*</span>
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div class="flex align-items-center gap-3 mb-3">
            <label for="name" class="w-10rem">
                Telefonnummer
            </label>
            <div class="flex flex-col grow">

                <InputText
                    id="name"
                    v-model="newCustomer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && newComputer.name.length == 0"/>
                <small v-show="checkInputValid && newComputer.name.length == 0">
                    Feld darf nicht leer sein.
                </small>
            </div>
        </div>
        <div>
            <Checkbox
                v-model="bothAddressesAreEqual"
                class="mr-2"
                @change="copyBillingAddressToShippingAddress"
            ></Checkbox>
            <label for="bothAddressesAreEqual">Lieferadresse entspricht Rechnungsadresse</label>
        </div>
        <div>
            <div class="flex align-items-center gap-3 mb-3">
                <label for="name" class="w-10rem">
                    Zahlungsart<span class="text-pink-500">*</span>
                </label>
                <div class="flex flex-col grow">

                    <Dropdown
                        :options="['Rechnung', 'Kreditkarte']"
                    ></Dropdown>
                    <small v-show="checkInputValid && newComputer.name.length == 0">
                        Feld darf nicht leer sein.
                    </small>
                </div>
            </div>
        </div>
        <div class="flex justify-content-end gap-2">
            <Button
                type="button"
                label="Cancel"
                severity="secondary"
                @click="showOrderDialog = false"></Button>
            <Button
                type="button"
                label="Save"
                @click="saveOrder"></Button>
        </div>
    </Dialog>
    
</template>
<script setup lang="ts">
import { computed, onMounted, reactive, ref } from 'vue';
import { Product } from '@/utils/classes/Product';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import Image from 'primevue/image';
import InputText from 'primevue/inputtext';
import Checkbox from 'primevue/checkbox';
import Dropdown from 'primevue/dropdown';
import { useCart } from '../stores/cartStore';
import { Customer, Address } from '@/utils/classes/Customer';
const products = ref<Product[]>([]);
const selectedItem = ref<Product>(new Product("", 0, 0, 0, ""));
const visible = ref(false);
const { items, size, add } = useCart();

const bothAddressesAreEqual = ref(false);

const showOrderDialog = ref(false);

const newCustomer = ref<Customer>(new Customer("", "", "", new Address("", "", "", "")));
const billingAddress = ref<Address>(new Address("", "", "", ""));

const deliveryAddress = ref<Address>(new Address("", "", "", ""));

function copyBillingAddressToShippingAddress() {
    if (bothAddressesAreEqual.value) {
        deliveryAddress.value = billingAddress.value;
    }
}

function saveOrder() {
    console.log(newCustomer.value);
    console.log(billingAddress.value);
    console.log(deliveryAddress.value);
}

const imageUrl = computed(() => {
    return __API_URL__ + "/uploads/" + selectedItem.value.imagePath;
});

function getImageUrl(product: Product) {
    return __API_URL__ + "/uploads/" + product.imagePath;
}
</script>