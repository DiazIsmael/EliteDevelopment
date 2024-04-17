<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getServices } from '@/api/api.js';

const services = ref([
  {
    ServiceID: 0,
    Description: ''
  }
])
const isLoading = ref(true)

const loadServices = async () => {
  try {
    const response = await getServices()
    services.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the services:", err)
    isLoading.value = false
  }
}

onMounted(loadServices)
</script>

<template>
  <div class="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
    <div class="py-6 px-4 md:px-6 xl:px-7.5">
      <h4 class="text-xl font-bold text-black dark:text-white">Services</h4>
    </div>
    <!-- Table Header -->
    <div
      class="grid grid-cols-2 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-2 md:px-6 2xl:px-7.5">
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Description</p>
      </div>
      <div class="text-center col-span-1 flex justify-center items-center">
        <p class="font-medium">Service No</p>
      </div>
    </div>

    <!-- Table Rows -->
    <div
      v-for="(service, index) in services"
      :key="index"
      :class="`grid grid-cols-2 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-2 md:px-6 2xl:px-7.5`">
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-medium text-black dark:text-white">{{ service.Description || 'N/A' }}</p>
      </div>
      <div class="col-span-1 flex justify-center items-center">
        <p class="text-center text-sm font-bold text-black dark:text-white">{{ service.ServiceID || 'N/A' }}</p>
      </div>
    </div>
  </div>
</template>