<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getClients } from '@/api/api.js';

const clients = ref([
  {
    ClientID: 0,
    ClientCode: 0,
    Name: '',
    MainContact: '',
    Phone: '',
    Email: '',
    Address: '',
    AddedDate: '0000-00-00',
    StatusCode: 0
  }
])
const isLoading = ref(true)

const loadClients = async () => {
  try {
    const response = await getClients()
    clients.value = response
    isLoading.value = false
  } catch (err) {
    console.error("There was an error fetching the clients:", err)
    isLoading.value = false
  }
}

onMounted(loadClients)
</script>

<template>
  <div class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
    <h4 class="mb-6 text-xl font-semibold text-black dark:text-white">Clients</h4>
    <div class="flex flex-col">
      <!-- Table Header -->
      <div class="grid grid-cols-4 rounded-sm bg-gray-2 dark:bg-meta-4 sm:grid-cols-8">
        <div class="p-2.5 xl:p-5">
          <p class="text-sm font-medium uppercase xsm:text-base">Name</p>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <p class="text-sm font-medium uppercase xsm:text-base">Address</p>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <p class="text-sm font-medium uppercase xsm:text-base">Main Contact</p>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <p class="text-sm font-medium uppercase xsm:text-base">Email</p>
        </div>
        <div class="hidden p-2.5 text-center sm:block xl:p-5">
          <p class="text-sm font-medium uppercase xsm:text-base">Phone Number</p>
        </div>
        <div class="col-span-1 flex justify-center items-center">
          <p class="text-sm font-medium uppercase xsm:text-base">Date Added</p>
        </div>
        <div class="col-span-1 flex justify-center items-center">
          <p class="text-sm font-medium uppercase xsm:text-base">Client Code</p>
        </div>
        <div class="col-span-1 flex justify-center items-center">
          <p class="text-sm font-medium uppercase xsm:text-base">Status Code</p>
        </div>
      </div>

      <!-- Table Rows -->
      <div
        v-for="(client, key) in clients"
        :key="client.ClientID"
        :class="`grid grid-cols-4 sm:grid-cols-8 ${key === clients.length - 1 ? '' : 'border-b border-stroke dark:border-strokedark'}`">
        <div class="col-span-1 flex items-center">
          <div class="flex items-center gap-3 p-2.5 xl:p-5">
            <p class="font-bold text-black dark:text-white">{{ client.Name }}</p>
          </div>
        </div>
        <div class="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
          <p class="text-center text-sm font-medium text-black dark:text-white">{{ client.Address || 'N/A' }}</p>
        </div>
        <div class="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
          <p class="text-center text-sm font-medium text-black dark:text-white">{{ client.MainContact || 'N/A' }}</p>
        </div>
        <div class="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
          <p class="text-center text-clip overflow-hidden hover:overflow-x-auto text-sm font-medium text-black dark:text-white">{{ client.Email || 'N/A' }}</p>
        </div>
        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p class="text-center text-sm font-medium text-black dark:text-white">{{ client.Phone || 'N/A' }}</p>
        </div>
        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p class="text-center text-sm font-medium text-black dark:text-white">{{ client.AddedDate || 'N/A' }}</p>
        </div>
        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p v-if="client.ClientCode == 1" class="text-meta-3">{{ client.ClientCode }}</p>
          <p v-if="client.ClientCode == 2" class="text-meta-6">{{ client.ClientCode }}</p>
          <p v-if="client.ClientCode == 3" class="text-meta-3">{{ client.ClientCode }}</p>
          <p v-if="client.ClientCode == 4" class="text-meta-3">{{ client.ClientCode }}</p>
        </div>
        <div class="flex items-center justify-center p-2.5 xl:p-5">
          <p v-if="client.StatusCode == 1" class="text-meta-6">{{ client.StatusCode }}</p>
          <p v-if="client.StatusCode == 2" class="text-meta-3">{{ client.StatusCode }}</p>
          <p v-if="client.StatusCode == 3" class="text-meta-5">{{ client.StatusCode }}</p>
          <p v-if="client.StatusCode == 4" class="text-meta-1">{{ client.StatusCode }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
