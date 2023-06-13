import os, sys


listofFile = os.listdir('./results')
count = 0
for i in listofFile:
    if i[:6] == 'result':
        count += 1
terminal_command = f"mkdir ./results/result-{count}" 
os.system(terminal_command)
os.system(f'npx artillery run -o ./results/result-{count} loadtest.json')
resultJson = os.listdir(f'./results/result-{count}')
resultJsonName = resultJson[0]
os.system(f'npx artillery report ./results/result-{count}/{resultJsonName}')
