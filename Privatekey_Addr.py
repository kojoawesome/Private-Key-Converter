#!/usr/bin/env

from bit import Key
from datetime import date
from datetime import datetime

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

#tiem stamp
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
                private_key = keys.strip('\n').strip()
                prv = Key.from_hex(private_key)
                addr = prv.address
                # print(f'{private_key}:{addr}\n')
                # balance = prv.get_balance('usd')

                count += 1
                # writing files locally
                with open (f'Results by Codejoe.txt @ {current_time}', 'a') as writer:
                    writer.write(f'{private_key}:{addr}\n')
                if count == amount:
                    writer.close()
                    break



with open ('Logs.txt', 'a') as logger:
    logger.write(f'Start Point: {line_Starter} | No. of lines converted: {amount} | End point: {endLine} | Date: {date.today()}\n')
    logger.close()
    
