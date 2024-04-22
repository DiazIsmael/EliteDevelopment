<script setup lang="ts">
import { ref } from 'vue'
import { createEmployee } from '@/api/api.js'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import AlertError from '@/components/Alerts/AlertError.vue'
import InputGroup from '@/components/Forms/InputGroup.vue'
import EmployeeStatusDropdown from '@/components/Forms/Dropdowns/EmployeeStatusDropdown.vue'

const pageTitle = ref('New Employee')
const formStatus = ref('')
const showSuccessAlert = ref(false)
const showErrorAlert = ref(false)
const newEmployee = ref({
  FirstName: '',
  LastName: '',
  Phone: '',
  Email: '',
  Address: '',
  StatusCode: 1
})

const submitEmployeeForm = async (event) => {
  event.preventDefault();
  if (!newEmployee.value.FirstName || !newEmployee.value.LastName || !newEmployee.value.Phone || !newEmployee.value.Email || !newEmployee.value.Address || !newEmployee.value.StatusCode) {
    alert("Please fill all required fields.");
    return;
  }
  try {
    const employeeData = {
      FirstName: newEmployee.value.FirstName,
      LastName: newEmployee.value.LastName,
      Phone: newEmployee.value.Phone,
      Email: newEmployee.value.Email,
      Address: newEmployee.value.Address,
      StatusCode: newEmployee.value.StatusCode
    };
    const response = await createEmployee(employeeData);

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
            <router-link class="font-medium" to="/employees"> Employees / </router-link>
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
        <DefaultCard cardTitle="Employee Creation Form">
          <form @submit="submitEmployeeForm">
            <div class="flex flex-col gap-5.5 p-6.5">
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newEmployee.FirstName"
                  label="First Name"
                  type="text"
                  placeholder="Enter employee's first name"
                  customClasses="w-full xl:w-1/2"
                />

                <InputGroup
                  required
                  v-model="newEmployee.LastName"
                  label="Last Name"
                  type="text"
                  placeholder="Enter the employee's last name"
                  customClasses="w-full xl:w-1/2"
                />
              </div>

              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup
                  required
                  v-model="newEmployee.Phone"
                  label="Phone Number"
                  type="text"
                  placeholder="Enter the employee's phone number"
                  customClasses="w-full xl:w-1/2"
                />
                
                <InputGroup
                  required
                  v-model="newEmployee.Email"
                  label="Email"
                  type="email"
                  placeholder="Enter the employee's email address"
                  customClasses="w-full xl:w-1/2"
                />
              </div>
              <InputGroup
                required
                v-model="newEmployee.Address"
                label="Address"
                type="text"
                placeholder="Enter the employee's address"
                customClasses="mb-4.5"
              />

              <div class="mb-4.5 flex flex-col justify-center gap-6 xl:flex-row">
                <EmployeeStatusDropdown required class="w-full xl:w-1/2" v-model="newEmployee.StatusCode"/>
              </div>

              <!-- Form Submit Button -->
              <button class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                  Add New Employee
              </button>      
            </div>
          </form>
        </DefaultCard>
      </div>
  </DefaultLayout>
</template>