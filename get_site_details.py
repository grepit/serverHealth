#! /usr/bin/env python
"""Check Server Health"""
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import os,json

class ServerHealthCheck():

    def __init__(self, base_url, port, tcp):
        self.base_url="www."+base_url
        self.port=port
        self.tcp=tcp
        self.url_path = self.tcp+"://"+self.base_url	
        self.ping_host()
        self.obtain_http_info()
        self.obtain_cert_info()

    def ping_host(self):
        #ping reesult
        print("PING INFO ....................................")
        response = os.system("ping -c 1 " + self.base_url)        
        #and then check the response...
        if response == 0:
            print(self.base_url, 'is up!')
        else:
            print(hostname, 'is down!')

    def obtain_http_info(self):
        print("SSL/TLS INFO ....................................")
        
        req = Request(self.url_path)
        try:
            response = urlopen(req,context=ssl._create_unverified_context())
            #htmlSource = response.read() 
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            print("http code:"+str(response.getcode())  )
            
    def obtain_cert_info(self):
        context = ssl.create_default_context()
        with socket.create_connection((self.base_url, self.port)) as socket_connection:
            with context.wrap_socket(socket_connection, server_hostname=self.base_url) as server_socket:
                print(server_socket.version())
                print(json.dumps(server_socket.getpeercert() , indent=2, sort_keys=True))
                der_cert = server_socket.getpeercert(False)
                der_cert_bin = server_socket.getpeercert(True)
                pem_cert = ssl.DER_cert_to_PEM_cert(server_socket.getpeercert(True))
                print(pem_cert)
                print ("cipher: "+str(server_socket.cipher()))
                print("SSL/TLS version:  "+server_socket.version())
                print(server_socket.shared_ciphers())
            server_socket.close()






host_name = "google.com"
prt = 443
tcp_it = "https"
serverHealthCheck = ServerHealthCheck(host_name, prt, tcp_it)
