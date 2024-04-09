

<template>
 
    <Menubar :model="menuItems">
        <template #end>
            <div class="flex align-items-center gap-2 w-10">
                <RouterLink :to="{name: 'shoppingcart'}">Warenkorb</RouterLink>
            </div>
        </template>
    </Menubar>
    
 
    <RouterView />
</template>
<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
import HelloWorld from './components/HelloWorld.vue';
import { useCart } from './stores/cartStore';
import Menubar from 'primevue/menubar';
import { type MenuItem } from 'primevue/menuitem';
import { ref } from 'vue';
import Dropdown, { type DropdownChangeEvent } from 'primevue/dropdown';
import { usePrimeVue } from 'primevue/config';

const PrimeVue = usePrimeVue();


const { items, add, size, count } = useCart();

const menuItems = ref<MenuItem[]>([
    {
        label: "Produkte",
        url: "/products"
    },
    {
        label: "Statistiken",
        url: "/stats"
    }   

]);

</script>
