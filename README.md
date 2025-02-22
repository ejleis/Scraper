# Scraper Application

## Description
A basic scraping program that gets all headings(`<h1></h1> - <h6></h6>`) inside a website

## Prerequisites
Ensure you have the following installed on your system:
- Python (version 3+ recommended)
- Git

## Setup Instructions
Follow these steps to set up and run the project:

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```

### 3. Activate the Virtual Environment
#### Windows:
```sh
venv\Scripts\activate
```
#### macOS/Linux:
```sh
source venv/bin/activate
```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Run the Project
```sh
python main.py
```

## Executing API:
### Run the following details on Postman to test
#### 1. Enter URL: `http://localhost:8000/scrape`
#### 2. On the body, enter the following JSON details:
`{
    "url": "<URL of the website you want to scrape>"
}`
#### 3. Execute "Send" on Postman