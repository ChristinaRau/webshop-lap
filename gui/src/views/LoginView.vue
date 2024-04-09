<template>

    
<div class="surface-card p-4 shadow-2 border-round w-full lg:w-6">
    <div class="text-center mb-5">
       
        <div class="text-900 text-3xl font-medium mb-3">Welcome Back</div>
        <span class="text-600 font-medium line-height-3">Don't have an account?</span>
        <a class="font-medium no-underline ml-2 text-blue-500 cursor-pointer">Create today!</a>
    </div>

    <div>
        <form id="login-form">
        <label for="username" class="block text-900 font-medium mb-2">Username</label>
        <InputText 
        id="username" type="text" class="w-full mb-3" 
        :pt="{autocomplete: 'username'}"
        v-model="credentials.username"
        />

        <label for="password1" class="block text-900 font-medium mb-2">Password</label>
        <InputText 
        id="password1" type="password" class="w-full mb-3"
        v-model="credentials.password" />

        <div class="flex align-items-center justify-content-between mb-6">
            <div class="flex align-items-center">
                <Checkbox id="rememberme1" :binary="true" v-model="checked" class="mr-2"></Checkbox>
                <label for="rememberme1">Remember me</label>
            </div>
            <a class="font-medium no-underline ml-2 text-blue-500 text-right cursor-pointer">Forgot password?</a>
        </div>

        <Button @click="tryLogin" label="Sign In" icon="pi pi-user" class="w-full"></Button>
        <span>{{ loginMessage }}</span>
    </form>
    </div>
</div>
</template>
<script setup lang="ts">
import { reactive, ref } from 'vue';
import InputText from 'primevue/inputtext';
import Checkbox from 'primevue/checkbox';
import Button from 'primevue/button';
import { login } from '@/utils/Authentication';

import { useRouter } from 'vue-router';

const checked = ref(true);
const loginMessage = ref("");
const credentials = reactive({
    username: "",
    password: ""
})

const router = useRouter()

function tryLogin() {
    login(credentials.username, credentials.password).then((success: boolean) => {
        if (success)
            router.push({name: "adminpanel"})
        else
            loginMessage.value = "Wrong password!";
    })
}
</script>   