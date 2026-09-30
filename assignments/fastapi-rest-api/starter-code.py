from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Collection API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookCreate(BaseModel):
    title: str
    author: str


books = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
}


@app.get("/books", response_model=list[Book])
def list_books():
    # Return all books in the collection.
    pass


@app.post("/books", response_model=Book, status_code=201)
def add_book(book: BookCreate):
    # Assign a unique ID, create the book, save it, and return it.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # Return the requested book or raise HTTPException with status code 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # Delete the requested book or raise HTTPException with status code 404.
    pass
