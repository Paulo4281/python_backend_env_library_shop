from typing import TypedDict
from datetime import datetime

class BookDTO(TypedDict):
    title: str
    price: float
    category_id: str
    user_id: str
    author_id: str

class BookResponseDTO(BookDTO):
    id_: str
    updated_at: datetime
    created_at: datetime

class BookUpdateDTO(BookDTO):
    pass