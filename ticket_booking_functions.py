from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ticket_booking_db_setup import event_details, ticket_details, Base
from datetime import datetime



engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()



class new_events():


	def add_events(eventName, startDate, endDate, eventVenue):

		if session.query(events).filter_by(event_name = eventName):

			print("This event already exists")

		else: 
			new_event = events(event_name = eventName, start_date = startDate, end_date= endDate, venue = eventVenue)
			session.append(event_name)
			session.add(new_event)
			session.commit()


	def view_events_list():

		for instance in session.query(events).order_by(evevnt_id):
			print(instance.event_name, instance.start_date, instance.end_date, instance.venue)
			session.commit()


	def delete_event(selected_event):
		
		to_delete = events(event_id = selected_event)
		session.delete(to_delete)
		session.commit()










