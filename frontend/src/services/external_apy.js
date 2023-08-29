import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function getRequiredFields() {
  try {
    let response;
    response = await api.get("/proposal-fields");
    return response.data;
  } catch (error) {
    null;
  }
}

export async function createLoanProposal(data) {
  try {
    let response;
    response = await api.post("/loan", data);
    return response;
  } catch (error) {
    throw error;
  }
}
