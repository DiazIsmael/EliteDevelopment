<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getInvoiceDetails } from '@/api/api.js';

// Defining necessary variables
const invoicedetails = ref([
  {
    InvoiceID: 0,
    ClientName: '',
    InvoiceNumber: 0,
    WorkOrderID: '',
    WorkOrderDate: '',
    WorkOrderName: '',
    EmployeeName: '',
    WorkOrderDescription: '',
    WorkOrderFrequency: '',
    WorkOrderPrice: 0,
    Breadcrumb: 'Loading...'
  }
])
const isLoading = ref(true)
const route = useRoute()
const emit = defineEmits(['emitBreadcrumb'])

// Method to fetch/GET invoice details table data from the backend API
const loadInvoiceDetails = async (invoiceID) => {
  try {
    const response = await getInvoiceDetails(invoiceID)
    invoicedetails.value = response

    if (invoicedetails.value[0].WorkOrderID != 'Total') {
      invoicedetails.value[0].Breadcrumb = `${invoicedetails.value[0].ClientName} Invoice #${invoicedetails.value[1].InvoiceNumber}`;
      emit('emitBreadcrumb', invoicedetails.value[0].Breadcrumb) // Emitting breadcrumb update event
    }
    
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
</script>

<template>
  <div
    class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1"
  >
    <div class="max-w-full overflow-x-auto">
      <table class="w-full table-auto">
        <thead>
          <tr class="bg-gray-2 text-center dark:bg-meta-4">
            <th class="hidden sm:block py-4 px-0 font-medium text-black dark:text-white">Work Order</th>
            <th class="py-4 px-4 font-medium text-black dark:text-white">Date</th>
            <th class="py-4 px-4 font-medium text-black dark:text-white">Name</th>
            <th class="hidden sm:block py-4 px-4 font-medium text-black dark:text-white">Employee</th>
            <th class="py-4 px-4 font-medium text-black dark:text-white">Description</th>
            <th class="py-4 px-4 font-medium text-black dark:text-white">Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(workorder, index) in invoicedetails" :key="index" class="text-center">
            <td class="hidden sm:block py-5 px-4">
              <h5 v-if="workorder.WorkOrderID != 'Total'" class="text-black dark:text-white">{{ workorder.WorkOrderID }}</h5>
              <h5 v-else class="font-bold text-black dark:text-white">{{ workorder.WorkOrderID }}</h5>
            </td>
            <td class="sm:px-4 py-5 px-1">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderDate }}</p>
            </td>
            <td class="sm:px-4 sm:text-center py-5 px-1">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderName }}</p>
            </td>
            <td class="hidden sm:block py-5 px-4">
              <p class="text-black dark:text-white">{{ workorder.EmployeeName }}</p>
            </td>
            <td class="sm:px-4 py-5 px-1">
              <p class="text-black dark:text-white">{{ workorder.WorkOrderDescription }}</p>
            </td>
            <td class="sm:px-4 sm:text-center py-5 px-1">
              <p v-if="workorder.WorkOrderID != 'Total'" class="text-meta-3">{{ workorder.WorkOrderPrice }}</p>
              <p v-if="workorder.WorkOrderID == 'Total'" class="font-bold text-black dark:text-white">{{ workorder.WorkOrderPrice }}</p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>