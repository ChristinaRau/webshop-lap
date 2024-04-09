

<template>
 
    <Menubar :model="menuItems">
        <template #end>
            <div class="flex align-items-center gap-2 w-10">
                <Dropdown
                    class="w-20"
                    :options="themeOptions"
                    @change="onThemeSelection"

                />
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
        label: "Computers",
        url: "/computers"
    },
    {
        label: "Admin panel",
        url: "/admin_panel"
    },
    {
        label: "Login",
        url: "/login"
    }
]);

const themeOptions = ref([
    "lara-light-pink",
    "arya-purple",
    "aura-light-lime",
    "luna-pink",
    "mira",
    "nano"

]);

let currentTheme = "lara-light-pink";

function onThemeSelection(event: DropdownChangeEvent) {
    console.log(event.value);
    PrimeVue.changeTheme(currentTheme, event.value, "theme-link", () => {
        currentTheme = event.value;
    });
}

</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
