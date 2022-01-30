from pydantic import BaseModel, Field

from modules.book.domain.value_objects import KoreanMoney, Title, Isbn, Page, Year


class NewBookCommand(BaseModel):
    title: Title = Field(title="Book Title")
    isbn: Isbn = Field(title="Book Isbn")
    pages: Page = Field(title="Book Page")
    price: KoreanMoney = Field(title="Book Price")
    publication_year: Year = Field(title="Book publication year")
