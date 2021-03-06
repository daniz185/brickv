# -*- coding: utf-8 -*-
"""
Industrial Dual AC Relay Plugin
Copyright (C) 2020 Olaf Lüke <olaf@tinkerforge.com>

industrial_dual_ac_relay.py: Industrial Dual AC Relay Plugin Implementation

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from brickv.plugin_system.comcu_plugin_base import COMCUPluginBase
from brickv.plugin_system.plugins.industrial_dual_ac_relay.ui_industrial_dual_ac_relay import Ui_IndustrialDualACRelay
from brickv.bindings.bricklet_industrial_dual_ac_relay import BrickletIndustrialDualACRelay
from brickv.async_call import async_call
from brickv.load_pixmap import load_masked_pixmap
from brickv.monoflop import Monoflop

class IndustrialDualACRelay(COMCUPluginBase, Ui_IndustrialDualACRelay):
    def __init__(self, *args):
        COMCUPluginBase.__init__(self, BrickletIndustrialDualACRelay, *args)

        self.setupUi(self)

        self.idr = self.device

        self.value0_combobox.setItemData(0, True)
        self.value0_combobox.setItemData(1, False)

        self.value1_combobox.setItemData(0, True)
        self.value1_combobox.setItemData(1, False)

        self.monoflop = Monoflop(self.idr,
                                 [0, 1],
                                 [self.value0_combobox, self.value1_combobox],
                                 self.cb_value_change_by_monoflop,
                                 [self.time0_spinbox, self.time1_spinbox],
                                 None,
                                 self)

        self.ch0_button.clicked.connect(self.ch0_clicked)
        self.ch1_button.clicked.connect(self.ch1_clicked)

        self.go0_button.clicked.connect(self.go0_clicked)
        self.go1_button.clicked.connect(self.go1_clicked)

        self.combobox_led0.currentIndexChanged.connect(self.combobox_led0_changed)
        self.combobox_led1.currentIndexChanged.connect(self.combobox_led1_changed)

        self.a0_pixmap = load_masked_pixmap('plugin_system/plugins/industrial_dual_ac_relay/relay_close.bmp')
        self.a1_pixmap = load_masked_pixmap('plugin_system/plugins/industrial_dual_ac_relay/relay_close.bmp')
        self.b0_pixmap = load_masked_pixmap('plugin_system/plugins/industrial_dual_ac_relay/relay_open.bmp')
        self.b1_pixmap = load_masked_pixmap('plugin_system/plugins/industrial_dual_ac_relay/relay_open.bmp')

    def combobox_led0_changed(self, value):
        self.idr.set_channel_led_config(0, value)

    def combobox_led1_changed(self, value):
        self.idr.set_channel_led_config(1, value)

    def get_value_async(self, value):
        width = self.ch0_button.width()

        if self.ch0_button.minimumWidth() < width:
            self.ch0_button.setMinimumWidth(width)

        width = self.ch1_button.width()

        if self.ch1_button.minimumWidth() < width:
            self.ch1_button.setMinimumWidth(width)

        ch0, ch1 = value

        if ch0:
            self.ch0_button.setText('Switch Off')
            self.ch0_image.setPixmap(self.a0_pixmap)
        else:
            self.ch0_button.setText('Switch On')
            self.ch0_image.setPixmap(self.b0_pixmap)

        if ch1:
            self.ch1_button.setText('Switch Off')
            self.ch1_image.setPixmap(self.a1_pixmap)
        else:
            self.ch1_button.setText('Switch On')
            self.ch1_image.setPixmap(self.b1_pixmap)

    def get_channel_led_config_async(self, index, config):
        if index == 0:
            self.combobox_led0.setCurrentIndex(config)
        elif index == 1:
            self.combobox_led1.setCurrentIndex(config)

    def start(self):
        async_call(self.idr.get_value, None, self.get_value_async, self.increase_error_count)
        for channel in range(2):
            async_call(self.idr.get_channel_led_config, channel, self.get_channel_led_config_async, self.increase_error_count, pass_arguments_to_result_callback=True)

        self.monoflop.start()

    def stop(self):
        self.monoflop.stop()

    def destroy(self):
        pass

    @staticmethod
    def has_device_identifier(device_identifier):
        return device_identifier == BrickletIndustrialDualACRelay.DEVICE_IDENTIFIER

    def ch0_clicked(self):
        width = self.ch0_button.width()

        if self.ch0_button.minimumWidth() < width:
            self.ch0_button.setMinimumWidth(width)

        value = 'On' in self.ch0_button.text().replace('&', '')

        if value:
            self.ch0_button.setText('Switch Off')
            self.ch0_image.setPixmap(self.a0_pixmap)
        else:
            self.ch0_button.setText('Switch On')
            self.ch0_image.setPixmap(self.b0_pixmap)

        async_call(self.idr.set_selected_value, (0, value), None, self.increase_error_count)

    def ch1_clicked(self):
        width = self.ch1_button.width()

        if self.ch1_button.minimumWidth() < width:
            self.ch1_button.setMinimumWidth(width)

        value = 'On' in self.ch1_button.text().replace('&', '')

        if value:
            self.ch1_button.setText('Switch Off')
            self.ch1_image.setPixmap(self.a1_pixmap)
        else:
            self.ch1_button.setText('Switch On')
            self.ch1_image.setPixmap(self.b1_pixmap)

        async_call(self.idr.set_selected_value, (1, value), None, self.increase_error_count)

    def go0_clicked(self):
        self.monoflop.trigger(0)

    def go1_clicked(self):
        self.monoflop.trigger(1)

    def cb_value_change_by_monoflop(self, channel, value):
        if channel == 0:
            if value:
                self.ch0_button.setText('Switch Off')
                self.ch0_image.setPixmap(self.a0_pixmap)
            else:
                self.ch0_button.setText('Switch On')
                self.ch0_image.setPixmap(self.b0_pixmap)
        elif channel == 1:
            if value:
                self.ch1_button.setText('Switch Off')
                self.ch1_image.setPixmap(self.a1_pixmap)
            else:
                self.ch1_button.setText('Switch On')
                self.ch1_image.setPixmap(self.b1_pixmap)
