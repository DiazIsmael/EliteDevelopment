<script setup lang="ts">
import { ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import InvoiceDetailsTable from '@/components/Tables/InvoiceDetailsTable.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const pageTitle = ref('All Past Invoices')
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <div class="flex flex-col gap-10">
      <InvoiceDetailsTable />
    </div>
  </DefaultLayout>
</template>
