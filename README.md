# Data Explorer
This repository contains the solution to the backend/data assignment for creating a data explorer that allows data analysts to run queries and analysis on uploaded CSV data.

## Deployed solution
- Frontend : https://silly-kelpie-6b31ec.netlify.app/

- Backend : https://backend-game-production.up.railway.app/
  
## Video Link 
- Loom - https://www.loom.com/share/ef1dc1a5b3a34ce18effe60cde39fe3f?sid=465640e1-9178-43ae-ba5f-658a5d9f9516
  
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

## Endpoints

### 1. Home Route (`/home`)
- **Method**: GET
- **Description**: A simple endpoint that returns a greeting message.
- **Response**:
  ```json
  {
    "message": "Hello, World!"
  }
  ```

### 2. Upload CSV Route (`/upload_csv`)
- **Method**: POST
- **Description**: Upload a CSV file containing game data.
- **Request Body**:
  ```json
  {
    "username": "usertest",
    "csv_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSCtraqtnsdYd4FgEfqKsHMR2kiwqX1H9uewvAbuqBmOMSZqTAkSEXwPxWK_8uYQap5omtMrUF1UJAY/pub?gid=1439814054&single=true&output=csv"
  }
  ```
- **Response** (on success):
  ```json
  {
    "message": "CSV data processed successfully"
  }
  ```
- **Response** (on failure):
  ```json
  {
    "error": "Failed to fetch CSV"
  }
  ```

### 3. Get Games by Username Route (`/<username>`)
- **Method**: GET
- **Description**: Get the list of games for a user.
- **Response** (on success):
  ```json
  {
    "username": "user",
    "games": [
      {
        "app_id": 12345,
        "name": "Game Title",
        "release_date": "Oct 21, 2008",
        "required_age": 18,
        "price": 59.99,
        "dlc_count": 3,
        "about_game": "This is a cool game.",
        "supported_languages": "English, French",
        "windows": true,
        "mac": false,
        "linux": true,
        "positive_reviews": 1000,
        "negative_reviews": 50,
        "score_rank": 95,
        "developers": "Game Studio",
        "publishers": "Game Publisher",
        "categories": "Action, Adventure",
        "genres": "RPG",
        "tags": "Open World, Story Rich",
        "uploaded_at": "2023-10-22T12:34:56Z"
      }
    ]
  }
  ```
- **Response** (if user not found):
  ```json
  {
    "message": "User not found"
  }
  ```

### 4. Search Games Route (`/api/searchGames`)
- **Method**: POST
- **Description**: Search games based on multiple filters.
- **Request Body**:
  ```json
  {
    "username": "user",
    "price": 59.99,
    "price_condition": "<",
    "tags": "Open World"
  }
  ```
- **Response**:
  ```json
  {
    "games": [
      {
        "app_id": 67890,
        "name": "Another Game",
        "release_date": "May 15, 2012",
        "price": 39.99,
        "required_age": 12,
        "dlc_count": 2,
        "about_game": "A fun open world game.",
        "supported_languages": "English, Spanish",
        "windows": true,
        "mac": false,
        "linux": false,
        "positive_reviews": 800,
        "negative_reviews": 20,
        "score_rank": 90,
        "developers": "Another Studio",
        "publishers": "Another Publisher",
        "categories": "Action, RPG",
        "genres": "Open World",
        "tags": "Adventure, Open World",
        "uploaded_at": "2023-10-21T10:30:00Z"
      }
    ]
  }
  ```

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
