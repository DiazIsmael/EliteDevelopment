<script setup lang="ts">
import { ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import ClientsTable from '@/components/Tables/ClientsTable.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const pageTitle = ref('Registered Clients')
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <div class="flex flex-col gap-10">
      <ClientsTable />
    </div>
  </DefaultLayout>
</template>
