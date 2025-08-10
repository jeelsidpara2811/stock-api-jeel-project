# Stock API
A FastAPI-based backend for retrieving, analyzing, and comparing stock market statistics using yfinance.
Built for high performance and easy deployment with Docker.
---

## Features 
- **Fetch** historical stock market data on demand via yfinance
- **Analyze** current momentum and trends
- **Compare** performance of multiple stocks
- **Preview** basic key metrics: high, low, average, last close
- **Interactive** API docs via Swagger UI (/docs)
- **Docker-ready** for quick deployment

---

##  Project Structure
```
app/
├── main.py # Entry point
├── router/ # API routes
│ ├── compare.py
│ ├── latest.py
│ ├── stats.py
├── services/ # Business logic
│ ├── compare_services.py
│ ├── latest_services.py
│ ├── stats_services.py
test/ # Unit tests
│ ├── test_compare.py
│ ├── test_latest.py
│ ├── test_stats.py
.env                  # Stores enviorment variables
.gitignore            # Exclude unnecessary tracked files
Dockerfile            # Docker setup
README.md             # This file
requirements.txt      # Dependencies
```
---
## Enviorment Variables

This project does not have any secret to hide yet.

## Installation
```
# Clone the repository
git clone https://github.com/jeelsidpara2811/stock-api-jeel-project.git

# Navigate to the project directory
cd stock-api-jeel-project

# Install required Python packages
pip install -r requirements.txt
```
## Run Server
### locally in terminal 
```
python -m uvicorn app.main:app --reload

#use this to run server on web
http://127.0.0.1:8000 
```
### Or with Docker

```
# Build Docker image
docker build -t stock-api .

# Run container on localhost
docker run -p 8000:8000 stock-api

# Then open in browser:
http://localhost:8000/docs
```
## API Endpoint
1. /api/compare - For Comparing stock performance within a specific time range
2. /api/latest - For change monentum 
3. /api/stats - For stock statistics like [high,low,last close]

## Example of API usage

### For compare Endpoint
Request
```
# via URL query parameter and then use pretty-print
http://127.0.0.1:8000/api/compare?ticker1=MSFT&ticker2=GOOGL&start=2023-01-01&end=2023-12-31

# via Swagger UI
http://127.0.0.1:8000/docs 
# Then set ticker1=MSFT, ticker2=GOOGL, start=2023-01-01, end=2023-12-31
```
Response
```
{
  "MSFT": {
    "high": 384.3,
    "low": 219.35,
    "average": 313.95,
    "last_close": 376.04
  },
  "GOOGL": {
    "high": 142.68,
    "low": 84.86,
    "average": 118.79,
    "last_close": 139.69
  }
}
```
### For latest Endpoint
Request
```
# via URL query parameter and then use pretty-print
http://127.0.0.1:8000/api/latest?ticker=GOOGL

# via Swagger UI
http://127.0.0.1:8000/docs 
# Then set ticker=GOOGL
```
Response
```
{
  "ticker": "GOOGL",
  "previous_close": 196.52,
  "last_close": 201.42,
  "change": 4.9,
  "change_percent": 2.49
}
```
### For stats Endpoint
Request
```
# via URL query parameter and then use pretty-print
http://127.0.0.1:8000/api/stats?ticker=MSFT&start=2023-01-01&end=2023-12-31

# via Swagger UI
http://127.0.0.1:8000/docs 
# Then set ticker=MSFT, start=2023-01-01, end=2023-12-31

```
Response
```
{
  "ticker": "MSFT",
  "start_date": "2023-01-03",
  "end_date": "2023-12-29",
  "high": 384.3,
  "low": 219.35,
  "average": 313.95,
  "last_close": 376.04
}
```
## Runing Tests
```
# For testing particular endpoint
python -m pytest test/test_stats.py

# For testing entire project
python -m pytest -v
```
## CI/CD Pipeline – Pseudocode
```
Trigger: On push or pull_request to main branch

Steps:
1. Checkout repository

2. Set up Python environment
   - Install Python (e.g., 3.11)
   - Install dependencies from requirements.txt

3. Run automated tests
   - Use pytest for unit/integration tests

4. Build Docker image
   - docker build -t <your-image-name> 

5. Publish Docker image
   - Push to container registry

6. Deploy
   - Connect to main server 
   - Stop/remove previous container
   - Pull new image and start container
```