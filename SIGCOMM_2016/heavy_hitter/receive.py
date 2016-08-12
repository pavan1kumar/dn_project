#!/usr/bin/python

# Copyright 2013-present Barefoot Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from scapy.all import sniff
from scapy.all import IP

VALID_IPS = ("10.0.0.1", "10.0.0.2", "10.0.0.3")
totals = {}

def handle_pkt(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        if src_ip in VALID_IPS:
            if src_ip not in totals:
                totals[src_ip] = 0
            totals[src_ip] += 1
            print ("Received from %s total: %s" %
                    (src_ip, totals[src_ip]))

def main():
    sniff(iface = "eth0",
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
