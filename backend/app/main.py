from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from . import models, schemas
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.BookOut)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(**book.dict(), available_copies=book.total_copies)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books/", response_model=list[schemas.BookOut])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.post("/books/{book_id}/reserve", response_model=schemas.ReservationOut)
def reserve_book(book_id: int, req: schemas.ReservationCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.available_copies < 1:
        raise HTTPException(status_code=400, detail="No copies left")

    book.available_copies -= 1
    res = models.Reservation(user_name=req.user_name, book_id=book.id, expires_at=datetime.utcnow() + timedelta(days=7))
    db.add(res)
    db.commit()
    db.refresh(res)
    return res

@app.delete("/reservations/{reservation_id}")
def cancel_reservation(reservation_id: int, db: Session = Depends(get_db)):
    res = db.query(models.Reservation).get(reservation_id)
    if not res:
        raise HTTPException(status_code=404, detail="Reservation not found")
    res.canceled = True
    book = db.query(models.Book).get(res.book_id)
    if book:
        book.available_copies += 1
    db.commit()
    return {"message": "Reservation canceled"}
