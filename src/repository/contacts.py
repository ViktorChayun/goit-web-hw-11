from typing import List, Optional
from datetime import date, timedelta

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import func

from src.models.contact import Contact
from src.schemas.contact import ContactSchema


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact | None:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def craete_contact(data: ContactSchema, db: Session) -> Contact:
    new_contact = Contact(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        phone_number=data.phone_number,
        birthday=data.birthday,
        additional_info=data.additional_info
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


async def update_contact(
    contact_id: int,
    data: ContactSchema,
    db: Session
) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = data.first_name
        contact.last_name = data.last_name
        contact.email = data.email
        contact.phone_number = data.phone_number
        contact.birthday = data.birthday
        contact.additional_info = data.additional_info
        db.commit()
        db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contacts(
    first_name: Optional[str],
    last_name: Optional[str],
    email: Optional[str],
    skip: int,
    limit: int,
    db: Session
) -> List[Contact]:
    # print(email)
    query = select(Contact)
    if first_name:
        query = query.where(Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.where(Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.where(Contact.email.ilike(f"%{email}%"))
    query = query.offset(skip).limit(limit)
    print(query)
    result = db.execute(query)
    return result.scalars().all()


async def upcoming_birthdays(days, skip, limit, db: Session) -> List[Contact]:
    today = date.today()
    filter_lst = {(today + timedelta(days=i)).strftime("%m-%d")
                  for i in range(days)}
    query = select(Contact).where(
        func.to_char(Contact.birthday, 'MM-DD').in_(filter_lst)
    )
    query = query.offset(skip).limit(limit)
    print(query)
    # result = await db.execute(query)
    result = db.execute(query)
    return result.scalars().all()
