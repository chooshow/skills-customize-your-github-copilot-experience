# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining request and response models, handling HTTP methods, and returning useful status codes. You will create an in-memory book collection that can be listed, added, retrieved, and deleted.

## 📝 Tasks

### 🛠️ List Books with GET

#### Description
Install the packages in `requirements.txt`, then complete the `GET /books` endpoint in the starter code. Run the API locally with `uvicorn starter-code:app --reload` and inspect the endpoint at `http://127.0.0.1:8000/docs`.

#### Requirements
Completed program should:

- Define a Pydantic `Book` model with an integer `id`, a `title`, and an `author`
- Return all books from `GET /books` as a JSON list
- Start with the sample books provided in the starter code


### 🛠️ Add Books with POST

#### Description
Create an endpoint that accepts a new book's title and author, assigns it a unique ID, and adds it to the in-memory collection.

#### Requirements
Completed program should:

- Define a request model for a book's `title` and `author`
- Add a book through `POST /books` and return the created book
- Return HTTP status code `201` when a book is created


### 🛠️ Retrieve and Delete a Book

#### Description
Add endpoints to retrieve one book by ID and delete a book by ID. Return a clear `404 Not Found` response when the requested ID does not exist.

#### Requirements
Completed program should:

- Return one book from `GET /books/{book_id}` when its ID exists
- Delete a book through `DELETE /books/{book_id}` and confirm the deletion
- Raise an HTTP 404 error for a book ID that is not in the collection
