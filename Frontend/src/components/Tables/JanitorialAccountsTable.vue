<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getJanitorialAccounts } from '@/api/api.js';

const janitorialaccounts = ref([
  {
    ClientID: 0,
    ServiceID: 0,
    Name: '',
    Address: '',
    Frequency: '',
    Price: 0.00,
    StatusCode: 0
  }
])
const isLoading = ref(true)

const loadJanitorialAccounts = async () => {
  try {
    const response = await getJanitorialAccounts()
    janitorialaccounts.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the work orders:", err)
    isLoading.value = false
  }
}

onMounted(loadJanitorialAccounts)
</script>

<template>
  <div class="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
    <div class="py-6 px-4 md:px-6 xl:px-7.5">
      <h4 class="text-xl font-bold text-black dark:text-white">Accounts</h4>
    </div>
    <!-- Table Header -->
    <div
      class="grid grid-cols-4 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-7 md:px-6 2xl:px-7.5">
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">ClientID</p>
      </div>
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">ServiceID</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Name</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Address</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Frequency</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Price</p>
      </div>
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">StatusCode</p>
      </div>
    </div>

    <!-- Table Rows -->
    <div
      v-for="(account, index) in janitorialaccounts"
      :key="index"
      :class="`grid grid-cols-4 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-7 md:px-6 2xl:px-7.5`">
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-bold text-black dark:text-white">{{ account.ClientID || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ account.ServiceID || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ account.Name || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ account.Address || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ account.Frequency || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-meta-3">${{ account.Price || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ account.StatusCode || 'N/A' }}</p>
      </div>
    </div>
  </div>
</template>