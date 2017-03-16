from sqlalchemy import create_engine, ForeignKey

from sqlalchemy import Column, Date, Integer, String, VARCHAR

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///ticket_booking_database.db')

Base = declarative_base()


class Event_details(Base):

    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True)

    event_name = Column(VARCHAR(50))

    start_date = Column(VARCHAR(9))

    end_date = Column(VARCHAR(9))

    venue = Column(VARCHAR(50))


    


class Ticket_details(Base):
	__tablename__ = "tickets"


	ticket_id = Column(Integer, primary_key = True)

	event_id = Column(Integer, ForeignKey("events.event_id"))
	event = relationship('Event_details', backref= 'events')
	
	customer_name = Column(String(50))

	customer_email = Column(VARCHAR(50))



Base.metadata.create_all(engine)