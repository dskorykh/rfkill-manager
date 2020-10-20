import rfkill_manager
from pprint import pprint


def get_rfkill_list():
    return rfkill_manager.rfkill_list()


if __name__ == '__main__':
    pprint(get_rfkill_list())
    rfkill_manager.rfkill_execute_event_by_type('bluetooth', 'block')
    pprint(get_rfkill_list())
    rfkill_manager.rfkill_execute_event_by_type('bluetooth', 'unblock')
    pprint(get_rfkill_list())
