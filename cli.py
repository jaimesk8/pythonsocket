#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:28:26 2023

@author: jaime
"""

import threading 
import socket

def main(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try: 
        client.connect(('172.29.1.167', 50000))
        
    except ConnectionRefusedError: 
        print('\nNão foi possível conectar ao servidor\n')
        return
    
    username = input('Digitalize o nome do utilizador.')
    print('\nConectado\n')
    
    thread1 = threading.Thread(target=receiveMessages, args=(client,))
    thread2 = threading.Thread(target=sendMessages, args=(client, username))
    
    thread1.start()
    thread2.start()
    

def receiveMessages(client):
    while True:
        try:
            msg=client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except ConnectionResetError:
            print('\nA conexão com o servidor foi encerrada')
            client.close()
            break
        
    
def sendMessages(client, username):
    while True:
        try: 
            msg = input('')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
            
        except ConnectionResetError:
            print('/nA conexão com o servidor foi encerrada')
            break
main()
    
    
    
    
    
    
    
    
    