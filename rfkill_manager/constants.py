WPA_STATE = 'Client state'
HOST_STATE = 'Host state'
OFF_STATE = 'WiFi off'

RFKILL_STATE = [False, True]

RFKILL_EVENT_ACTIONS = {
    "unblock": 0,
    "block": 1,
}

RFKILL_TYPES = ['all', 'wlan', 'bluetooth', 'uwb', 'wimax', 'wwan', 'gps', 'fm', 'nfc']
RFKILL_TYPE_ALL = 0
RFKILL_TYPE_WLAN = 1
RFKILL_TYPE_BLUETOOTH = 2
RFKILL_TYPE_UWB = 3
RFKILL_TYPE_WIMAX = 4
RFKILL_TYPE_WWAN = 5
RFKILL_TYPE_GPS = 6
RFKILL_TYPE_FM = 7
RFKILL_TYPE_NFC = 8
NUM_RFKILL_TYPES = 9

EVENT_FORMAT = "IBBBB"

RFKILL_OP_ADD = 0
RFKILL_OP_DEL = 1
RFKILL_OP_CHANGE = 2
RFKILL_OP_CHANGE_ALL = 3

UDEV_RFKILL_PATH = '/dev/rfkill'
SYSFS_RFKILL_PATH = '/sys/class/rfkill'
