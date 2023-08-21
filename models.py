from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    phoneNumber = Column(String)
    email = Column(String)
    linkedId = Column(Integer, ForeignKey('contacts.id'))
    linkPrecedence = Column(Enum('secondary', 'primary'))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True))

    linked_contact = relationship('Contact', remote_side=[id])

    def __repr__(self):
        return f"<Contact(id={self.id}, phoneNumber={self.phoneNumber}, email={self.email}, linkedId={self.linkedId}, linkPrecedence={self.linkPrecedence})>"
