# API Gateway Routes

This document lists all REST API routes used in the Serverless E-Commerce backend.

---

## 1. GET /products
Returns the complete list of products stored in DynamoDB.

### Method:
GET

### Request:
No request body required.

### Success Response (200):
```json
{
  "products": [
    {
      "product_id": "p1",
      "name": "Sample Product",
      "price": 100,
      "description": "Product description here"
    }
  ]
}
```

---

## 2. GET /products/{product_id}
Fetch a single product by ID.

### Method:
GET

### Path Parameter:
- **product_id** → The ID of the product (e.g., "p1")

### Success Response (200):
```json
{
  "product": {
    "product_id": "p1",
    "name": "Sample Product",
    "price": 100,
    "description": "Product description here"
  }
}
```

---

## 3. POST /order
Create a new order and send a confirmation email.

### Method:
POST

### Body:
```json
{
  "email": "user1@gmail.com",
  "product_id": "p1",
  "quantity": 1
}
```

### Success Response (200):
```json
{
  "message": "Order placed successfully",

}
```

### Error Response (500):
```json
{
  "error": "Reason for failure"
}
```

---
