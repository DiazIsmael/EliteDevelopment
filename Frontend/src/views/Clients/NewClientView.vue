<script setup lang="ts">
import { ref } from 'vue'
import { createClient } from '@/api/api.js'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import AlertError from '@/components/Alerts/AlertError.vue'
import InputGroup from '@/components/Forms/InputGroup.vue'
import ClientStatusDropdown from '@/components/Forms/Dropdowns/ClientStatusDropdown.vue'
import ClientTypeDropdown from '@/components/Forms/Dropdowns/ClientTypeDropdown.vue'

const pageTitle = ref('New Client')
const formStatus = ref('')
const showSuccessAlert = ref(false)
const showErrorAlert = ref(false)
const newClient = ref({
  Name: '',
  MainContact: '',
  Phone: '',
  Email: '',
  Address: '',
  ClientCode: 1,
  StatusCode: 1
})

const submitClientForm = async (event) => {
  event.preventDefault();
  if (!newClient.value.Name || !newClient.value.MainContact || !newClient.value.Phone || !newClient.value.Email || !newClient.value.Address || !newClient.value.StatusCode|| !newClient.value.ClientCode) {
    alert("Please fill all required fields.");
    return;
  }
  try {
    const clientData = {
      Name: newClient.value.Name,
      MainContact: newClient.value.MainContact,
      Phone: newClient.value.Phone,
      Email: newClient.value.Email,
      Address: newClient.value.Address,
      ClientCode: newClient.value.ClientCode,
      StatusCode: newClient.value.StatusCode
    };
    const response = await createClient(clientData);

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
            <router-link class="font-medium" to="/clients"> Clients / </router-link>
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
        <DefaultCard cardTitle="Client Creation Form">
          <form @submit="submitClientForm">
            <div class="flex flex-col gap-5.5 p-6.5">
              <div>
                <InputGroup
                required
                v-model="newClient.Name"
                label="Company Name"
                type="text"
                placeholder="Enter the client's company name"
                customClasses="mb-4.5"
                />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newClient.MainContact"
                  label="Main Contact"
                  type="text"
                  placeholder="Enter main contact's name"
                  customClasses="w-full xl:w-1/2"
                />

                <InputGroup
                  required
                  v-model="newClient.Phone"
                  label="Phone Number"
                  type="text"
                  placeholder="Enter the client's phone number"
                  customClasses="w-full xl:w-1/2"
                />
              </div>

              <InputGroup
                required
                v-model="newClient.Email"
                label="Email"
                type="email"
                placeholder="Enter the client's email"
                customClasses="mb-4.5"
              />

              <InputGroup
                required
                v-model="newClient.Address"
                label="Address"
                type="text"
                placeholder="Enter the client's address"
                customClasses="mb-4.5"
              />

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <ClientStatusDropdown required class="w-full xl:w-1/2" v-model="newClient.StatusCode"/>

                <ClientTypeDropdown required class="w-full xl:w-1/2" v-model="newClient.ClientCode"/>
              </div>

              <!-- Form Submit Button -->
              <button class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                  Add New Client
              </button>      
            </div>
          </form>
        </DefaultCard>
      </div>
  </DefaultLayout>
</template>