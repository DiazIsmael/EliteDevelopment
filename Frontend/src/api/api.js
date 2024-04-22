/* eslint-disable no-useless-catch */
// This file contains all API calls to the API endpoints
// import axios to make API calls
import axios from "axios";

// Create HTTP client with the base URL, and specify that the data sent in the request body is JSON
const apiClient = axios.create({
  baseURL: "http://localhost:5000",
  headers: {
    "Content-Type": "application/json"
  }
});

// --Login related API calls-- //

// If user logs in successfully, this login sets a header to "apiClient" called "Authorization" with the value of "Bearer <token>" This security token is used to validate API calls
function setAuthHeader(token) {
  apiClient.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}

// When user logs out, this function removes the Authorization header from apiClient
function removeAuthHeader() {
  delete apiClient.defaults.headers.common["Authorization"];
}

// parsing out error messages from API calls see https://stackoverflow.com/questions/67089014/how-to-read-error-messages-from-javascript-error-object
function getErrorMessageFromResponseBody(string) {
  let errorString = string;

  try {
    let json = JSON.parse(string);
    if (json.errors) {
      errorString = json.errors[0].msg;
    }
  } catch (parseOrAccessError) {
    console.error(parseOrAccessError);
  }

  return errorString;
}

// API call to log the user in
export async function loginUser(username, password) {
  try {
    const response = await apiClient.post("/users/login", {
      username,
      password,
    });
    const token = response.data.token;
    localStorage.setItem("authToken", token);
    setAuthHeader(token);
    return token;
  } catch (error) {
    if (error.response.status === 400) {
      let errorString = getErrorMessageFromResponseBody(
        error.response.data.message
      );
      throw new Error(errorString); // API errors get thrown here
    } else throw error;
  }
}

// API call to log the user out
export function logoutUser() {
  localStorage.removeItem("authToken");
  removeAuthHeader();
}

// --Org related API calls-- //

// API call to GET org name
export async function getOrgName() {
  const response = await apiClient.get(`/org`);
  return response.data;
};

// -- Employees related API calls-- //

