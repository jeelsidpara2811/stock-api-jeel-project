# JEEL's Stock API

A FastAPI-based application for retrieving and comparing stock market statistics.
---

## Features
- Analysis of current momentum of stock
- Compare stocks performance
- Preview stock statistics
- Built with **FastAPI**(Swagger UI) for high performance
- Ready to deploy with **Docker**

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
1. /api/compare - For Comparing stock performance
2. /api/latest - For change monentum 
3. /api/stats - For stock statistics 

## Example of API usage

### For compare Endpoint
Request
```
# Use this URL on web and 
http://127.0.0.1:8000/docs 
# Then set ticker1=GOOGL, ticker2=MSFT, start=2023-01-01, end=2023-03-31
```
Response
```
{
  "GOOGL": {
    "high": 107.54,
    "low": 84.35,
    "average": 95.24,
    "last_close": 100.29
  },
  "MSFT": {
    "high": 279.49,
    "low": 214.98,
    "average": 249.79,
    "last_close": 279.09
  }
}
```
### For latest Endpoint
Request
```
# Use this URL on web and
http://127.0.0.1:8000/docs 
# Then set ticker=GOOGL
```
Response
```
{
  "ticker": "GOOGL",
  "previous_close": 194.67,
  "last_close": 196.09,
  "change": 1.42,
  "change_percent": 0.73
}
```
### For stats Endpoint
Request
```
# Use this URL on web and
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