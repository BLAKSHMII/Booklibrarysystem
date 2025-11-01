from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    author = Column(String(100))
    total_copies = Column(Integer)
    available_copies = Column(Integer)
    reservations = relationship("Reservation", back_populates="book")

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    book_id = Column(Integer, ForeignKey("books.id"))
    expires_at = Column(DateTime, default=datetime.utcnow)
    canceled = Column(Boolean, default=False)
    book = relationship("Book", back_populates="reservations")