// API call to GET all Employees
export const getEmployees = async () => {
  try {
    const response = await apiClient.get("/api/employee/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to GET all Employee Statuses
export const getEmployeeStatus = async () => {
  try {
    const response = await apiClient.get("/api/employeestatus/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new Employee
export const createEmployee = async (newEmployee) => {
  try {
    const response = await apiClient.post("/api/employee/add", newEmployee);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --Clients related API calls-- //

// API call to GET all Clients
export const getClients = async () => {
  try {
    const response = await apiClient.get("/api/client/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to GET all Client Statuses
export const getClientStatus = async () => {
  try {
    const response = await apiClient.get("/api/clientstatus/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to GET all Client Types
export const getClientTypes = async () => {
  try {
    const response = await apiClient.get("/api/clienttype/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new Client
export const createClient = async (newClient) => {
  const currentDate = new Date();
  const formattedDate = currentDate.getFullYear() + '-' + 
                        ('0' + (currentDate.getMonth() + 1)).slice(-2) + '-' + 
                        ('0' + currentDate.getDate()).slice(-2);

  newClient.AddedDate = formattedDate;

  try {
    const response = await apiClient.post("/api/client/add", newClient);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// THE REST OF THESE CLIENT ONES WERE INCLUDED IN TEMPLATE, BUT MAY SERVE USEFUL L8R //
// API call to GET single client by ID
export const getClientById = async (id) => {
  try {
    const response = await apiClient.get(`/clients/id/${id}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to GET entries based on search query
export const searchClients = async (query) => {
  try {
    let params = {};
    if (query.searchBy === "name") {
      params.searchBy = query.searchBy;
      params.firstName = query.firstName || "";
      params.lastName = query.lastName || "";
    } else if (query.searchBy === "number") {
      params.searchBy = query.searchBy;
      params.phoneNumber = query.phoneNumber || "";
    }
    const response = await apiClient.get("/clients/search", {
      params: params,
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to PUT update client
export const updateClient = async (id, updatedClient) => {
  try {
    const response = await apiClient.put(
      `/clients/update/${id}`,
      updatedClient
    );
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to delete client
export const deleteClientbyId = async (id) => {
  try {
    const response = await apiClient.delete(`/clients/${id}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --Service related API calls-- //

// API call to GET all Services
export const getServices = async () => {
  try {
    const response = await apiClient.get("/api/service/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new service
export const createService = async (newService) => {
  try {
    const response = await apiClient.post("/api/service/add", newService);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to PUT update service
export const updateService = async (id, updatedService) => {
  try {
    const response = await apiClient.put(`/services/update/${id}`, updatedService);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to DELETE service by ID
export const deleteService = async (id) => {
  try {
    const response = await apiClient.delete(`/services/${id}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --Janitorial Account related API calls-- //

// API call to GET all Janitorial Accounts
export const getJanitorialAccounts = async () => {
  try {
    const response = await apiClient.get("/api/janitorialaccount/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to GET all Client Statuses
export const getAccountStatus = async () => {
  try {
    const response = await apiClient.get("/api/accountstatus/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new Janitorial Account
export const createJanitorialAccount = async (newAccount) => {
  try {
    const response = await apiClient.post("/api/janitorialaccount/add", newAccount);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --Work Order related API calls-- //

// API call to GET all Work Orders
export const getWorkOrders = async () => {
  try {
    const response = await apiClient.get("/api/workorder/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new Work Order
export const createWorkOrder = async (newWorkOrder) => {
  try {
    const response = await apiClient.post("/api/janitorialaccount/add", newWorkOrder);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --Invoices related API calls-- //

// API call to GET all Invoices
export const getInvoices = async () => {
  try {
    const response = await apiClient.get("/api/invoice/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Incident related API calls-- //

// API call to GET all Service Incidents
export const getServiceIncidents = async () => {
  try {
    const response = await apiClient.get("/api/serviceincident/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getIncidentStatus = async () => {
  try {
    const response = await apiClient.get("/api/incidentstatus/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to GET all Employee Incidents
export const getEmployeeIncidents = async () => {
  try {
    const response = await apiClient.get("/api/employeeincident/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new Service Incident
export const createServiceIncident = async (newIncident) => {
  try {
    const response = await apiClient.post("/api/serviceincident/add", newIncident);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to POST new Service Incident
export const createEmployeeIncident = async (newIncident) => {
  try {
    const response = await apiClient.post("/api/employeeincident/add", newIncident);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --Reports/Views related API calls-- //

// API call to GET all InvoiceDetailsView
export const getInvoiceDetails = async (invoiceID) => {
  try {
    const response = await apiClient.get(`/report/invoicedetails/${invoiceID}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Uploads related API calls (FROM TEMPLATE)-- //

// API call to GET the image path for a client by their imageID
export const getClientImagePath = async (imageID) => {
  try {
    const response = await apiClient.get(`/uploads/${imageID}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// API call to POST new image for a client by passing clientID and imageFile
export const uploadImage = async (formData) => {
  try {
    const response = await apiClient.post(`/uploads/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to DELETE image path for a client by passing clientID and imageFile
export const deleteImage = async (clientID) => {
  try {
    const response = await apiClient.delete(`/uploads/delete/${clientID}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// --API calls related to services (FROM TEMPLATE)-- //

// API call to GET all services for org
export const getService = async () => {
  try {
    const response = await apiClient.get("/services/");
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to GET single service by ID
export const getServiceById = async (id) => {
  try {
    const response = await apiClient.get(`/services/id/${id}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to GET services based on search query
export const searchServices = async (query) => {
  try {
    let params = {};
    params.searchBy = query.searchBy;
    if (query.searchBy === "name") {
      params.name = query.name || "";
    } else if (query.searchBy === "description") {
      params.description = query.description;
    }
    const response = await apiClient.get("/services/search", {
      params: params,
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};