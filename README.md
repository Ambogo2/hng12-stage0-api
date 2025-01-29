# HNG12 Stage 0 - Public API

This is a simple FastAPI backend for the HNG12 internship.

## API Endpoint
**Base URL:** `https://hng12-stage0-api-nw4x.onrender.com/`

**Response Example**
```json
{
"current_datetime": "2025-01-29T16:20:44.315708+00:00",
"email": "ruthambogo.ra@gmail.com",
"github_url": "https://github.com/Ambogo2/hng12-stage0-api.git"
}
```
## Setup & Installation
** clone the repository **
```git clone https://github.com/Ambogo2/hng12-stage0-api.git
cd hng12-stage0-api
```
## Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies
```
pip install -r requirements.txt
```
## Run the Flask App Locally

```python app.py```
By default, the app runs on `http://127.0.0.1:5000.`

## Deployment
This API is deployed on Render. The deployed version can be accessed at:
`https://hng12-stage0-api-nw4x.onrender.com/`

