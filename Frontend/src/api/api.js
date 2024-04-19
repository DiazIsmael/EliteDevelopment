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

// API call to get org name
export async function getOrgName() {
  const response = await apiClient.get(`/org`);
  return response.data;
};

// -- Employees related API calls-- //

// API call to get all Employees
export const getEmployees = async () => {
  try {
    const response = await apiClient.get("/api/employee/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Clients related API calls-- //

// API call to get all Clients
export const getClients = async () => {
  try {
    const response = await apiClient.get("/api/client/all");
    return response.data;
  } catch (error) {
    throw error;
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

// API call to POST new client
export const createClient = async (newClient) => {
  try {
    const response = await apiClient.post("/clients", newClient);
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

// API call to get events for dashboard
export const getClientsByZipCode = async () => {
  try {
    const response = await apiClient.get("/clients/byzip");
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
// --Service related API calls-- //

// API call to get all Services
export const getServices = async () => {
  try {
    const response = await apiClient.get("/api/service/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Janitorial Account related API calls-- //

// API call to get all Janitorial Accounts
export const getJanitorialAccounts = async () => {
  try {
    const response = await apiClient.get("/api/janitorialaccount/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Work Order related API calls-- //

// API call to get all Work Orders
export const getWorkOrders = async () => {
  try {
    const response = await apiClient.get("/api/workorder/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Invoices related API calls-- //

// API call to get all Invoices
export const getInvoices = async () => {
  try {
    const response = await apiClient.get("/api/invoice/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Incident related API calls-- //

// API call to get all EmployeeIncidents
export const getEmployeeIncidents = async () => {
  try {
    const response = await apiClient.get("/api/employeeincident/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getServiceIncidents = async () => {
  try {
    const response = await apiClient.get("/api/serviceincident/all");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// --Reports/Views related API calls-- //

// API call to get all InvoiceDetailsView
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

// API call to get all services for org
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

// API call to POST new service
export const createService = async (newService) => {
  try {
    const response = await apiClient.post("/services", newService);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// API call to PUT update service
export const updateService = async (id, updatedService) => {
  try {
    const response = await apiClient.put(
      `/services/update/${id}`,
      updatedService
    );
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