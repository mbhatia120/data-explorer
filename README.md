# Data Explorer
This repository contains the solution to the backend/data assignment for creating a data explorer that allows data analysts to run queries and analysis on uploaded CSV data.

## Deployed solution
-Frontend : https://silly-kelpie-6b31ec.netlify.app/
-Backend : https://backend-game-production.up.railway.app/

## Problem Statement
The goal is to build a system that can:
- Accept a link to a CSV file and store the data.
- Provide a data explorer API to run queries on the stored CSV data.
- Ensure the solution is scalable, performant, and easy to deploy.

## Technologies Used

- **Frontend:** React (Vite)
- **Backend:** Flask
- **Database:** PostgreSQL
- **Deployment:** Docker, Cloud provider (free tier - Netlify and Railways)

## Architecture

This project follows a 3-tier architecture:
- **Client**: React-based interface for interaction with the API.
- **Backend**: Flask server that handles API requests and connects to the PostgreSQL database.
- **Database**: PostgreSQL used to store and query CSV data.

## Features

- Upload and store CSV data using a public link.
- Query data using any field from the CSV, including substring matches for string fields and exact matches for numerical fields.
- Supports pagination for large datasets.
- Deployed on a cloud provider, accessible through a simple UI.

## Setting up the project
This web app is made using **Flask, Postgres, React vite** stack.

```bash
# Clone the repo
git clone https://github.com/mbhatia120/data-explorer.git

# For Server
cd api
npm install
docker-compose up --build 


# For Client

npm install
npm run start
sudo npm run dev 

# Server runs on http://localhost:5000 and Client on http://localhost:5173

#For env variables

#copy .env.example and make your own .env file for both server and client
```

## Project flow and assumptions
- A user comes on the webpage, they need to give username(unique) and public link to csv file
- The data will be stored in the postgres sql.
- Let say user u1 comes gives 100 entries and then u2 comes and gives 50 entries, all this will be stored in the database
- Assumption that u1 come up with another csv and it has some entry similar to the previous 100 entries, then data with respect to those entries will be updated in the database. (overwritten)
- EG Initially - app id:123, price: $3 -------> updated to app id:123, price:$5
- After user has provided the data it will redirect to /:username and by default all entries will be visible.
- search column will be visible and after submitting the parameters a query will be initiated and results will be displayed on the frontend.

## Cost Estimation for Running the System 24x7 in Production

The following is an estimate of the cost for running this system in production on **Netlify** (frontend) and **Railway** (backend and database), 24x7 for 30 days, assuming one file upload (50 MB) and 100 queries per day.

### Infrastructure Components:
1. **Frontend (React App)**: 
   - Hosted on Netlify
   - Estimated Cost: $0 (free tier)

2. **Backend (Flask Service)**: 
   - Hosted on Railway
   - Estimated Cost: ~$5 to $10/month (depending on runtime)

3. **Database (PostgreSQL)**:
   - Hosted on Railway (free tier: 500 MB)
   - Estimated Cost: $0 (within free tier)

### Total Estimated Cost:
- **~$5 to $10/month**

This estimate assumes low traffic and usage. Costs may vary based on actual usage and pricing changes from Netlify and Railway.
