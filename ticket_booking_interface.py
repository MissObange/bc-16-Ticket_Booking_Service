"""

Usage:
    event add_event <event_name> ...
    event view_events
    event delete_event <event_ id>
    event edit_event <event_id>

    ticket view_tickets <event_id>

    ticket (-i | --interactive)
    ticket (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from ticket_booking_functions import new_events


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, args):
        try:
            opt = docopt(fn.__doc__, args)

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


class event_actions(cmd.Cmd):
    intro = 'Ticket Booking Service Application'
    prompt = 'event>> '
    file = None

    
    @docopt_cmd
    def do_add_event(self, args):
        """
        Usage:
        	add_event <event_name> ... 
        """
        eventName= args["<event_name>"]
        startDate= input("Enter the event start date in the format mm/dd/yy: ")
        endDate= input("Enter the event end date in the format mm/dd/yy: ")
        eventVenue = input("enter the event venue:")
        new_events.add_events(eventName, startDate, endDate, eventVenue)


    @docopt_cmd
    def do_view_events(self, args):
         """
        Usage:
            <view_events> 
        """
        new_events.view_events_list()
                                       
    @docopt_cmd
    def do_delete_event(self,args):

         """
        Usage:
            delete_event <event_id> 
        """
        selected_event = args["<event_id>"]
        new_events.delete_event(selected_event)


    
    @docopt_cmd
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()


option = docopt(__doc__, sys.argv[1:])

if option['--interactive']:
    try:
        print(__doc__)
        event_actions().cmdloop()
    except KeyboardInterrupt:
    	print("Exiting App")