from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    total_copies: int

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    total_copies: int
    available_copies: int
    class Config:
        orm_mode = True

class ReservationCreate(BaseModel):
    user_name: str

class ReservationOut(BaseModel):
    id: int
    user_name: str
    book_id: int
    canceled: bool
    class Config:
        orm_mode = True
