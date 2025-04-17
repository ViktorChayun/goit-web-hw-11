from datetime import date
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class ContactSchema(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr = Field()
    phone_number: str = Field(max_length=20)
    birthday: date = Field()
    additional_info: Optional[str] = Field()
