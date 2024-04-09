<template>
    <Button label="Add award" @click="dialogVisible = true" />
    
        <DataTable :value="awardList" tableStyle="min-width: 50rem">
        <Column field="id" header="Id"></Column>
        <Column field="points_per_member" header="Points per member"></Column>
        <Column field="points_per_leader" header="Points per leader"></Column>
    </DataTable>
    
    
    
    <Dialog v-model:visible="dialogVisible" modal header="Add award" :style="{ width: '25rem' }">
        <!-- span class="p-text-secondary block mb-5">Update your information.</span -->
        <div class="flex align-items-center gap-3 mb-3">
            <label for="pointsPerMember" class="font-semibold w-6rem">Points per member</label>
            <InputText v-model="newAward.pointsPerMember" id="pointsPerMember" class="flex-auto" autocomplete="off" />
        </div>
        <div class="flex align-items-center gap-3 mb-5">
            <label for="pointsPerLeader" class="font-semibold w-6rem">Points per leader</label>
            <InputText v-model="newAward.pointsPerLeader" id="pointsPerLeader" class="flex-auto" autocomplete="off" />
        </div>
        <div class="flex justify-content-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="dialogVisible = false"></Button>
            <Button type="button" label="Save" @click="onCreateAward"></Button>
        </div>
    </Dialog>
    
    
    
    </template>
    <script setup lang="ts">
    import { ref, onMounted } from 'vue';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column'
    import Button from 'primevue/button'
    
    import Dialog from 'primevue/dialog'
    
    import InputText from 'primevue/inputtext'
    import { Award, createAward, getAwardList } from '../utils/Award'
    
    const dialogVisible = ref(false);
    
    const awardList = ref([]);
    
    const newAward = ref(new Award("", ""))
    
    async function onCreateAward() {
        const resp = await createAward(newAward.value);
        console.log(resp)
    
        if (resp.ok) {
            // reload award list 
            awardList.value = await getAwardList();
            dialogVisible.value = false;
        }
    }
    
    onMounted(async () => {
        awardList.value = await getAwardList();
    })
    </script>