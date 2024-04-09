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
        :closable="false"
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
                    v-model="customer.billingAddress.firstName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && fieldIsInvalid(customer.billingAddress.firstName)"/>
                <small v-show="checkInputValid && fieldIsInvalid(customer.billingAddress.firstName)">
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
                    v-model="customer.billingAddress.lastName"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && customer.billingAddress.lastName"/>
                <small v-show="checkInputValid && customer.billingAddress.lastName">
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
                    v-model="customer.billingAddress.street"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && customer.billingAddress.street"/>
                <small v-show="checkInputValid && customer.billingAddress.street">
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
                    v-model="customer.billingAddress.houseNumber"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && customer.billingAddress.houseNumber"/>
                <small v-show="checkInputValid && customer.billingAddress.houseNumber">
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
                    v-model="customer.billingAddress.zipCode"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && customer.billingAddress.zipCode"/>
                <small v-show="checkInputValid && customer.billingAddress.zipCode">
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
                    v-model="customer.billingAddress.city"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && customer.billingAddress.city"/>
                <small v-show="checkInputValid && customer.billingAddress.city">
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
                    v-model="customer.billingAddress.country"
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
                    v-model="customer.emailAddress"
                    class="flex-auto"
                    autocomplete="off"
                    :invalid="checkInputValid && fieldIsInvalid(customer.emailAddress)"/>
                <small v-show="checkInputValid && fieldIsInvalid(customer.emailAddress)">
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
                    v-model="customer.telNumber"
                    class="flex-auto"
                    autocomplete="off"/>
               
            </div>
        </div>
        <div>
            <input
                id="bothAddressesAreEqual"
                v-model="bothAddressesAreEqual"
                type="checkbox"
                @change="copyBillingAddressToShippingAddress">
        
            <label for="bothAddressesAreEqual">Lieferadresse entspricht Rechnungsadresse</label>
        </div>
        <div v-if="!bothAddressesAreEqual">
            <div class=" font-bold text-gray-900 mt-2  mb-4">Lieferadresse</div>
            <div class="flex align-items-center gap-3 mb-3">
                <label for="name" class=" w-10rem">
                    Vorname<span class="text-pink-500">*</span>
                </label>
                <div class="flex flex-col grow">

                    <InputText
                        id="name"
                        v-model="order.deliveryAddress.firstName"
                        class="flex-auto"
                        autocomplete="off"
                        :invalid="checkInputValid && fieldIsInvalid(order.deliveryAddress.firstName)"/>
                    <small v-show="checkInputValid && fieldIsInvalid(order.deliveryAddress.firstName)">
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
                        v-model="order.deliveryAddress.lastName"
                        class="flex-auto"
                        autocomplete="off"
                        :invalid="checkInputValid && fieldIsInvalid(order.deliveryAddress.lastName)"/>
                    <small v-show="checkInputValid && fieldIsInvalid(order.deliveryAddress.lastName)">
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
                        v-model="order.deliveryAddress.street"
                        class="flex-auto"
                        autocomplete="off"
                        :invalid="checkInputValid && fieldIsInvalid(order.deliveryAddress.street)"/>
                    <small v-show="checkInputValid && fieldIsInvalid(order.deliveryAddress.street)">
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
                        v-model="order.deliveryAddress.houseNumber"
                        class="flex-auto"
                        autocomplete="off"
                        :invalid="checkInputValid && fieldIsInvalid(order.deliveryAddress.houseNumber)"/>
                    <small v-show="checkInputValid && fieldIsInvalid(order.deliveryAddress.houseNumber)">
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
                        v-model="order.deliveryAddress.zipCode"
                        class="flex-auto"
                        autocomplete="off"
                        :invalid="checkInputValid && fieldIsInvalid(order.deliveryAddress.zipCode)"/>
                    <small v-show="checkInputValid && fieldIsInvalid(order.deliveryAddress.zipCode)">
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
                        v-model="order.deliveryAddress.city"
                        class="flex-auto"
                        autocomplete="off"
                        :invalid="checkInputValid && fieldIsInvalid(order.deliveryAddress.city)"/>
                    <small v-show="checkInputValid && fieldIsInvalid(order.deliveryAddress.city)">
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
                        v-model="order.deliveryAddress.country"
                        class="flex-auto"
                        autocomplete="off"
                    ></InputText>
                </div>
            </div>
        </div>
        <div>
            <div class="flex align-items-center gap-3 mb-3">
                <label for="name" class="w-10rem">
                    Zahlungsart<span class="text-pink-500">*</span>
                </label>
                <div class="flex flex-col grow">

                    <Dropdown
                        v-model="order.paymentMethod"
                        :options="['Rechnung', 'Kreditkarte']"
                    ></Dropdown>
                    <small v-show="checkInputValid && order.paymentMethod != undefined">
                        Feld darf nicht leer sein.
                    </small>
                </div>
            </div>
        </div>
        <div class="flex justify-content-end gap-2">
            <Button
                type="button"
                label="Abbrechen"
                severity="secondary"
                @click="showOrderDialog = false"></Button>
            <Button
                type="button"
                label="Bestellen"
                @click="saveOrder"></Button>
        </div>
    </Dialog>
    <Dialog
        :visible="showBillingDialog"
        :draggable="false"
        :closable="false">

        <div class="text-xl font-bold text-gray-900  pb-5">Danke für Ihren Einkauf.</div>
        <div class="text-md font-bold text-gray-900  pb-5">Produkte:</div>
        <div
            v-for="orderProduct in billingInfo.order_products"
            :key="orderProduct.id"
            class="flex justify-between">
            <span>{{ orderProduct.product.name }}</span>
            <span>{{ orderProduct.product.price }}€</span>
        </div>
        <div class="flex justify-between border-t-2">
            <span>Gesamter Betrag:</span> 
            <span>{{ productPricesSum }}€</span>
        </div>
        <!-- <div class="flex justify-between border-t-2">
            <span>Zahlungsart:</span> 
            <span>{{ orderProduct.order.paymentMethod }}€</span>
        </div> -->
        <div class="pt-5 pb-5">
            Die Rechnung wurde an Ihre E-Mail-Adresse versendet.
        </div>
        <Button
            type="button"
            label="Schließen"
            severity="secondary"
            @click="showBillingDialog = false"></Button>
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
import { Order, OrderProduct } from '@/utils/classes/Order';
import {getBillingInformation} from '@/utils/Billing';
const products = ref<Product[]>([]);
const selectedItem = ref<Product>(new Product("", 0, 0, 0, ""));
const visible = ref(false);

