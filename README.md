# rfkill_manager

Python API to manage Linux rfkill 

### API 

`rfkill_list()` - returns dict with next structure: 
```
{"interface": 
    {"idx": ..., "type": ..., "soft": ..., "hard": ...}, 
 ...
}
```

`rfkill_execute_soft_event(idx, event)` - execute soft rfkill event for one interface:  
Arguments:
* `idx` - index of rfkill device
* `event` - string "block" or "unblock"

`rfkill_execute_event_by_type(type, event)` - execute soft rfkill event for type:  
Arguments:
* `type` - type of rfkill devices:
    * 'all', 
    * 'wlan', 
    * 'bluetooth', 
    * 'uwb', 
    * 'wimax', 
    * 'wwan', 
    * 'gps', 
    * 'fm', 
    * 'nfc'
* `event` - string "block" or "unblock"