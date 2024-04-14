<script setup lang="ts">
import DataStatsOne from '@/components/DataStats/DataStatsOne.vue'
import ChartOne from '@/components/Charts/ChartOne.vue'
import ChartThree from '@/components/Charts/ChartThree.vue'
import ChartTwo from '@/components/Charts/ChartTwo.vue'
import TableOne from '@/components/Tables/TableOne.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
</script>

<template>
  <DefaultLayout>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-2 md:gap-6 xl:grid-cols-4 2xl:gap-7.5">
      <DataStatsOne />
    </div>

    <div class="mt-4 grid grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-7.5 2xl:gap-7.5">
      <!-- ====== Chart One Start -->
      <div class="col-span-12 xl:col-span-12">
        <ChartOne />
      </div>
      <!-- ====== Chart One End -->

      <!-- ====== Chart Two Start -->
      <div class="col-span-12 xl:col-span-6">
        <ChartTwo />
      </div>
      <!-- ====== Chart Two End -->

      <!-- ====== Chart Three Start -->
      <div class="col-span-12 xl:col-span-6">
        <ChartThree />
      </div>
      <!-- ====== Chart Three End -->

      <!-- ====== Table One Start -->
      <div class="col-span-12 xl:col-span-12">
        <TableOne />
      </div>
      <!-- ====== Table One End -->
    </div>
  </DefaultLayout>
</template>
