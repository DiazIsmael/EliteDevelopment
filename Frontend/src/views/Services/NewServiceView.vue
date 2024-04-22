<script setup lang="ts">
import { ref } from 'vue'
import { createService } from '@/api/api.js'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import AlertError from '@/components/Alerts/AlertError.vue'

const pageTitle = ref('New Service')
const serviceDescription = ref('')
const formStatus = ref('')
const showSuccessAlert = ref(false)
const showErrorAlert = ref(false)

const submitServiceForm = async (event) => {
  event.preventDefault();
  try {
    const newService = {
      Description: serviceDescription.value
    };
    const response = await createService(newService);

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
            <router-link class="font-medium" to="/services"> Services / </router-link>
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
        <DefaultCard cardTitle="Service Creation Form">
          <form @submit="submitServiceForm">
            <div class="flex flex-col gap-5.5 p-6.5">
              <div>
                <label for="serviceDescription" class="mb-3 block text-sm font-medium text-black dark:text-white">
                  Service Description
                </label>
                <input id="serviceDescription" required
                  v-model="serviceDescription"
                  type="text"
                  placeholder="Ex: TikTok Bathroom Cleaning, Rug Restoration, Stuffed Animal Cleaning"
                  class="w-full rounded-lg border-[1.5px] text-black border-stroke bg-transparent py-3 px-5 font-normal outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:text-white dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary"
                />
              </div>
              <button class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                  Add New Service
              </button>      
            </div>
          </form>
        </DefaultCard>
      </div>
  </DefaultLayout>
</template>