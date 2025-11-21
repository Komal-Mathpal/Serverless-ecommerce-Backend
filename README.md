# Serverless E-Commerce Backend(AWS)

This is a fully **serverless backend project** built on **AWS Console** to support  .
## About
It powers a simple e-commerce workflow — listing products, fetching a product by ID, and placing an order with email confirmation.

I created this project using the AWS Console (no frameworks), and later organized it into a clean folder structure for GitHub.



 ## Features
 ### 1. Get All Products
Returns the list of all available products stored in DynamoDB (Products table).

 ### 2. Get Product by ID
Fetches a single product using the product_id passed in the API URL.

 ### 3. Create Order
Creates a new order entry in DynamoDB (Orders table)

### Sends an order confirmation email using AWS SES (sandbox-verified emails).

## Tech Stack
Service	Purpose
AWS Lambda	Backend logic (Python)
API Gateway	REST API endpoints
DynamoDB	NoSQL data storage (Products & Orders)
SES	Sending order confirmation emails
IAM	Secure permissions for Lambda functions

## 📁 Project Structure (Manually Organized for GitHub)
- project/
 - lambda/
    - getProducts.py
│   ├── getProductById.py
│   └── createOrder.py
│
├── dynamodb/
│   ├── products-table-structure.json
│   └── orders-table-structure.json
│
├── api/
│   ├── gateway-routes.md
│   └── example-requests.md
│
└── README.md

 ## DynamoDB Tables
 ### Products Table
    Partition Key: product_id
    Contains 2 sample handmade product items
    (Crochet Earrings & Macrame Wall Hanging)

### Orders Table
    Partition Key: order_id
    Stores user order information

    Each order also triggers a confirmation email

## Lambda Functions (Python)
### 1️ getProducts.py
Returns all products from the table.

### 2️ ProductById.py
Uses product_id from URL path to return a single item.

### 3️ createOrder.py
Accepts POST body JSON
Creates a new order in DynamoDB

Sends email using SES
Returns order_id in response

## API Gateway Routes

Your routes may look like this:

Method	Endpoint	Lambda
GET	/products	getProducts
GET	/products/{id}	getProductById
POST	/order	CreateOrder

Full details are included inside:
 api/gateway-routes.md

## Testing the APIs

You can test the API using:

 Postman

(full examples included in
 api/example-requests.md)

Browser

Works for:

GET /products

GET /products/{id}

 AWS CLI

Example:

aws lambda invoke \
  --function-name CreateOrder \
  --payload "{ \"body\": \"{ \\\"email\\\": \\\"test@example.com\\\", \\\"product_id\\\": \\\"p1\\\", \\\"quantity\\\": 1 }\" }" \
  --cli-binary-format raw-in-base64-out \
  response.json \
  --region us-east-1

 SES Email Setup

Since SES sandbox only allows verified emails, I verified:

Sender Email

Receiver Email (the user's email)

Emails are sent upon successful order creation.

How to Run This Project Anywhere

This backend is serverless — no installation needed on the user's computer.

To run it:

Deploy code to Lambda (upload .zip or inline)

Configure API Gateway routes

Connect DynamoDB tables

Verify emails in SES

Test using Postman or browser

No local server or environment required.

Why This Project Is Good for Cloud based post  Resume

 Uses multiple AWS services together
 Demonstrates serverless design
 Real-world e-commerce use case
 Includes IAM, SES, DynamoDB, API Gateway
 Shows API testing, debugging & architecture understanding

 Improvements (Optional)

Add authentication using Cognito

Add pagination for product list

Add status tracking for orders

Build a frontend (React, Next.js or simple HTML)

Implement IaC (CloudFormation / SAM / Terraform)

 Final Note

This repository is structured to make the project understandable, readable, and recruiter-friendly — even though the entire backend was originally built using the AWS Console.

The folder structure simply documents and organizes the system, which is absolutely professional and commonly done for cloud engineers.
