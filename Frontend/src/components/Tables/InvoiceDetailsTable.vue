<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { getInvoiceDetails } from '@/api/api.js';

// Defining necessary variables
const invoicedetails = ref([
  {
    InvoiceID: 0,
    ClientName: '',
    InvoiceNumber: 0,
    WorkOrderDate: '',
    WorkOrderName: '',
    EmployeeName: '',
    WorkOrderDescription: '',
    WorkOrderFrequency: '',
    WorkOrderPrice: 0
  }
])
const isLoading = ref(true)
const route = useRoute()

// Method to fetch/GET invoice details table data from the backend API
const loadInvoiceDetails = async (invoiceID) => {
  try {
    const response = await getInvoiceDetails(invoiceID)
    invoicedetails.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the invoice details:", err)
    isLoading.value = false
  }
}

// Mounted lifecycle hook to load invoice details when the component mounts
onMounted(() => {
  loadInvoiceDetails(route.params.invoiceID)
})

// Watcher to react to changes in the route params (if the component is used in a way where the route can change without remounting)
watch(() => route.params.invoiceID, (newInvoiceID) => {
  if (newInvoiceID) {
    loadInvoiceDetails(newInvoiceID)
  }
})
</script>

<template>
  <div
    class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1"
  >
    <div class="max-w-full overflow-x-auto">
      <table class="w-full table-auto">
        <thead>
          <tr class="bg-gray-2 text-left dark:bg-meta-4">
            <th class="py-4 px-4 font-medium text-black dark:text-white xl:pl-11">Client</th>
            <th class="py-4 px-0 text-center font-medium text-black dark:text-white">Invoice No</th>
            <th class="py-4 px-4 text-center font-medium text-black dark:text-white">Date</th>
            <th class="py-4 px-4 text-center font-medium text-black dark:text-white">Name</th>
            <th class="py-4 px-4 text-center font-medium text-black dark:text-white">Employee</th>
            <th class="py-4 px-4 text-center font-medium text-black dark:text-white">Description</th>
            <th class="py-4 px-4 text-center font-medium text-black dark:text-white">Frequency</th>
            <th class="py-4 px-4 text-center font-medium text-black dark:text-white">Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(workorder, index) in invoicedetails" :key="index">
            <td class="py-5 px-4 pl-9 xl:pl-11">
              <h5 v-if="workorder.ClientName != 'Total'" class="text-black dark:text-white">{{ workorder.ClientName }}</h5>
              <h5 v-else class="font-bold text-black dark:text-white">{{ workorder.ClientName }}</h5>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.InvoiceNumber }}</p>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderDate }}</p>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderName }}</p>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.EmployeeName }}</p>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderDescription }}</p>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderFrequency }}</p>
            </td>
            <td class="text-center py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderPrice }}</p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>