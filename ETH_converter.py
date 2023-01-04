#!/usr/bin/env

from hdwallet import HDWallet
from hdwallet.symbols import ETH as eth
from lxml import html
import requests
from fake_useragent import UserAgent
from datetime import date
from datetime import datetime

print ('''

██╗░░██╗███████╗██╗░░░██╗░█████╗░░█████╗░███╗░░██╗
██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██╔══██╗████╗░██║
█████═╝░█████╗░░░╚████╔╝░██║░░╚═╝██║░░██║██╔██╗██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░██╗██║░░██║██║╚████║
██║░╚██╗███████╗░░░██║░░░╚█████╔╝╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚══╝

    ETH Private Key Converter written by Codejoe
========================================================    
     \n''')

#time stamp
count = 0
time = datetime.now()
current_time = time.strftime("%H:%M")

#grabing file content
file = input('Enter file with .txt: \n')
amount = int(input('No. of keys to convert: '))
line_Starter = int(input('Enter line to begin from: '))
print('Converting...')

#getting line end
endLine = line_Starter + amount

# file = 'Results by Codejoe.txt'
with open (file, 'r', encoding='utf-8', errors='ignore') as reader:
    for i, line in enumerate(reader):
        if i == line_Starter:
            for keys in reader.readlines():
                Private_key = keys.strip('\n').strip()
                hd: HDWallet = HDWallet(symbol = eth)
                hd.from_private_key(private_key=Private_key)
                addr = hd.p2pkh_address()
                # print(f'{private_key}:{addr}\n')
                # balance = prv.get_balance('usd')

                count += 1
                # writing files locally
                with open (f'Eth results by Codejoe.txt @ {current_time}', 'a') as writer:
                    writer.write(f'{Private_key}:{addr}\n')
                if count == amount:
                    writer.close()
                    break



with open ('Eth logs.txt', 'a') as logger:
    logger.write(f'Start Point: {line_Starter} | No. of lines converted: {amount} | End point: {endLine} | Date: {date.today()}\n')
    logger.close()
    
