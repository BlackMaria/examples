# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receiver With Decoder
# Author: Piotr Krysik
# Generated: Sat Jul 22 00:27:21 2017
##################################################

from gnuradio import gr
from gnuradio.filter import firdes
import grgsm


class receiver_with_decoder(gr.hier_block2):

    def __init__(self, OSR=4, chan_num=0, fc=939.4e6, osr=4, ppm=0, samp_rate=0.2e6):
        gr.hier_block2.__init__(
            self, "Receiver With Decoder",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(0, 0, 0),
        )
        self.message_port_register_hier_out("bursts")
        self.message_port_register_hier_out("msgs")

        ##################################################
        # Parameters
        ##################################################
        self.OSR = OSR
        self.chan_num = chan_num
        self.fc = fc
        self.osr = osr
        self.ppm = ppm
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_out = samp_rate_out = 1625000.0/6.0*OSR

        ##################################################
        # Blocks
        ##################################################
        self.gsm_receiver_0 = grgsm.receiver(OSR, ([chan_num]), ([]), False)
        self.gsm_input_0 = grgsm.gsm_input(
            ppm=ppm,
            osr=OSR,
            fc=fc,
            samp_rate_in=samp_rate,
        )
        self.gsm_control_channels_decoder_0 = grgsm.control_channels_decoder()
        self.gsm_clock_offset_control_0 = grgsm.clock_offset_control(fc, samp_rate, osr)
        self.gsm_bcch_ccch_demapper_0 = grgsm.gsm_bcch_ccch_demapper(
            timeslot_nr=0,
        )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.gsm_bcch_ccch_demapper_0, 'bursts'), (self.gsm_control_channels_decoder_0, 'bursts'))    
        self.msg_connect((self.gsm_clock_offset_control_0, 'ctrl'), (self.gsm_input_0, 'ctrl_in'))    
        self.msg_connect((self.gsm_control_channels_decoder_0, 'msgs'), (self, 'bursts'))    
        self.msg_connect((self.gsm_control_channels_decoder_0, 'msgs'), (self, 'msgs'))    
        self.msg_connect((self.gsm_receiver_0, 'C0'), (self.gsm_bcch_ccch_demapper_0, 'bursts'))    
        self.msg_connect((self.gsm_receiver_0, 'measurements'), (self.gsm_clock_offset_control_0, 'measurements'))    
        self.connect((self.gsm_input_0, 0), (self.gsm_receiver_0, 0))    
        self.connect((self, 0), (self.gsm_input_0, 0))    

    def get_OSR(self):
        return self.OSR

    def set_OSR(self, OSR):
        self.OSR = OSR
        self.set_samp_rate_out(1625000.0/6.0*self.OSR)
        self.gsm_input_0.set_osr(self.OSR)

    def get_chan_num(self):
        return self.chan_num

    def set_chan_num(self, chan_num):
        self.chan_num = chan_num

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.gsm_input_0.set_fc(self.fc)

    def get_osr(self):
        return self.osr

    def set_osr(self, osr):
        self.osr = osr

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.gsm_input_0.set_ppm(self.ppm)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.gsm_input_0.set_samp_rate_in(self.samp_rate)

    def get_samp_rate_out(self):
        return self.samp_rate_out

    def set_samp_rate_out(self, samp_rate_out):
        self.samp_rate_out = samp_rate_out
