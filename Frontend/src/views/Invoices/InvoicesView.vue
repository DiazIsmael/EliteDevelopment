<script setup lang="ts">
import { ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import InvoicesTable from '@/components/Tables/InvoicesTable.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const pageTitle = ref('Past Invoices')
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <div class="flex flex-col gap-10">
      <InvoicesTable />
    </div>
  </DefaultLayout>
</template>
