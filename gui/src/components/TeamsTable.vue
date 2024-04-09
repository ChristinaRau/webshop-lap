<template>
    <Button label="Add team" @click="dialogVisible = true" />
    
        <DataTable :value="teamList" tableStyle="min-width: 50rem">
        <Column field="id" header="Id"></Column>
        <Column field="points_per_member" header="Points per member"></Column>
        <Column field="points_per_leader" header="Points per leader"></Column>
    </DataTable>
    
    
    
    <Dialog v-model:visible="dialogVisible" modal header="Add team" :style="{ width: '25rem' }">
        <div class="flex align-items-center gap-3 mb-3">
            <label for="leader" class="font-semibold w-6rem">Team leader</label>
            <AutoComplete
            v-model="selectedLeader"
            :option-label="(data) => data.first_name + ' ' + data.last_name"
            dropdown :suggestions="personSuggestions"
            @complete="searchPersons">
            <template #option="slotProps">
            <div>{{ slotProps.option.first_name + " " + slotProps.option.last_name }}</div> 
            </template>
          
            </AutoComplete>

</div>
        <div class="flex align-items-center gap-3 mb-5">
            <label for="teamMembers" class="font-semibold w-6rem">Team members</label>
            <AutoComplete
            multiple
            v-model="selectedMembers"
            :option-label="(data) => data.first_name + ' ' + data.last_name"
            dropdown :suggestions="personSuggestions"
            @complete="searchPersons">
            <template #option="slotProps">
            <div>{{ slotProps.option.first_name + " " + slotProps.option.last_name }}</div> 
            </template>
          
            </AutoComplete>
        </div>
        <div class="flex justify-content-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="dialogVisible = false"></Button>
            <Button type="button" label="Save" @click="onCreateTeam"></Button>
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
    import AutoComplete, { AutoCompleteCompleteEvent } from 'primevue/autocomplete';
    import { Team, createTeam, getTeamList } from '../utils/Team'
    import { Person, getPersonList } from '../utils/Person';
    
    const dialogVisible = ref(false);
    
    const teamList = ref([]);

    // for selection of leader and members
    const personList = ref([]);
    let personSuggestions = ref([]);

    const selectedLeader = ref();
    const selectedMembers = ref();
    
    const newTeam = ref(new Team(new Person("", "")))
    
    async function onCreateTeam() {
        /* const resp = await createTeam(newTeam.value);
        console.log(resp)
    
        if (resp.ok) {
            // reload team list 
            teamList.value = await getTeamList();
            dialogVisible.value = false;
        } */

        console.log(selectedLeader.value)
        console.log(selectedMembers.value)
    }
    

    function searchPersons(event: AutoCompleteCompleteEvent) {
        personSuggestions.value = personList.value.filter((el) => String(el.first_name + " " + el.last_name).toLowerCase().includes(event.query.toLowerCase()))
    }

    onMounted(async () => {
        teamList.value = await getTeamList();
        personList.value = await getPersonList();
        personSuggestions.value = [...personList.value]
    })
    </script>