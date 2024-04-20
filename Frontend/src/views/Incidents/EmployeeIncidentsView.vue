<script setup lang="ts">
import { ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import EmployeeIncidentsTable from '@/components/Tables/EmployeeIncidentsTable.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const pageTitle = ref('Employee-Related Incidents')
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <div class="flex flex-col gap-10">
      <EmployeeIncidentsTable />
    </div>
  </DefaultLayout>
</template>
