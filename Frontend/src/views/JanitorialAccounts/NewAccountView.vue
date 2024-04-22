<script setup lang="ts">
import { ref } from 'vue'
import { createJanitorialAccount } from '@/api/api.js'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import AlertError from '@/components/Alerts/AlertError.vue'
import InputGroup from '@/components/Forms/InputGroup.vue'
import AccountStatusDropdown from '@/components/Forms/Dropdowns/AccountStatusDropdown.vue'
import ClientDropdown from '@/components/Forms/Dropdowns/ClientDropdown.vue'
import ServiceDropdown from '@/components/Forms/Dropdowns/ServiceDropdown.vue'

const pageTitle = ref('New Account')
const formStatus = ref('')
const showSuccessAlert = ref(false)
const showErrorAlert = ref(false)
const newAccount = ref({
  ClientID: 0,
  ServiceID: 0,
  Name: '',
  Address: '',
  Frequency: '',
  Price: 0.00,
  StatusCode: 0
})

const submitAccountForm = async (event) => {
  event.preventDefault();
  if (!newAccount.value.ClientID || !newAccount.value.ServiceID || !newAccount.value.Name || !newAccount.value.Address || !newAccount.value.Frequency || !newAccount.value.Price || !newAccount.value.StatusCode) {
    alert("Please fill all required fields.");
    return;
  }
  try {
    const accountData = {
      ClientID: newAccount.value.ClientID,
      ServiceID: newAccount.value.ServiceID,
      Name: newAccount.value.Name,
      Address: newAccount.value.Address,
      Frequency: newAccount.value.Frequency,
      Price: newAccount.value.Price,
      StatusCode: newAccount.value.StatusCode
    };
    const response = await createJanitorialAccount(accountData);

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
            <router-link class="font-medium" to="/accounts"> Accounts / </router-link>
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
        <DefaultCard cardTitle="Account Creation Form">
          <form @submit="submitAccountForm">
            <div class="flex flex-col gap-5.5 p-6.5">
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <ClientDropdown required class="w-full xl:w-1/2" v-model="newAccount.ClientID"/>

                <ServiceDropdown required class="w-full xl:w-1/2" v-model="newAccount.ServiceID"/>
              </div>

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newAccount.Name"
                  label="Account Name"
                  type="text"
                  placeholder="Enter the account's name"
                  customClasses="w-full xl:w-1/2"
                />
                
                <InputGroup
                  required
                  v-model="newAccount.Address"
                  label="Address"
                  type="text"
                  placeholder="Enter the account's jobsite address"
                  customClasses="w-full xl:w-1/2"
                />
              </div>

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newAccount.Frequency"
                  label="Frequency"
                  type="text"
                  placeholder="Enter the account's service frequency"
                  customClasses="w-full xl:w-1/2"
                />

                <InputGroup
                  required
                  v-model="newAccount.Price"
                  label="Price"
                  type="number"
                  placeholder="Enter the account's price"
                  customClasses="w-full xl:w-1/2"
                />
              </div>

              <div class="mb-4.5 flex flex-col justify-center gap-6 xl:flex-row">
                <AccountStatusDropdown required class="w-full xl:w-1/2" v-model="newAccount.StatusCode"/>
              </div>

              <!-- Form Submit Button -->
              <button class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                  Add New Account
              </button>      
            </div>
          </form>
        </DefaultCard>
      </div>
  </DefaultLayout>
</template>