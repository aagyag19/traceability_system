# Product Management and Traceability Information System for Agricultural Cooperatives
## Project Overview
The Product Management and Traceability Information System for Agricultural Cooperatives is a web-based system developed to enable agricultural cooperatives in Nepal to digitally manage and track packaged agro-products throughout different stages of the supply chain.

The system centralizes information related to farmers, produce deliveries, quality inspections, product batches, processing, and packaging. It also allows consumers to access product traceability information using batch numbers or QR codes.

The project was developed as a sixth-semester academic project using the Incremental Development Model.

## Problem Statement
Agricultural cooperatives may face difficulties in maintaining accurate and well-organized records throughout the product lifecycle. Manual record keeping and fragmented information can make it difficult to trace products and provide consumers with clear information about their origin.

This project addresses these challenges by providing a centralized web-based system for managing product information and improving traceability.

## Objectives
* Establish a centralized database for managing agricultural product information.
* Digitize farmer and produce delivery records.
* Record and manage product quality checks.
* Create and manage product batches.
* Maintain records of processing and packaging activities.
* Generate unique QR codes for product batches.
* Allow consumers to verify product information using batch numbers or QR codes.
* Provide a centralized system for cooperative staff to manage traceability records.
* Generate reports related to farmers, batches, and production activities.

## Key Features
### Farmer Management
* Register and manage farmer information.
* Record produce deliveries associated with farmers.

### Quality Check Management
* Record quality inspection information for delivered produce.
* Maintain quality-related records for traceability.

### Batch Management
* Create and manage product batches.
* Store important batch details such as product information and dates.
* Maintain relationships between batches and their source records.

### Processing, Packaging & Distribution
* Record processing activities associated with product batches.
* Maintain packaging information for traceability.
* Record distribution of batches to recipients and destinations.

### QR Code Traceability
* Generate a unique QR code for each product batch.
* Scan the QR code with a phone camera to open the batch's verification page.
* Retrieve the corresponding batch information after scanning.

### Consumer Verification
* Allow consumers to search for product information using a batch number.
* Allow consumers to scan a product QR code to access its traceability information.
* Consumer verification does not require an account.

### Authentication
* Provide secure login for cooperative staff.
* Restrict access to the management system to authorized users.
* Provide logout functionality for authenticated users.

## System Workflow
```text
Cooperative
↓
Farmer
↓
Produce Delivery
↓
Quality Check
↓
Batch Creation
↓
Processing
↓
Packaging
↓
Distribution
↓
QR Code Generation
↓
Consumer Verification
```

## Technology Stack
### Frontend
* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend
* Python
* Django

### Database
* MySQL

### Additional Tools
* QR Code generation and scanning libraries
* Visual Studio Code
* Git
* GitHub

## User Access
The system primarily allows cooperative staff and administrators to manage records and product traceability information.
Consumers do not need to create an account. They can access relevant product information through the public verification interface using a batch number or QR code.

## Project Structure
```text
sixth_sem_project/
│
├── manage.py
├── README.md
├── requirements.txt
├── .env.example          # copy to .env and fill in your values
│
├── config/               # project settings, root URLs, WSGI/ASGI
│
├── products/             # main app
│   ├── models.py         # Cooperative, Farmer, Product, Delivery, QualityCheck,
│   │                     # Batch, Processing, Packaging, Distribution
│   ├── views.py
│   ├── urls.py
│   └── static/products/css/site.css
│
└── templates/            # HTML templates (base, dashboard, lists, forms, public verify page)
```

## Installation and Setup
### 1. Clone the repository

```bash
git clone https://github.com/aagyag19/traceability_system.git
cd traceability_system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the MySQL database
Log in to MySQL and create an empty database:

```sql
CREATE DATABASE agro_products CHARACTER SET utf8mb4;
```

### 6. Configure environment variables
Copy `.env.example` to `.env` and fill in your values.
The `.env` file holds secrets and must never be committed to Git.

### 7. Apply migrations
```bash
python manage.py migrate
```

### 8. Create a staff account
```bash
python manage.py createsuperuser
```

### 9. Start the development server
```bash
python manage.py runserver
```

Then open the application in your browser:
http://127.0.0.1:8000/

Staff log in at `/login/`. The public verification page is at `/verify/`.

## Using QR codes on a phone
A QR code stores the address of the batch's verification page, so the phone must be able to reach the server.

1. Connect the computer and the phone to the same Wi-Fi network (or put the computer on the phone's hotspot).
2. Find the computer's IP address (`ipconfig` on Windows).
3. In `.env`, add that IP to `DJANGO_ALLOWED_HOSTS` and set `SITE_BASE_URL=http://<ip>:8000`.
4. Allow port 8000 through the firewall and start the server with:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
5. Open a batch's QR code in the app, then scan it with the phone's camera app and tap the link.

QR codes contain the address that was set when they were generated. If the IP or `SITE_BASE_URL` changes, generate and print the QR codes again.

For QR codes that work from anywhere, deploy the application to an online host and set `SITE_BASE_URL` to its public HTTPS address. Browsers only allow the in-page camera scanner on HTTPS, so on a local HTTP address use the phone's camera app instead.

## Screenshots

### Home page
![Home page](screenshots/home.png)

### Login
![Login](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Farmer management
![Farmers](screenshots/farmers.png)

### Batch management
![Batches](screenshots/batches.png)

### Generated QR code
![QR code](screenshots/qr.png)

### Consumer verification
![Verification page](screenshots/verify.png)

### Mobile view
![Mobile view](screenshots/mobile.png)

## Expected Outcomes
The completed system is expected to provide:
* A web-based traceability solution designed for agricultural cooperatives.
* Centralized and well-organized product records.
* Improved traceability of packaged agro-products.
* Greater transparency for consumers.
* Easier management of cooperative records.
* A foundation for improved reporting and decision-making.

## References
* Aung, M. M., & Chang, Y. S. (2014). *Traceability in a Food Supply Chain: Safety and Quality Perspectives*.
* Xu, Y., & Gao, X. (2015). *QR Code-Based Traceability Systems*.
* Paraforos, D. S., et al. (2016). *Farm Management Information Systems*.
* Bhatta, G. D., Doppler, W., & KC, K. B. (2009). *Organic Agriculture in Nepal*.

## Project
Academic Project – BIM, Tribhuvan University

Status: Completed (academic submission)
