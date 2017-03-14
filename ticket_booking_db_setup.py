from sqlalchemy import create_engine, ForeignKey

from sqlalchemy import Column, Date, Integer, String, VARCHAR

from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///ticket_booking.db', echo=True)

Base = declarative_base()


class events(Base):

    __tablename__ = "event_details"

    event_id = Column(VARCHAR, primary_key=True)

    event_name = Column(VARCHAR)

    start_date = Column(Date)

    end_date = Column(Date)

    venue = Column(VARCHAR)


    


class tickets(Base):
	__tablename__ = "ticket_details"

	ticket_id = Column(VARCHAR)

	
	event_title = Column(VARCHAR)
	
	customer_name = Column(String)

	customer_email = Column(String)

	begin_id = Column(Date)
	

	end_id = Column(Date)
	

	



Base.metadata.create_all(engine)