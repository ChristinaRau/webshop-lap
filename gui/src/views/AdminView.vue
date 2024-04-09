<template>
    Admin View
    <SelectButton v-model="optionValue" :options="options" aria-labelledby="basic" />
    <PersonsTable v-if="optionValue == 'Persons'" />
    <AwardsTable v-else-if="optionValue == 'Awards'" />
    <TeamsTable v-else-if="optionValue == 'Teams'" />
   
</template>
<script setup lang="ts">
import { getPersonList } from '../utils/GetCalls';
import { ref, onMounted } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column'
import SelectButton from 'primevue/selectbutton';
import PersonsTable from '../components/PersonsTable.vue'
import AwardsTable from '../components/AwardsTable.vue'
import TeamsTable from '../components/TeamsTable.vue';


const personList = ref([]);
const options = ["Persons", "Awards", "Teams"]
const optionValue = ref("Persons")


</script>