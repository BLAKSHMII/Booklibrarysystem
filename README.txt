Library Book Reservation System

A simple Library Management System built with FastAPI, React, and an auto-generated Python SDK using OpenAPI.

===Features==

Add Books → Add books with total copies.

View Books → List all available books.

Reserve Book → Reserve a book if copies are available.

Cancel Reservation → Cancel an existing reservation.

Auto Availability → Book copies update automatically when reserved or canceled.

Python SDK → Generated via openapi-generator-cli from the backend’s OpenAPI spec.

Automation → Scripts for setup and running both backend and frontend.

===Tech Stack==
Layer	Technology

Backend	FastAPI + SQLite
Frontend	ReactJS
SDK	OpenAPI Generator (Python)
Automation	Batch / PowerShell scripts

==== Setup Instructions =====
1.Backend Setup
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

2.SDK Generation
openapi-generator-cli generate -i http://localhost:8000/openapi.json -g python -o library_sdk

3.SDK Test Example
from library_sdk.openapi_client import Configuration, ApiClient
from library_sdk.openapi_client.api.default_api import DefaultApi
from library_sdk.openapi_client.models import BookCreate, ReservationCreate

# Connect to FastAPI backend
config = Configuration(host="http://localhost:8000")
client = ApiClient(config)
api = DefaultApi(client)

# Add a new book
print("Add a New Book")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
total_copies = int(input("Enter Total Copies: "))

new_book = BookCreate(
    title=title,
    author=author,
    total_copies=total_copies
)
created_book = api.add_book_books_post(book_create=new_book)
print("Book Added Successfully:")
print(created_book)

# List all books
print("Current Books in Library:")
books = api.get_books_books_get()
for book in books:
    print(f"  ID: {book.id}, Title: {book.title}, Author: {book.author}, Available: {book.available_copies}")

# Reserve a book by ID
book_id = int(input("\nEnter Book ID to Reserve: "))
user_name = input("Enter Your Name: ")
reservation = api.reserve_book_books_book_id_reserve_post(
    book_id=book_id,
    reservation_create=ReservationCreate(user_name=user_name)
)
print("Book Reserved Successfully:")
print(reservation)

#Cancel reservation by ID
reservation_id = int(input("\nEnter Reservation ID to Cancel: "))
api.cancel_reservation_reservations_reservation_id_delete(
    reservation_id=reservation_id
)
print("Reservation Canceled Successfully!")


4.Frontend Setup
cd frontend
npm install
npm start

==Project Structure==
Booklibrarysystem/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── frontend/
│   └── (React app)
├── library_sdk/
│   └── openapi_client/
└── test_sdk.py


==Example Workflow==

Run the FastAPI backend (uvicorn app.main:app --reload).

Generate the Python SDK using OpenAPI.

Run test_sdk.py to interact with the API.

Use the React dashboard to manage books visually.


# ===============================
# AUTOMATION SCRIPT (WINDOWS)
# FastAPI + Frontend + SDK Setup
# ===============================

Write-Host "=== Step 1: Create Python virtual environment ==="
python -m venv venv
venv\Scripts\activate

Write-Host "=== Step 2: Install backend dependencies ==="
pip install -r backend\requirements.txt

# ===============================
# Apply DB setup (optional)
# ===============================
Write-Host "=== Step 3: Configure database (optional) ==="
# Example: if using SQLite, skip this; for MySQL, uncomment below
# python backend\app\database.py

# ===============================
# Generate Python SDK
# ===============================
Write-Host "=== Step 4: Generate SDK from FastAPI OpenAPI spec ==="
Start-Process powershell -ArgumentList "cd backend; uvicorn main:app --reload"  # Start backend temporarily
Start-Sleep -Seconds 5  # wait for server to start
openapi-generator-cli generate -i http://localhost:8000/openapi.json -g python -o library_sdk --skip-validate-spec
Stop-Process -Name "python" -ErrorAction SilentlyContinue

# ===============================
# Frontend setup
# ===============================
Write-Host "=== Step 5: Install frontend dependencies ==="
cd frontend
npm install
cd ..

# ===============================
# Run both servers
# ===============================
Write-Host "=== Step 6: Launch backend and frontend ==="
Start-Process powershell -ArgumentList "cd backend; uvicorn main:app --reload"
Start-Process powershell -ArgumentList "cd frontend; npm start"

Write-Host " Setup complete! Backend: http://127.0.0.1:8000  |  Frontend: http://localhost:3000"
