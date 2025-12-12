import { axiosInstance } from "./api";

/**
 * Service for managing Categories.
 * Endpoints:
 * - GET /categorias/ : List
 * - POST /categorias/ : Create
 * - PUT /categorias/<id>/ : Update
 * - DELETE /categorias/<id>/ : Delete
 */

const CategoryService = {
  async getAll() {
    try {
      const response = await axiosInstance.get("/categorias/");
      // Handle pagination result
      if (response.data && response.data.results) {
        return response.data.results;
      }
      return response.data;
    } catch (error) {
      console.error("Error fetching categories:", error);
      throw error;
    }
  },

  async getById(id) {
    try {
      const response = await axiosInstance.get(`/categorias/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching category ${id}:`, error);
      throw error;
    }
  },

  async create(data) {
    try {
      const response = await axiosInstance.post("/categorias/", data);
      return response.data;
    } catch (error) {
      console.error("Error creating category:", error);
      throw error;
    }
  },

  async update(id, data) {
    try {
      const response = await axiosInstance.put(`/categorias/${id}/`, data);
      return response.data;
    } catch (error) {
      console.error(`Error updating category ${id}:`, error);
      throw error;
    }
  },

  async delete(id) {
    try {
      await axiosInstance.delete(`/categorias/${id}/`);
    } catch (error) {
      console.error(`Error deleting category ${id}:`, error);
      throw error;
    }
  },
};

export default CategoryService;
