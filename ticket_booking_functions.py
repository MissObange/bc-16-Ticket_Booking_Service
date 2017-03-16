from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ticket_booking_db_setup import Event_details, Ticket_details, Base
from datetime import datetime
from tabulate import tabulate


engine = create_engine('sqlite:///ticket_booking_DB.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()



class New_events():


	def event_create(self, eventName, startDate, endDate, eventVenue):


		events = Event_details(event_name = eventName, start_date= startDate, end_date= endDate, venue = eventVenue)
		session.add(events)
		session.commit()
		return "Successfully added"
		

	def event_list():
		event_list = session.query(Event_details).all()
		list_events = []

		for item in event_list:
			list_item = [item.event_id, item.event_name, item.start_date, item.end_date, item.venue]
			list_events.append(list_item)

			if len(list_events)==0:
				return ("There are no upcoming events currently stored in the database")

			
		return list_events

	def event_delete(eventID):
		to_delete = session.query(Event_details).filter_by(event_id = eventID).first()
		session.delete(to_delete)
		session.commit()
		return('Successfully deleted!')

	def event_edit(event_ID):
		to_edit = session.query(Event_details).filter_by(event_id = event_ID).first()
		new_name = input("Enter new name to change from '%s' (Enter '0' to leave as is):  "%(to_edit.event_name))
		if new_name != 0:
			to_edit.event_name = new_name
		else: 
			pass

		new_start_date = input(("Enter new date to change from '%s' (Enter '0' to leave as is):  "%(to_edit.start_date)))
		if new_start_date !='0':
			to_edit.start_date = new_start_date

		new_end_date = input(("Enter new date to change from '%s' (Enter '0' to leave as is):  "%(to_edit.end_date)))
		if new_end_date != 0:
			to_edit.end_date = new_end_date

		new_venue = input(("Enter new date to change from '%s' (Enter '0' to leave as is):  "%(to_edit.venue)))
		if new_venue != 0:
			to_edit.venue = new_venue

		session.add(to_edit)
		session.commit()
		return "Successfully edited"


class New_tickets(New_events):
	def ticket_generate(self, eventID, customer_name, customer_email):
		session.query(Event_details).filter_by(event_id =eventID).first()
		tickets = Ticket_details(event_id = eventID, customer_name= customerName, customer_email = customerEmail)
		session.add(tickets)
		session.commit()
		return "Ticket has been succesfully generated"
		


New_events()
New_tickets()


	

			










