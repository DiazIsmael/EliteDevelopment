<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getWorkOrders } from '@/api/api.js';

const workorders = ref([
  {
    WorkOrderID: 0,
    AccountID: 0,
    EmployeeID: 0,
    Date: '',
    Name: '',
    Description: '',
    Price: 0.00,
    Frequency: '',
    InvoiceID: 0,
    ClientID: 0,
  }
])
const isLoading = ref(true)

const loadWorkOrders = async () => {
  try {
    const response = await getWorkOrders()
    workorders.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the work orders:", err)
    isLoading.value = false
  }
}

onMounted(loadWorkOrders)
</script>

<template>
  <div class="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
    <div class="py-6 px-4 md:px-6 xl:px-7.5">
      <h4 class="text-xl font-bold text-black dark:text-white">Work Orders</h4>
    </div>
    <!-- Table Header -->
    <div
      class="grid grid-cols-4 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-9 md:px-6 2xl:px-7.5">
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">AccountID</p>
      </div>
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">EmployeeID</p>
      </div>
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">Date</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Name</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Description</p>
      </div>
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">Frequency</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Price</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">InvoiceID</p>
      </div>
      <div class="hidden text-center col-span-1 justify-center items-center sm:flex">
        <p class="font-medium">ClientID</p>
      </div>
    </div>

    <!-- Table Rows -->
    <div
      v-for="(workorder, key) in workorders"
      :key="workorder.WorkOrderID"
      :class="`grid grid-cols-4 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-9 md:px-6 2xl:px-7.5`">
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-bold text-black dark:text-white">{{ workorder.AccountID || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ workorder.EmployeeID || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ workorder.Date || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-clip overflow-hidden hover:overflow-x-auto text-sm font-medium text-black dark:text-white">{{ workorder.Name || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ workorder.Description || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ workorder.Frequency || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-meta-3">${{ workorder.Price || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ workorder.InvoiceID || 'N/A' }}</p>
      </div>
      <div class="hidden col-span-1 justify-center items-center sm:flex">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ workorder.ClientID || 'N/A' }}</p>
      </div>
    </div>
  </div>
</template>