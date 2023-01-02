#!/usr/bin/env

from bit import Key
from datetime import date

print ('''

██╗░░██╗███████╗██╗░░░██╗░█████╗░░█████╗░███╗░░██╗
██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██╔══██╗████╗░██║
█████═╝░█████╗░░░╚████╔╝░██║░░╚═╝██║░░██║██╔██╗██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░██╗██║░░██║██║╚████║
██║░╚██╗███████╗░░░██║░░░╚█████╔╝╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚══╝

    BTC Private Key Converter written by Codejoe
========================================================    
     \n''')

count = 0
#grabing file content
file = input('Enter file with .txt: \n')
amount = int(input('No. of keys to convert: '))
line_Starter = int(input('Enter line to begging from: '))
print('Converting...')

# file = 'Results by Codejoe.txt'
with open (file, 'r', encoding='utf-8', errors='ignore') as reader:
    for i, line in enumerate(reader):
        if i == line_Starter:
            for keys in reader.readlines():
                private_key = keys.strip('\n').strip()
                prv = Key.from_hex(private_key)
                addr = prv.address
                # print(f'{private_key}:{addr}\n')
                # balance = prv.get_balance('usd')

                count += 1
                # writing files locally
                with open ('Results by Codejoe.txt', 'a') as writer:
                    writer.write(f'{private_key}:{addr}\n')
                if count == amount:
                    writer.close()
                    break

with open ('Logs.txt', 'a') as logger:
    logger.write(f'line checkpoint: {line_Starter} | Date: {date.today()}\n')
    logger.close()
    
