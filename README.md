# Product Management and Traceability Information System for Agricultural Cooperatives
## Project Overview
The Product Management and Traceability Information System for Agricultural Cooperatives is a web-based system developed to enable agricultural cooperatives in Nepal to digitally manage and track packaged agro-products throughout different stages of the supply chain.

The system centralizes information related to farmers, produce deliveries, quality inspections, product batches, processing, and packaging. It also allows consumers to access product traceability information using batch numbers or QR codes.

The project is being developed as a sixth-semester academic project using the Incremental Development Model.

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

### Processing & Packaging
* Record processing activities associated with product batches.
* Maintain packaging information for traceability.

### QR Code Traceability
* Generate a unique QR code for each product batch.
* Scan QR codes using a device camera.
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
QR Code Generation
↓
Consumer Verification

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
The project follows the standard Django project structure.

sixth_sem_project/
│
├── manage.py
├── README.md
├── requirements.txt
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
├── static/
└── ...

The structure above is a simplified representation and may change as development progresses.

## Installation and Setup
### 1. Clone the repository

```bash
git clone <repository-url>
cd sixth_sem_project
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

### 5. Configure the database
Create a MySQL database and configure the database connection in the Django project's settings.

### 6. Apply migrations
```bash
python manage.py migrate
```

### 7. Start the development server
```bash
python manage.py runserver
```

Then open the application in your browser:
http://127.0.0.1:8000/

## Screenshots
Screenshots of the system will be added here as development progresses.
Planned screenshots include:
* Login page
* Dashboard
* Farmer management
* Batch management
* Batch details
* Generated QR code
* QR code scanner
* Consumer verification page

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
Status: Under Development
