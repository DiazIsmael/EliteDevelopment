<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getEmployees } from '@/api/api.js';

const employees = ref([
  {
    EmployeeID: 0,
    FirstName: '',
    LastName: '',
    Address: '',
    Email: '',
    Phone: '',
    StatusCode: 0
  }
])
const isLoading = ref(true)

const loadEmployees = async () => {
  try {
    const response = await getEmployees()
    employees.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the employees:", err)
    isLoading.value = false
  }
}

onMounted(loadEmployees)
</script>

<template>
  <div class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
    <div class="flex flex-col">
      <div class="grid grid-cols-3 rounded-sm bg-gray-2 dark:bg-meta-4 sm:grid-cols-5">
        <div class="p-2.5 xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Name</h5>
        </div>
        <div class="p-2.5 text-center xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Address</h5>
        </div>
        <div class="p-2.5 text-center xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Email</h5>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Phone Number</h5>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <h5 class="text-sm font-medium uppercase xsm:text-base">Status Code</h5>
        </div>
      </div>

      <div
        v-for="(employee,key) in employees"
        :key="employee.EmployeeID"
        :class="`grid grid-cols-3 sm:grid-cols-5 ${key === employees.length - 1 ? '' : 'border-b border-stroke dark:border-strokedark'}`"
      >
        <div class="flex items-center gap-3 p-2.5 xl:p-5">
          <p v-if="employee.StatusCode != 1" class="font-bold text-meta-5 dark:text-meta-5 sm:block">{{ employee.FirstName }} {{ employee.LastName }}</p>
          <p v-if="employee.StatusCode == 1" class="font-bold text-meta-1 dark:text-meta-5 sm:block">{{ employee.FirstName }} {{ employee.LastName }}</p>
        </div>

        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p class="text-black dark:text-white">{{ employee.Address || 'N/A'  }}</p>
        </div>

        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p class="text-black dark:text-white">{{ employee.Email || 'N/A'  }}</p>
        </div>

        <div class="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
          <p class="text-black dark:text-white">{{ employee.Phone || 'N/A'  }}</p>
        </div>

        <div class="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
          <p v-if="employee.StatusCode != 1" class="text-meta-5">{{ employee.StatusCode }}</p>
          <p v-if="employee.StatusCode == 1" class="text-meta-1">{{ employee.StatusCode }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