// the shopping cart pinia store (stores all products where the user clicked "add to cart" in "items")
const { items, size, add, createOrderProducts, emptyArray } = useCart();

const billingAddress = new Address("", "", "", "", "", "");
let deliveryAddress = new Address("", "", "", "", "", "");

const bothAddressesAreEqual = ref<boolean>(true);

// toggle visibility of order dialog (where the user can fill out his address etc)
const showOrderDialog = ref(false);

const customer = ref<Customer>(new Customer(
    "", 
    "", 
    billingAddress,
    
    
));

const order = ref<Order>( new Order(
    deliveryAddress, 
    "", // payment method
    customer.value, 
    "", // timestamp
    [], // orderProducts
)
);

// marks fields as invalid if they are invalid (empty)
const checkInputValid = ref(false);

function copyBillingAddressToShippingAddress() {
    if (bothAddressesAreEqual.value) {
        deliveryAddress = billingAddress;
    }
}

async function saveOrder() {
    // check if all required fields are filled
    checkInputValid.value = true;

    // create billing address
    await customer.value.billingAddress.create().then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        customer.value.billingAddressId = data.id;
    });

    // create the customer
    await customer.value.create().then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        // customer.value.id = data.id;
        order.value.customerId = data.id;
    });

    if (bothAddressesAreEqual.value) {
        order.value.deliveryAddressId = customer.value.billingAddressId;
    }
    // create delivery address
    else {
        order.value.deliveryAddress.create().then((response) => {
            return response.json();
        }).then((data) => {
            console.log(data);
            order.value.deliveryAddressId = data.id;
        });
    }

    // set order datetime to now
    order.value.dateOrdered = new Date().toISOString().replace("T", " ");

    // create the order
    await order.value.create().then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        order.value.id = data.id;
    });

    console.log(items);

    await createOrderProducts(order.value.id);

    showOrderDialog.value = false;

    // after creating the order, it's time to empty the shopping cart
    emptyArray();


    await getBillingInformation(order.value.id).then((resp) => {
        return resp.json();
    }).then((data) => {
        console.log(data);
        billingInfo.value = data;
        //showOrderDialog.value = false;
        showBillingDialog.value = true;
    });
}

const imageUrl = computed(() => {
    return __API_URL__ + "/uploads/" + selectedItem.value.imagePath;
});

function getImageUrl(product: Product) {
    return __API_URL__ + "/uploads/" + product.imagePath;
}

function fieldIsInvalid(field) {
    console.log(field);
    console.log(field.value);
    return field.value == undefined || field.value.length == 0;
}


// SHOW BILLING

const showBillingDialog = ref(false);
const billingInfo = ref();

const productPricesSum = computed(() => {
    let sum = 0;
    billingInfo.value.order_products.forEach((orderProduct) => {
        sum += orderProduct.product.price;
    });

    // need to round it because JS does weird things when calculating and you won't get the exact number
    return Math.round(sum * 100) / 100;
});

</script>