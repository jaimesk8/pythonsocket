# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import threading
import socket

clients = []

def main():
    #definir a caracterização do socket
    #identifcamos o IPV4(af_inet)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try: 
        server.bind(('172.29.1.167', 50000))
        
        #vai estar à escuta por 10 pedidos
        server.listen(10)
        
        print('Servidor iniciado. Aguarda conexões ...')
        
    except Exception as e:
       print('Não foi possível ligar ao servidor', str(e))
       return
   
    while True:
        client, addr = server.accept()
        clients.append(client)
        print('Cliente conectado', addr)
        
        thread = threading.Thread(target=messagesTreatment, args=(client,))
        thread.start()
        
def messagesTreatment(client):
    while True:
        try: 
            msg = client.recv(2048)
            if msg:
                broadcast(msg, client)
            else:
                deleteclient(client)
                break
            
        except Exception as e:
            print('Erro ao receber a mensagem do cliente', str(e))
            deleteclient(client)
            break
        
def broadcast(msg, sender):
    for client in clients:
        if client != sender: 
            try: 
                client.send(msg)
            except Exception as e:
                print('Erro ao enviar mensagem para o cliente', str(e))
                deleteclient(client)
                break
                
def deleteclient(client):
    if client in clients:
        clients.remove(client)
        client.close()
        print('Cliente desconectado ...')

if __name__ == '__main__':
    main()
        
                
                
    
    
    
    
    
    
    