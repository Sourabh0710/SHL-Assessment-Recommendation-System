# SHL-Assessment-Recommendation-System

Generative AI powered semantic recommendation engine


## Overview

Hiring managers and recruiters often struggle to identify the most suitable assessments for a given role.  
This project solves that problem by using **Generative AI techniques** to semantically match job descriptions with SHL assessments.

Instead of relying on keyword matching, the system understands **context and intent**, producing accurate and ranked assessment recommendations.

---

##  Generative AI Approach

- Uses a **pre-trained transformer-based language model** (`all-MiniLM-L6-v2`)
- Converts job descriptions and SHL assessments into **dense semantic embeddings**
- Computes **cosine similarity** to rank relevant assessments
- No LLM is trained from scratch (industry best practice)

This approach ensures efficiency, scalability, and strong semantic performance.

---

##  System Architecture

<img width="798" height="911" alt="Screenshot 2025-12-18 161755" src="https://github.com/user-attachments/assets/4ff74a81-2b6c-4313-9f54-dc40b0cd3bf5" />


### Flow Explanation

1. **User / Evaluator**
   - Enters job description text
   - Requests top-K assessment recommendations

2. **Streamlit UI (`app.py`)**
   - Collects user input
   - Sends request to REST API
   - Displays ranked results
   - Allows CSV download

3. **FastAPI Backend (`api.py`)**
   - Exposes `/recommend` endpoint
   - Handles request validation
   - Returns results in JSON format

4. **Recommendation Engine (`recommender.py`)**
   - Encodes text using transformer model
   - Computes cosine similarity
   - Ranks SHL assessments

5. **SHL Assessment Catalog (`shl_catalog.csv`)**
   - Cleaned and validated dataset
   - Used for recommendation lookup

---

##  Features

-  Semantic job-to-assessment matching
-  Transformer-based LLM embeddings
-  Cosine similarity ranking
-  REST API with JSON response
-  Interactive Streamlit UI
-  CSV download support
-  Validated and cleaned dataset
-  Ready for cloud deployment

---
## Setup & Installation
### 1️ Clone the Repository
git clone https://github.com/Sourabh0710/SHL-Assessment-Recommendation-System (for streamlit) & https://github.com/Sourabh0710/SHL-Assessment-Recommendation-System-Backend/tree/main ( for backend) 
cd SHL-Assessment-Recommendation

### 2️ Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate

### 3️ Install Dependencies
pip install -r requirements.txt

### Running the Project Locally
Start FastAPI Backend
uvicorn api:app --reload


API Docs: https://shl-assessment-recommendation-system-462r.onrender.com/docs

Start Streamlit App
streamlit run app.py

App URL: http://localhost:8501

---
## Data Validation & Cleaning

### fix_shl_csv.py
Cleans raw SHL assessment data
Filters invalid entries
Standardizes test types

### validate_csv.py
Validates column schema
Checks missing values
Ensures dataset consistency
---

##  Demo

### Streamlit Web App
- Users enter a job description
- Select number of recommendations (max 10)
- View ranked SHL assessments
- Download results as CSV

### API (Swagger UI)
- Interactive API documentation
- Try `/recommend` endpoint directly
- JSON-based responses
---
## Project Structure

- app.py : Streamlit UI
- api.py : FastAPI REST API
- recommender.py: Recommendation engine (LLM + similarity)
- hl_catalog.csv : Cleaned SHL assessment dataset
- fix_shl_csv.py : Dataset cleaning script
- validate_csv.py : Dataset validation script
- requirements.txt : Python dependencies
- architecture.png : System architecture diagram
- README.md : Project documentation
---
## Technologies Used
- Python 3.11
- FastAPI – REST API framework
- Streamlit – Web UI
- Sentence-Transformers – Transformer-based embeddings
- scikit-learn – Cosine similarity
- Pandas & NumPy – Data processing
- Uvicorn – ASGI server
