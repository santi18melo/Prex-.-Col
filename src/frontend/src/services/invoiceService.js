import { axiosInstance } from "./api";

/**
 * Service for managing Invoices (Facturas).
 * Endpoints:
 * - GET /facturas/ : List
 * - GET /facturas/<id>/ : Detail
 */

const InvoiceService = {
  async getAll() {
    try {
      const response = await axiosInstance.get("/facturas/");
      if (response.data && response.data.results) {
        return response.data.results;
      }
      return response.data;
    } catch (error) {
      console.error("Error fetching invoices:", error);
      throw error;
    }
  },

  async getById(id) {
    try {
      const response = await axiosInstance.get(`/facturas/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching invoice ${id}:`, error);
      throw error;
    }
  },

  // Maybe filter by order ID if supported by backend
  async getByOrderId(orderId) {
    try {
        // This assumes the backend supports filtering by pedido, e.g. /facturas/?pedido=ID
        const response = await axiosInstance.get(`/facturas/?pedido=${orderId}`);
        if(response.data && response.data.results && response.data.results.length > 0) {
            return response.data.results[0];
        } else if (Array.isArray(response.data) && response.data.length > 0) {
            return response.data[0];
        }
        return null; // Not found
    } catch (error) {
        console.error(`Error fetching invoice for order ${orderId}:`, error);
        return null;
    }
  }
};

export default InvoiceService;
