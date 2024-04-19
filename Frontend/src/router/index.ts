import { createRouter, createWebHistory } from 'vue-router'

import SigninView from '@/views/Authentication/SigninView.vue'
import SignupView from '@/views/Authentication/SignupView.vue'
import CalendarView from '@/views/CalendarView.vue'
import BasicChartView from '@/views/Charts/BasicChartView.vue'
import GlanceView from '@/views/Dashboard/GlanceView.vue'
import FormElementsView from '@/views/Forms/FormElementsView.vue'
import FormLayoutView from '@/views/Forms/FormLayoutView.vue'
import SettingsView from '@/views/SettingsView.vue'
import ProfileView from '@/views/ProfileView.vue'
import TablesView from '@/views/TablesView.vue'
import AlertsView from '@/views/UIElements/AlertsView.vue'
import ButtonsView from '@/views/UIElements/ButtonsView.vue'
import EmployeesView from '@/views/Employees/EmployeesView.vue'
import ClientsView from '@/views/Clients/ClientsView.vue'
import ServicesView from '@/views/Services/ServicesView.vue'
import JanitorialAccountsView from '@/views/JanitorialAccounts/JanitorialAccountsView.vue'
import WorkOrdersView from '@/views/WorkOrders/WorkOrdersView.vue'
import InvoicesView from '@/views/Invoices/InvoicesView.vue'
import InvoiceDetailsView from '@/views/Invoices/InvoiceDetailsView.vue'
import EmployeeIncidentsView from '@/views/Incidents/EmployeeIncidentsView.vue'
import ServiceIncidentsView from '@/views/Incidents/ServiceIncidentsView.vue'

const routes = [
  {
    path: '/',
    name: 'GlanceView',
    component: GlanceView,
    meta: {
      title: 'Dashboard'
    }
  },
  {
    path: '/calendar',
    name: 'Calendar',
    component: CalendarView,
    meta: {
      title: 'Calendar'
    }
  },
  {
    path: '/employees',
    name: 'Employees',
    component: EmployeesView,
    meta: {
      title: 'Employees'
    }
  },
  {
    path: '/clients',
    name: 'Clients',
    component: ClientsView,
    meta: {
      title: 'Clients'
    }
  },
  {
    path: '/services',
    name: 'Services',
    component: ServicesView,
    meta: {
      title: 'Services'
    }
  },
  {
    path: '/accounts',
    name: 'Accounts',
    component: JanitorialAccountsView,
    meta: {
      title: 'Janitorial Accounts'
    }
  },
  {
    path: '/workorders',
    name: 'Workorders',
    component: WorkOrdersView,
    meta: {
      title: 'Work Orders'
    }
  },
  {
    path: '/invoices',
    name: 'Invoices',
    component: InvoicesView,
    meta: {
      title: 'Invoices'
    }
  },
  {
    path: '/invoicedetails/:invoiceID',
    name: 'InvoiceDetails',
    props: true,
    component: InvoiceDetailsView,
    meta: {
      title: 'Invoice Details'
    }
  },
  {
    path: '/employeeincidents',
    name: 'Employeeincidents',
    component: EmployeeIncidentsView,
    meta: {
      title: 'Employee Incidents'
    }
  },
  {
    path: '/serviceincidents',
    name: 'Serviceincidents',
    component: ServiceIncidentsView,
    meta: {
      title: 'Service Incidents'
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: {
      title: 'Profile'
    }
  },
  {
    path: '/forms/form-elements',
    name: 'FormElements',
    component: FormElementsView,
    meta: {
      title: 'Form Elements'
    }
  },
  {
    path: '/forms/form-layout',
    name: 'FormLayout',
    component: FormLayoutView,
    meta: {
      title: 'Form Layout'
    }
  },
  {
    path: '/tables',
    name: 'Tables',
    component: TablesView,
    meta: {
      title: 'Tables'
    }
  },
  {
    path: '/settings',
    name: 'Settings',
    component: SettingsView,
    meta: {
      title: 'Settings'
    }
  },
  {
    path: '/charts/basic-chart',
    name: 'BasicChart',
    component: BasicChartView,
    meta: {
      title: 'Basic Chart'
    }
  },
  {
    path: '/ui-elements/alerts',
    name: 'Alerts',
    component: AlertsView,
    meta: {
      title: 'Alerts'
    }
  },
  {
    path: '/ui-elements/buttons',
    name: 'Buttons',
    component: ButtonsView,
    meta: {
      title: 'Buttons'
    }
  },
  {
    path: '/auth/signin',
    name: 'Signin',
    component: SigninView,
    meta: {
      title: 'Signin'
    }
  },
  {
    path: '/auth/signup',
    name: 'Signup',
    component: SignupView,
    meta: {
      title: 'Signup'
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { left: 0, top: 0 }
  }
})

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} | JADiaz Dashboard`
  next()
})

export default router
