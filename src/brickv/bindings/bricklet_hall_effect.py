# -*- coding: utf-8 -*-
#############################################################
# This file was automatically generated on 2019-12-02.      #
#                                                           #
# Python Bindings Version 2.1.24                            #
#                                                           #
# If you have a bugfix for this file and want to commit it, #
# please fix the bug in the generator. You can find a link  #
# to the generators git repository on tinkerforge.com       #
#############################################################

from collections import namedtuple

try:
    from .ip_connection import Device, IPConnection, Error, create_char, create_char_list, create_string, create_chunk_data
except ValueError:
    from ip_connection import Device, IPConnection, Error, create_char, create_char_list, create_string, create_chunk_data

GetEdgeCountConfig = namedtuple('EdgeCountConfig', ['edge_type', 'debounce'])
EdgeInterrupt = namedtuple('EdgeInterrupt', ['count', 'value'])
GetIdentity = namedtuple('Identity', ['uid', 'connected_uid', 'position', 'hardware_version', 'firmware_version', 'device_identifier'])

class BrickletHallEffect(Device):
    """
    Detects presence of magnetic field
    """

    DEVICE_IDENTIFIER = 240
    DEVICE_DISPLAY_NAME = 'Hall Effect Bricklet'
    DEVICE_URL_PART = 'hall_effect' # internal

    CALLBACK_EDGE_COUNT = 10


    FUNCTION_GET_VALUE = 1
    FUNCTION_GET_EDGE_COUNT = 2
    FUNCTION_SET_EDGE_COUNT_CONFIG = 3
    FUNCTION_GET_EDGE_COUNT_CONFIG = 4
    FUNCTION_SET_EDGE_INTERRUPT = 5
    FUNCTION_GET_EDGE_INTERRUPT = 6
    FUNCTION_SET_EDGE_COUNT_CALLBACK_PERIOD = 7
    FUNCTION_GET_EDGE_COUNT_CALLBACK_PERIOD = 8
    FUNCTION_EDGE_INTERRUPT = 9
    FUNCTION_GET_IDENTITY = 255

    EDGE_TYPE_RISING = 0
    EDGE_TYPE_FALLING = 1
    EDGE_TYPE_BOTH = 2

    def __init__(self, uid, ipcon):
        """
        Creates an object with the unique device ID *uid* and adds it to
        the IP Connection *ipcon*.
        """
        Device.__init__(self, uid, ipcon)

        self.api_version = (2, 0, 0)

        self.response_expected[BrickletHallEffect.FUNCTION_GET_VALUE] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_GET_EDGE_COUNT] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_SET_EDGE_COUNT_CONFIG] = BrickletHallEffect.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletHallEffect.FUNCTION_GET_EDGE_COUNT_CONFIG] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_SET_EDGE_INTERRUPT] = BrickletHallEffect.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_GET_EDGE_INTERRUPT] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_SET_EDGE_COUNT_CALLBACK_PERIOD] = BrickletHallEffect.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_GET_EDGE_COUNT_CALLBACK_PERIOD] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_EDGE_INTERRUPT] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletHallEffect.FUNCTION_GET_IDENTITY] = BrickletHallEffect.RESPONSE_EXPECTED_ALWAYS_TRUE

        self.callback_formats[BrickletHallEffect.CALLBACK_EDGE_COUNT] = 'I !'


    def get_value(self):
        """
        Returns *true* if a magnetic field of 3.5 millitesla or greater is detected.
        """
        return self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_GET_VALUE, (), '', '!')

    def get_edge_count(self, reset_counter):
        """
        Returns the current value of the edge counter. You can configure
        edge type (rising, falling, both) that is counted with
        :func:`Set Edge Count Config`.

        If you set the reset counter to *true*, the count is set back to 0
        directly after it is read.
        """
        reset_counter = bool(reset_counter)

        return self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_GET_EDGE_COUNT, (reset_counter,), '!', 'I')

    def set_edge_count_config(self, edge_type, debounce):
        """
        The edge type parameter configures if rising edges, falling edges or
        both are counted. Possible edge types are:

        * 0 = rising (default)
        * 1 = falling
        * 2 = both

        A magnetic field of 3.5 millitesla or greater causes a falling edge and a
        magnetic field of 2.5 millitesla or smaller causes a rising edge.

        If a magnet comes near the Bricklet the signal goes low (falling edge), if
        a magnet is removed from the vicinity the signal goes high (rising edge).

        Configuring an edge counter resets its value to 0.

        If you don't know what any of this means, just leave it at default. The
        default configuration is very likely OK for you.
        """
        edge_type = int(edge_type)
        debounce = int(debounce)

        self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_SET_EDGE_COUNT_CONFIG, (edge_type, debounce), 'B B', '')

    def get_edge_count_config(self):
        """
        Returns the edge type and debounce time as set by :func:`Set Edge Count Config`.
        """
        return GetEdgeCountConfig(*self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_GET_EDGE_COUNT_CONFIG, (), '', 'B B'))

    def set_edge_interrupt(self, edges):
        """
        Sets the number of edges until an interrupt is invoked.

        If *edges* is set to n, an interrupt is invoked for every n-th detected edge.

        If *edges* is set to 0, the interrupt is disabled.

        Default value is 0.
        """
        edges = int(edges)

        self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_SET_EDGE_INTERRUPT, (edges,), 'I', '')

    def get_edge_interrupt(self):
        """
        Returns the edges as set by :func:`Set Edge Interrupt`.
        """
        return self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_GET_EDGE_INTERRUPT, (), '', 'I')

    def set_edge_count_callback_period(self, period):
        """
        Sets the period with which the :cb:`Edge Count` callback is triggered
        periodically. A value of 0 turns the callback off.

        The :cb:`Edge Count` callback is only triggered if the edge count has changed
        since the last triggering.
        """
        period = int(period)

        self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_SET_EDGE_COUNT_CALLBACK_PERIOD, (period,), 'I', '')

    def get_edge_count_callback_period(self):
        """
        Returns the period as set by :func:`Set Edge Count Callback Period`.
        """
        return self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_GET_EDGE_COUNT_CALLBACK_PERIOD, (), '', 'I')

    def edge_interrupt(self):
        """
        This callback is triggered every n-th count, as configured with
        :func:`Set Edge Interrupt`. The parameters are the
        current count and the current value (see :func:`Get Value` and
        :func:`Get Edge Count`).
        """
        return EdgeInterrupt(*self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_EDGE_INTERRUPT, (), '', 'I !'))

    def get_identity(self):
        """
        Returns the UID, the UID where the Bricklet is connected to,
        the position, the hardware and firmware version as well as the
        device identifier.

        The position can be 'a', 'b', 'c' or 'd'.

        The device identifier numbers can be found :ref:`here <device_identifier>`.
        |device_identifier_constant|
        """
        return GetIdentity(*self.ipcon.send_request(self, BrickletHallEffect.FUNCTION_GET_IDENTITY, (), '', '8s 8s c 3B 3B H'))

    def register_callback(self, callback_id, function):
        """
        Registers the given *function* with the given *callback_id*.
        """
        if function is None:
            self.registered_callbacks.pop(callback_id, None)
        else:
            self.registered_callbacks[callback_id] = function

HallEffect = BrickletHallEffect # for backward compatibility
