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


	def add_events(self, eventName, startDate, endDate, eventVenue):


		events = Event_details(event_name = eventName, start_date= startDate, end_date= endDate, venue = eventVenue)
		session.add(events)
		session.commit()
		

	def view_events_list():
		view_events_list = session.query(Event_details).all()
		list_events = []

		for item in view_events_list:
			list_item = [item.event_id, item.event_name, item.start_date, item.end_date, item.venue]
			list_events.append(list_item)
			

			if len(list_events)==0:
				print ("There are no upcoming events currently stored in the database")
		
		return list_events			


		


	def delete_event(selected_event):
		
		to_delete = Event_details(event_id = selected_event)
		session.delete(to_delete)
		session.commit()


	def edit_event(selected_event):

		updated_event = Event_details(event_name = new_eventName, start_date = new_startDate, end_date= new_endDate, venue = new_eventVenue)
		session.query(Event_details).filter_by(event_id).update(updated_event)

			
New_events()









