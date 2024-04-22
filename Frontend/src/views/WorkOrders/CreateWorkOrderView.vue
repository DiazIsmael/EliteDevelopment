<script setup lang="ts">
import { ref } from 'vue'
import { createWorkOrder } from '@/api/api.js'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import AlertError from '@/components/Alerts/AlertError.vue'
import InputGroup from '@/components/Forms/InputGroup.vue'
import AccountDropdown from '@/components/Forms/Dropdowns/AccountDropdown.vue'
import EmployeeDropdown from '@/components/Forms/Dropdowns/EmployeeDropdown.vue'
import ClientDropdown from '@/components/Forms/Dropdowns/ClientDropdown.vue'
import InvoiceDropdown from '@/components/Forms/Dropdowns/InvoiceDropdown.vue'

const pageTitle = ref('Create Work Order')
const formStatus = ref('')
const showSuccessAlert = ref(false)
const showErrorAlert = ref(false)
const newWorkOrder = ref({
  ClientID: 0,
  AccountID: 0,
  EmployeeID: 0,
  Date: '',
  Name: '',
  Description: '',
  Price: 0,
  Frequency: '',
  InvoiceID: 0
})

const submitWorkOrderForm = async (event) => {
  event.preventDefault();
  if (!newWorkOrder.value.ClientID || !newWorkOrder.value.EmployeeID || !newWorkOrder.value.Date || !newWorkOrder.value.Name || !newWorkOrder.value.Description || !newWorkOrder.value.Price || !newWorkOrder.value.Frequency) {
    alert("Please fill all required fields.");
    return;
  }
  try {
    const workOrderData = {
      ClientID: newWorkOrder.value.ClientID,
      InvoiceID: newWorkOrder.value.InvoiceID,
      AccountID: newWorkOrder.value.AccountID,
      EmployeeID: newWorkOrder.value.EmployeeID,
      Date: newWorkOrder.value.Date,
      Name: newWorkOrder.value.Name,
      Address: newWorkOrder.value.Address,
      Frequency: newWorkOrder.value.Frequency,
      Price: newWorkOrder.value.Price
    };
    const response = await createWorkOrder(workOrderData);

    if (response == "Query successfully executed!") {
      formStatus.value = 'Service Created Successfully';
      showSuccessAlert.value = true;
    }
    else if (response != "Query successfully executed!") {
      formStatus.value = 'Error Creating Service';
      showErrorAlert.value = true;
    }
  } catch (error) {
    formStatus.value = 'Error Creating Service';
    showErrorAlert.value = true;
    console.log(error);
  }
}
</script>

<template>
  <DefaultLayout>
      <AlertSuccess v-if="showSuccessAlert" @click="showSuccessAlert = false" class="gap-7.5"/>
      <AlertError v-if="showErrorAlert" @click="showErrorAlert = false" class="gap-7.5"/>

    <!-- Breadcrumb Start -->
    <div class="pt-7.5 mb-6 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
      <h2 class="text-title-md2 font-semibold text-black dark:text-white">
        {{ pageTitle }}
      </h2>

      <nav>
        <ol class="flex items-center gap-2">
          <li>
            <router-link class="font-medium" to="/"> Dashboard / </router-link>
          </li>
          <li>
            <router-link class="font-medium" to="/workorders"> Work Orders / </router-link>
          </li>
          <li class="font-medium text-primary">
            {{ pageTitle }}
          </li>
        </ol>
      </nav>
    </div>
    <!-- Breadcrumb End -->

    <!-- Form Section Start -->
      <div class="flex flex-col gap-10">
        <DefaultCard cardTitle="Work Order Creation Form">
          <form @submit="submitWorkOrderForm">
            <div class="flex flex-col gap-5.5 p-6.5">
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <ClientDropdown required class="w-full xl:w-1/2" v-model="newWorkOrder.ClientID"/>

                <AccountDropdown required class="w-full xl:w-1/2" v-model="newWorkOrder.AccountID"/>
              </div>

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  disabled
                  v-model="newWorkOrder.Name"
                  label="Work Order Name"
                  type="text"
                  placeholder="Enter the work order's name"
                  customClasses="w-full xl:w-1/2"
                />
                
                <EmployeeDropdown required class="w-full xl:w-1/2" v-model="newWorkOrder.EmployeeID"/>
              </div>

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newWorkOrder.Address"
                  label="Address"
                  type="text"
                  placeholder="Enter the work order's jobsite address"
                  customClasses="w-full xl:w-1/2"
                />

                <InputGroup
                  required
                  v-model="newWorkOrder.Frequency"
                  label="Frequency"
                  type="text"
                  placeholder="Enter the work order's service frequency"
                  customClasses="w-full xl:w-1/2"
                />
              </div>

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newWorkOrder.Date"
                  label="Date"
                  type="date"
                  placeholder="Enter the work order's service frequency"
                  customClasses="w-full xl:w-1/2"
                />

                <InputGroup
                  required
                  v-model="newWorkOrder.Price"
                  label="Price"
                  type="text"
                  placeholder="Enter the work order's price"
                  customClasses="w-full xl:w-1/2"
                />
              </div>

              <div class="mb-4.5 flex flex-col justify-center gap-6 xl:flex-row">
                <InvoiceDropdown required class="w-full xl:w-1/2" v-model="newWorkOrder.InvoiceID"/>
              </div>

              <!-- Form Submit Button -->
              <button class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                  Create Work Order
              </button>      
            </div>
          </form>
        </DefaultCard>
      </div>
  </DefaultLayout>
</template>