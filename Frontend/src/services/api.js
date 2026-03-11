import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-resume-analyzer-h4f1.onrender.com",
});

export const analyzeResume = async (formData) => {
  const response = await API.post("/analyze", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return response.data;
};

