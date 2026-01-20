"""
Starter code para a tarefa de FastAPI REST APIs.
Complete as seções marcadas com TODO para implementar a API.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

# Inicialize a aplicação FastAPI
app = FastAPI(title="Book Management API")


# TODO: Defina o modelo de dados para um livro usando Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    description: Optional[str] = None


# TODO: Crie uma estrutura de dados em memória para armazenar livros
books_db = []


# TODO: Implemente o endpoint GET /books para listar todos os livros
@app.get("/books", response_model=List[Book])
def get_books():
    """Retorna todos os livros da biblioteca."""
    pass


# TODO: Implemente o endpoint GET /books/{book_id} para obter um livro específico
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Retorna um livro específico pelo ID."""
    pass


# TODO: Implemente o endpoint POST /books para criar um novo livro
@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    """Cria um novo livro na biblioteca."""
    pass


# TODO: Implemente o endpoint PUT /books/{book_id} para atualizar um livro
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    """Atualiza um livro existente."""
    pass


# TODO: Implemente o endpoint DELETE /books/{book_id} para deletar um livro
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """Deleta um livro da biblioteca."""
    pass


# TODO: (OPCIONAL) Implemente autenticação simples com tokens
# Dica: Você pode usar um dicionário para armazenar credenciais válidas
