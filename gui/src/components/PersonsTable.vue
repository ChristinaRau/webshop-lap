<template>
<Button label="Add person" @click="dialogVisible = true" />

    <DataTable :value="personList" tableStyle="min-width: 50rem">
    <Column field="id" header="Id"></Column>
    <Column field="first_name" header="Vorname"></Column>
    <Column field="last_name" header="Nachname"></Column>
</DataTable>



<Dialog v-model:visible="dialogVisible" modal header="Add person" :style="{ width: '25rem' }">
    <!-- span class="p-text-secondary block mb-5">Update your information.</span -->
    <div class="flex align-items-center gap-3 mb-3">
        <label for="username" class="font-semibold w-6rem">First name</label>
        <InputText v-model="newPerson.firstName" id="firstName" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex align-items-center gap-3 mb-5">
        <label for="email" class="font-semibold w-6rem">Last name</label>
        <InputText v-model="newPerson.lastName" id="lastName" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex justify-content-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="dialogVisible = false"></Button>
        <Button type="button" label="Save" @click="onCreatePerson"></Button>
    </div>
</Dialog>



</template>
<script setup lang="ts">
import { getPersonList } from '../utils/GetCalls';
import { ref, onMounted } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column'
import Button from 'primevue/button'

import Dialog from 'primevue/dialog'

import InputText from 'primevue/inputtext'
import { Person, createPerson } from '../utils/Person'

const dialogVisible = ref(false);

const personList = ref([]);

const newPerson = ref(new Person("", ""))

async function onCreatePerson() {
    const resp = await createPerson(newPerson.value);
    console.log(resp)

    if (resp.ok) {
        // reload person list 
        personList.value = await getPersonList();
        dialogVisible.value = false;
    }
}

onMounted(async () => {
    personList.value = await getPersonList();
})
</script>