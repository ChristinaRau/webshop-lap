<template>
    <div>
        <div class="text-xl">Die 5 meist verkauften Produkte</div>
        <DataTable 
            :value="statistics.top_products">
            <Column field="name" header="Name" />
        </DataTable>
        <div class="text-xl">Die 5 am wenigsten verkauften Produkte</div>
        <DataTable 
            :value="statistics.worst_products">
            <Column field="name" header="Name" />
        </DataTable>
    </div>
</template>
<script setup lang="ts">
import { ref } from "vue";
import DataTable from "primevue/datatable";
import Column from 'primevue/column';

import { getStatistics } from "@/utils/Statistics";

const statistics = ref();


getStatistics().then((response) => {
    return response.json();
}).then((data) => {
    console.log(data);
    statistics.value = data;
});


</script>