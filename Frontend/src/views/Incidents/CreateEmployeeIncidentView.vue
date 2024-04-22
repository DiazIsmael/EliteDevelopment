<script setup lang="ts">
import { ref } from 'vue'
import { createEmployeeIncident } from '@/api/api.js'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import AlertError from '@/components/Alerts/AlertError.vue'
import InputGroup from '@/components/Forms/InputGroup.vue'
import DatePickerOne from '@/components/Forms/DatePicker/DatePickerOne.vue'
import EmployeeDropdown from '@/components/Forms/Dropdowns/EmployeeDropdown.vue'
import IncidentStatusDropdown from '@/components/Forms/Dropdowns/IncidentStatusDropdown.vue'

const pageTitle = ref('New Employee Incident')
const formStatus = ref('')
const showSuccessAlert = ref(false)
const showErrorAlert = ref(false)
const newEmployeeIncident = ref({
  EmployeeID: 0,
  Description: '',
  Resolution: '',
  Date: '',
  StatusCode: 0
})

const submitEmployeeIncidentForm = async (event) => {
  console.log(newEmployeeIncident.value);
  event.preventDefault();
  if (!newEmployeeIncident.value.EmployeeID || !newEmployeeIncident.value.Description || !newEmployeeIncident.value.Date || !newEmployeeIncident.value.StatusCode) {
    alert("Please fill all required fields.");
    return;
  }
  try {
    const EmployeeIncidentData = {
      EmployeeID: newEmployeeIncident.value.EmployeeID,
      Description: newEmployeeIncident.value.Description,
      Resolution: newEmployeeIncident.value.Resolution,
      Date: newEmployeeIncident.value.Date,
      StatusCode: newEmployeeIncident.value.StatusCode
    };
    const response = await createEmployeeIncident(EmployeeIncidentData);

    if (response == "Query successfully executed!") {
      formStatus.value = 'Employee Created Successfully';
      showSuccessAlert.value = true;
    }
    else if (response != "Query successfully executed!") {
      formStatus.value = 'Error Creating Employee';
      showErrorAlert.value = true;
    }
  } catch (error) {
    formStatus.value = 'Error Creating Employee';
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
            <router-link class="font-medium" to="/employeeincidents"> Employee Incidents / </router-link>
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
        <DefaultCard cardTitle="Incident Creation Form">
          <form @submit="submitEmployeeIncidentForm">
            <div class="flex flex-col gap-5.5 p-6.5">

              <div class="mb-4.5 justify-center flex flex-col gap-6 xl:flex-row">
                <EmployeeDropdown required class="w-full xl:w-1/2" v-model="newEmployeeIncident.EmployeeID"/>
              </div>

              <DatePickerOne required v-model="newEmployeeIncident.Date"/>

              <InputGroup
                required
                v-model="newEmployeeIncident.Description"
                label="Description"
                type="text"
                placeholder="Enter the incident's description"
                customClasses="mb-4.5"
              />

              <InputGroup
                v-model="newEmployeeIncident.Resolution"
                label="Resolution"
                type="text"
                placeholder="Enter the incident's resolution"
                customClasses="mb-4.5"
              />

              <div class="mb-4.5 flex flex-col justify-center gap-6 xl:flex-row">
                <IncidentStatusDropdown class="w-full xl:w-1/2" v-model="newEmployeeIncident.StatusCode"/>
              </div>

              <!-- Form Submit Button -->
              <button class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                  Create Employee Incident
              </button>      
            </div>
          </form>
        </DefaultCard>
      </div>
  </DefaultLayout>
</template>