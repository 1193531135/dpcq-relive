from scapy.all import *

def hui(p):
    p.show()
sniff(count=0,prn=hui)