# Example API Requests (Postman)

This document shows how to test the Serverless E-Commerce Backend using Postman.

---

## 1. Get All Products  
**Method:** GET  
**URL:** https://your-api-id.execute-api.us-east-1.amazonaws.com/ServerlessEcommerceAPI/products  

### Postman Steps:
1. Open Postman → New → HTTP Request  
2. Select **GET**  
3. Paste the URL  
4. Click **Send**

or

### Web Browser Steps:
1.Directly place the **url** in the search bar

---

## 2. Get Product by ID  
**Method:** GET  
**URL:** https://your-api-id.execute-api.us-east-1.amazonaws.com/ServerlessEcommerceAPI/products/p1  

### Postman Steps:
1. Set method to **GET**  
2. Paste URL  
3. Replace `p1` with any product ID  
4. Click **Send**

---

## 3. Create Order  
**Method:** POST  
**URL:** https://your-api-id.execute-api.us-east-1.amazonaws.com/ServerlessEcommerceAPI/order  
**Headers:**  
`Content-Type: application/json`

### **Body (Postman → Body → raw → JSON):**

```json
{
  "email": "user1@gmail.com",
  "product_id": "p1",
  "quantity": 1
}
