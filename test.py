import scapy.all as scapy
from scapy.layers.http import HTTPRequest,HTTPResponse,HTTP

# 代理数据返回
def proxyServer():
    def responeseChange(packet):
        if packet.haslayer(HTTPRequest):
            print(packet)
            # 只要http的包
            if 'Raw' in packet:
                print('<---------------->')
                print(packet['Raw'].load)
    scapy.sniff(prn=fengxi,count=0,iface="Intel(R) Wi-Fi 6 AX201 160MHz",filter="tcp",store=0)


def fengxi(pkt):
    flag = False
    ip_layer = pkt.getlayer('IP')
    tcp_layer = pkt.getlayer('TCP')
    if tcp_layer:
        data = {
            'time': ip_layer.time,
            "ip": {'src': ip_layer.src, 'dst': ip_layer.dst, 'version': ip_layer.version},
            "tcp": {'seq': tcp_layer.seq, 'ack': tcp_layer.ack}
        }
        if pkt.haslayer(HTTPRequest):
            data['type'] = 'request'
            http_header = pkt[HTTPRequest].fields
            # print(http_header)
            http_header.pop("Unknown_Headers")
            data['hearder'] = http_header
            flag = True
        elif pkt.haslayer(HTTPResponse):
            data['type'] = 'response'
            http_header = pkt[HTTPResponse].fields
            print(http_header)
            http_header.pop("Unknown_Headers")
            data['hearder'] = http_header
            flag = True
        if flag:
            if 'Raw' in pkt:
                payload = pkt['Raw'].load
                if payload:
                    if isinstance(payload, str):
                        data['data'] = payload
            print(data)

proxyServer()