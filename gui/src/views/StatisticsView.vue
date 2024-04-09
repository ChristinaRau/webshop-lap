<template>
    <div class="pl-3">
        <div class="text-xl mt-5 pl-2">Die 5 meist verkauften Produkte</div>
        <DataTable 
            :value="statistics.top_products">
            <Column field="name" header="Name" />
            <Column field="order_product_count" header="Anzahl Bestellungen" />
        </DataTable>
        <div class="text-xl mt-5 pl-2">Die 5 am wenigsten verkauften Produkte</div>
        <DataTable 
            :value="statistics.worst_products">
            <Column field="name" header="Name" />
            <Column field="order_product_count" header="Anzahl Bestellungen" />
        </DataTable>
        <div class="text-xl mt-5 pl-2">Alle Bestellungen der letzten vier Wochen</div>
        <DataTable 
            :value="statistics.orders_last_weeks">
            <Column field="date_ordered" header="Datum" />
            <Column field="payment_method" header="Zahlungsmethode" />
            <Column field="product_count" header="Anzahl Produkte" />
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

    statistics.value.orders_last_weeks.forEach((order) => {
        order.product_count = order.order_products.length;
    });
});


</script>