import pytest
import rfkill_manager


def test_rfkill_list():
    rflist = rfkill_manager.rfkill_list()

    assert isinstance(rflist, dict)

    for value in rflist.values():
        assert any(key in ('name', 'type', 'soft', 'hard') for key in value.keys())


def test_rfkill_block():
    dev_type = 'bluetooth'

    rfkill_manager.rfkill_execute_event_by_type('bluetooth', 'block')

    rflist = rfkill_manager.rfkill_list()

    for name in rflist:
        if rflist[name]['type'] == dev_type:
            assert rflist[name]['soft'] is True


def test_rfkill_unblock():
    dev_type = 'bluetooth'

    rfkill_manager.rfkill_execute_event_by_type('bluetooth', 'unblock')

    rflist = rfkill_manager.rfkill_list()

    for name in rflist:
        if rflist[name]['type'] == dev_type:
            assert rflist[name]['soft'] is False


def test_soft_event_fake_interface():
    with pytest.raises(rfkill_manager.exceptions.RfkillError):
        rfkill_manager.rfkill_execute_soft_event(123, 'block')
