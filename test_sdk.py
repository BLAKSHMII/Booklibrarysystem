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
