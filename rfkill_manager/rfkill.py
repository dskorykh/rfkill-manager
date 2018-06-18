import os
import sys
import fcntl
import struct
import logging

from rfkill_manager import constants
from rfkill_manager import exceptions


logger = logging.getLogger(__name__)

EVENT_LENGTH = struct.calcsize(constants.EVENT_FORMAT)


def rfkill_list():
    try:
        with open(constants.UDEV_RFKILL_PATH, 'r') as file_udev:
            rfkill_dict = _get_rfkill_values(file_udev)
    except IOError:
        logger.exception("rfkill is not available via udev")
    else:
        return rfkill_dict


def _get_rfkill_values(file):
    rfkill_dict = {}
    flags = fcntl.fcntl(file.fileno(), fcntl.F_GETFL)
    fcntl.fcntl(file.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK)
    while True:
        try:
            rfkill_dict.update(_read_rfkill_stream(file))
        except IOError:
            break

    return rfkill_dict


def _read_rfkill_stream(file):
    stream = file.read(EVENT_LENGTH)

    if is_python3():
        stream = bytes(stream, 'ascii')
        if len(stream) < EVENT_LENGTH:
            raise IOError('Error related to python version')

    return _unpack_rfkill_add_event(stream)


def is_python3():
    return sys.version_info.major == 3


def _unpack_rfkill_add_event(stream):
    idx, rtype, op, soft, hard = struct.unpack(constants.EVENT_FORMAT, stream)

    if op == constants.RFKILL_OP_ADD:
        name = get_rfkill_property(idx, 'name')
        return {name: {'idx': idx,
                       'type': constants.RFKILL_TYPES[rtype],
                       'soft': constants.RFKILL_STATE[soft],
                       'hard': constants.RFKILL_STATE[hard]}
                }


def get_rfkill_property(idx, property):
    _check_rfkill_device_on_existance(idx)
    try:
        with open(os.path.join(constants.SYSFS_RFKILL_PATH, "rfkill{}".format(idx), property), 'r') as f:
            return f.read().strip()
    except IOError:
        logger.exception("Available properties: 'name', 'type', 'soft', 'hard'. Please, choose one of them")


def _check_rfkill_device_on_existance(idx):
    if not os.path.exists(os.path.join(constants.SYSFS_RFKILL_PATH, "rfkill{}".format(idx))):
        raise exceptions.RfkillError("Device at {} rfkill index does not exist".format(idx))


def rfkill_event(idx, rtype, op, hard=0, soft=0):
    return struct.pack(constants.EVENT_FORMAT, idx, rtype, op, hard, soft)


def rfkill_execute_soft_event(idx, event):
    """event block or unblock"""
    _check_rfkill_device_on_existance(idx)
    event_struct = _prepare_event_struct(idx, event)
    try:
        with open(constants.UDEV_RFKILL_PATH, 'w') as f:
            f.write(event_struct)
    except IOError:
        logger.exception("Available properties: 'name', 'type', 'soft', 'hard'. Please, choose one of them")


def _prepare_event_struct(idx, event):
    action = constants.RFKILL_STATE[constants.RFKILL_EVENT_ACTIONS[event]]
    event_struct = rfkill_event(idx, constants.RFKILL_TYPE_ALL, constants.RFKILL_OP_CHANGE, action, 0)

    if is_python3():
        event_struct = event_struct.decode("ascii")

    return event_struct