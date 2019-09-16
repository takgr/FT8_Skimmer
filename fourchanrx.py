#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fourchanrx
# Generated: Mon Sep 16 10:19:46 2019
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class fourchanrx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Fourchanrx")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6
        self.freq_4 = freq_4 = 21074000
        self.freq_3 = freq_3 = 18100000
        self.freq_2 = freq_2 = 10136000
        self.freq_1 = freq_1 = 14074000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "fpga=usrp1_fpga_4rx.rbf")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		otw_format='sc16',
        		channels=range(4),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec('A:A A:A A:A A:A', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq_1, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_center_freq(freq_2, 1)
        self.uhd_usrp_source_0.set_gain(0, 1)
        self.uhd_usrp_source_0.set_center_freq(freq_3, 2)
        self.uhd_usrp_source_0.set_gain(0, 2)
        self.uhd_usrp_source_0.set_center_freq(freq_4, 3)
        self.uhd_usrp_source_0.set_gain(0, 3)
        self.blocks_file_sink_0_0_1 = blocks.file_sink(gr.sizeof_float*1, 'fifo_chan4.c2', False)
        self.blocks_file_sink_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_float*1, 'fifo_chan3.c2', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, 'fifo_chan2.c2', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, 'fifo_chan1.c2', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_file_sink_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 2), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 3), (self.blocks_file_sink_0_0_1, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_freq_4(self):
        return self.freq_4

    def set_freq_4(self, freq_4):
        self.freq_4 = freq_4
        self.uhd_usrp_source_0.set_center_freq(self.freq_4, 3)

    def get_freq_3(self):
        return self.freq_3

    def set_freq_3(self, freq_3):
        self.freq_3 = freq_3
        self.uhd_usrp_source_0.set_center_freq(self.freq_3, 2)

    def get_freq_2(self):
        return self.freq_2

    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2
        self.uhd_usrp_source_0.set_center_freq(self.freq_2, 1)

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.uhd_usrp_source_0.set_center_freq(self.freq_1, 0)


def main(top_block_cls=fourchanrx, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
