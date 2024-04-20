<script setup lang="ts">
import { ref } from 'vue'
import InvoiceDetailsTable from '@/components/Tables/InvoiceDetailsTable.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const pageTitle = ref('Loading Invoice Details...')

const updateBreadcrumb = (breadcrumb) => {
  pageTitle.value = breadcrumb; // Updates pageTitle based on emitted event from InvoiceDetailsTable
};
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <div class="mb-6 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
      <h2 class="text-title-md2 font-semibold text-black dark:text-white">{{ pageTitle }}</h2>

      <nav>
        <ol class="flex items-center gap-2">
          <li>
            <router-link class="font-medium" to="/"> Dashboard / </router-link>
          </li>
          <li>
            <router-link class="font-medium" to="/Invoices"> Past Invoices /</router-link>
          </li>
          <li class="font-medium text-primary">{{ pageTitle }}</li>
        </ol>
      </nav>
    </div>
    <!-- Breadcrumb End -->

    <div class="flex flex-col gap-10">
      <InvoiceDetailsTable @emitBreadcrumb="updateBreadcrumb"/>
    </div>
  </DefaultLayout>
</template>
