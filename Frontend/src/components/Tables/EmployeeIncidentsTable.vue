<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getEmployeeIncidents } from '@/api/api.js';

const employeeincidents = ref([
  {
    EmployeeIncidentID: 0,
    EmployeeID: 0,
    Description: '',
    Resolution: '',
    Date: '0000-00-00',
    StatusCode: 0
  }
])
const isLoading = ref(true)

const loadEmployeeIncidents = async () => {
  try {
    const response = await getEmployeeIncidents()
    employeeincidents.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the employee incidents:", err)
    isLoading.value = false
  }
}

onMounted(loadEmployeeIncidents)
</script>

<template>
  <div class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
    <h4 class="mb-6 text-xl font-semibold text-black dark:text-white">Employee Incidents</h4>
    <div class="flex flex-col">
      <div class="grid grid-cols-4 rounded-sm bg-gray-2 dark:bg-meta-4 sm:grid-cols-5">
        <div class="p-2.5 text-center xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Employee ID</h5>
        </div>
        <div class="p-2.5 xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Description</h5>
        </div>
        <div class="p-2.5 xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Resolution</h5>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Date</h5>
        </div>
        <div class="p-2.5 text-center xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Status Code</h5>
        </div>
      </div>

      <div
        v-for="(incident,key) in employeeincidents"
        :key="incident.EmployeeIncidentID"
        :class="`grid grid-cols-4 sm:grid-cols-5 ${key === employeeincidents.length - 1 ? '' : 'border-b border-stroke dark:border-strokedark'}`">
        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p class="font-bold text-black dark:text-white sm:block">{{ incident.EmployeeID }}</p>   
        </div>

        <div class="flex items-center gap-3 p-2.5 xl:p-5">
          <p class="text-clip overflow-hidden hover:overflow-x-auto text-black dark:text-white">{{ incident.Description || 'N/A' }}</p>
        </div>

        <div class="flex items-center gap-3 p-2.5 xl:p-5">
          <p class="text-clip overflow-hidden hover:overflow-x-auto text-black dark:text-white">{{ incident.Resolution || 'N/A'  }}</p>
        </div>

        <div class="hidden text-center items-center justify-center p-2.5 sm:flex xl:p-5">
          <p class="text-black dark:text-white">{{ incident.Date || 'N/A' }}</p>
        </div>

        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p v-if="incident.StatusCode == 2" 
            class="inline-flex rounded-full bg-opacity-10 py-1 px-4 text-sm font-medium"
            :class="{'bg-success text-success': incident.StatusCode == 2}"> Resolved
          </p>
          <p v-if="incident.StatusCode == 1" 
            class="inline-flex rounded-full bg-opacity-10 py-1 px-4 text-sm font-medium"
            :class="{'bg-success text-success': incident.StatusCode == 1}"> Open
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
