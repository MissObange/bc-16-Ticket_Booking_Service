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
		# new_event = Event_details(event_name = eventName, start_date= startDate, end_date= endDate, venue = eventVenue)
		 
		# if session.query(Event_details).filter_by(event_name == eventName): 

		# 	print("This event already exists")

		# else: 
			
		# 	session.add(new_event)
		# 	session.commit()
		

	def view_events_list():

		for instance in session.query(Event_details).order_by(event_id):
			print(instance.event_name, instance.start_date, instance.end_date, instance.venue)
			session.commit()


	def delete_event(selected_event):
		
		to_delete = Event_details(event_id = selected_event)
		session.delete(to_delete)
		session.commit()


	def edit_event(selected_event):

		updated_event = Event_details(event_name = new_eventName, start_date = new_startDate, end_date= new_endDate, venue = new_eventVenue)
		session.query(Event_details).filter_by(event_id).update(updated_event)

			
New_events()









