#!venv/bin/python
"""
Usage:
    my_app add_event 
    my_app list_events 
    my_app delete_event <event_id>
    my_app edit_event <event_id>
    my_app view_tickets <event_id>
    my_app (-i | --interactive)
    my_app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from ticket_booking_functions import New_events
from tabulate import tabulate



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Event_actions(cmd.Cmd):
    intro = 'Welcome to Ticket Booking Service System'
    prompt = 'Enter action>> '
    file = None

    @docopt_cmd
    def do_add_event(self, arg):
        """Usage:
                add_event
        """
        eventName= input("Event name: ")
        startDate= input("Start date(mm/dd/yy): ")
        endDate= input("End date (mm/dd/yy): ")
        eventVenue = input("Venue:")

        add_new_event = New_events()
        add_new_event.add_events(eventName, startDate, endDate, eventVenue)
        print("Events successfully created")

    @docopt_cmd
    def do_list_events(self, arg):
        """Usage:
                list_events 
        """
        print(tabulate(New_events.view_events_list(), headers =("Event ID", "Event Name", "Start Date", "End Date", "Venue"), tablefmt = "orgtbl"))




        

    @docopt_cmd
    def do_delete_event(self, arg):
        """Usage: 
                delete_event <event_id>
        """
        

    @docopt_cmd
    def do_edit_event(self, arg):
        """Usage: 
            edit_event <event_id> 
        """
        

    @docopt_cmd
    def do_view_tickets(self,arg):
        """Usage: 
                view_tickets <event_id>
        """
        



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('     Thank you for using Ticket Booking Service system')
        print('                         Goodbye')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        Event_actions().cmdloop()
    except KeyboardInterrupt:
        print("Exiting App")