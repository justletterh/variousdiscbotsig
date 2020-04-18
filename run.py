import subprocess
import asyncio
import threading
import time
import os
startscreen =f"\033[32;1m.----------------.  .----------------.  .----------------.  .----------------.\n| \033[34;1m.--------------. \033[32;1m|| \033[34;1m.--------------. \033[32;1m|| \033[34;1m.--------------. \033[32;1m|| \033[34;1m.--------------. \033[32;1m|\n| \033[34;1m|\033[30;1m  ____  ____  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   ______     \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m     ____     \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  _________   \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m |_   ||   _| \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  |_   _ \    \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   .'    `.   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m |  _   _  |  \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m   | |__| |   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m    | |_) |   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  /  .--.  \  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m |_/ | | \_|  \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m   |  __  |   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m    |  __'.   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  | |    | |  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m     | |      \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m  _| |  | |_  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   _| |__) |  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  \  `--'  /  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m    _| |_     \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m |____||____| \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  |_______/   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   `.____.'   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   |_____|    \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|\n| \033[34;1m'--------------' \033[32;1m|| \033[34;1m'--------------' \033[32;1m|| \033[34;1m'--------------' \033[32;1m|| \033[34;1m'--------------' \033[32;1m|\n '----------------'  '----------------'  '----------------'  '----------------'\n .----------------.  .----------------.  .----------------.  .----------------.\n| \033[34;1m.--------------. \033[32;1m|| \033[34;1m.--------------. \033[32;1m|| \033[34;1m.--------------. \033[32;1m|| \033[34;1m.--------------. \033[32;1m|\n| \033[34;1m|\033[30;1m   ______     \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m     ____     \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m     ____     \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  _________   \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m  |_   _ \    \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   .'    `.   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   .'    `.   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m |  _   _  |  \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m    | |_) |   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  /  .--.  \  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  /  .--.  \  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m |_/ | | \_|  \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m    |  __'.   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  | |    | |  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  | |    | |  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m     | |      \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m   _| |__) |  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  \  `--'  /  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m  \  `--'  /  \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m    _| |_     \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m  |_______/   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   `.____.'   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   `.____.'   \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m   |_____|    \033[34;1m| \033[32;1m|\n| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|| \033[34;1m|\033[30;1m              \033[34;1m| \033[32;1m|\n| \033[34;1m'--------------' \033[32;1m|| \033[34;1m'--------------' \033[32;1m|| \033[34;1m'--------------' \033[32;1m|| \033[34;1m'--------------' \033[32;1m|\n '----------------'  '----------------'  '----------------'  '----------------' \033[m"
print(startscreen)
print('\033[37;1mM\033[31;1ma\033[33;1md\033[32;1me \033[34;1mb\033[36;1my \033[35;1mH\033[m')
time.sleep(1)
print('\033[35;1m------------------------------------------'+'\033[32;1m'+'['+'\033[31;1m'+'START'+'\033[32;1m'+']'+ '\033[m'+'\033[35;1m------------------------------------------\033[m')
def py():
    process = subprocess.Popen(['python3', '-u', 'bot.py'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[33;1mpyt\033[36;1mhon\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[33;1mpyt\033[36;1mhon\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[31;1mru\033[35;1mby\033[m] ', output.strip())
            break
def rb():
    process = subprocess.Popen(['ruby', 'bot.rb'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[31;1mru\033[35;1mby\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[31;1mru\033[35;1mby\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[31;1mru\033[35;1mby\033[m] ', output.strip())
            break
def js():
    process = subprocess.Popen(['node', 'bot.js'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[35;1mja\033[33;1mvascri\033[35;1mpt\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[35;1mja\033[33;1mvascri\033[35;1mpt\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[35;1mja\033[33;1mvascri\033[35;1mpt\033[m] ', output.strip())
            break
def ph():
    process = subprocess.Popen(['php', 'php/bot.php'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[34;1mp\033[30;1mh\033[34;1mp\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[34;1mp\033[30;1mh\033[34;1mp\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[34;1mp\033[30;1mh\033[34;1mp\033[m] ', output.strip())
            break
def lu():
    process = subprocess.Popen(['luvit', 'bot.lua'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[31;1ml\033[32;1mu\033[34;1ma\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[31;1ml\033[32;1mu\033[34;1ma\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[31;1ml\033[32;1mu\033[34;1ma\033[m] ', output.strip())
            break
def go():
    process = subprocess.Popen(['go', 'run', 'bot.go'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[36;1mg\033[32;1mo\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[36;1mg\033[32;1mo\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[36;1mg\033[32;1mo\033[m] ', output.strip())
            break
def cr():
    process = subprocess.Popen(['crystal', 'cr/bot.cr'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[31;1mcry\033[33;1ms\033[30;1mtal\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[31;1mcry\033[33;1ms\033[30;1mtal\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[31;1mcry\033[33;1ms\033[30;1mtal\033[m] ', output.strip())
            break
def vb():
    process = subprocess.Popen(['cd vb/Example1&&dotnet run'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True,
                               shell=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[35;1mvisual\033[34;1mbasic\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[35;1mvisual\033[34;1mbasic\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[35;1mvisual\033[34;1mbasic\033[m] ', output.strip())
            break
def da():
    process = subprocess.Popen(['dart', 'dart/bot.dart'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        if output.strip() != '':
            print('[\033[34;1mda\033[36;1mrt\033[m] ', output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('[\033[34;1mda\033[36;1mrt\033[m] ', 'RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print('[\033[34;1mda\033[36;1mrt\033[m] ', output.strip())
            break
async def main():
    global threads
    threads = []
    pyt = threading.Thread(target=py)
    pyt.start()
    threads.append(pyt)
    rub = threading.Thread(target=rb)
    rub.start()
    threads.append(rub)
    jas = threading.Thread(target=js)
    jas.start()
    threads.append(jas)
    php = threading.Thread(target=ph)
    php.start()
    threads.append(php)
    lua = threading.Thread(target=lu)
    lua.start()
    threads.append(lua)
    gol = threading.Thread(target=go)
    gol.start()
    threads.append(gol)
    cry = threading.Thread(target=cr)
    cry.start()
    threads.append(cry)
    vib = threading.Thread(target=vb)
    vib.start()
    threads.append(vib)
    dar = threading.Thread(target=da)
    dar.start()
    threads.append(dar)
asyncio.run(main())
for process in threads:
    process.join()
print('\033[35;1m------------------------------------------'+'\033[32;1m'+'['+'\033[31;1m'+'DONE'+'\033[32;1m'+']'+ '\033[m'+'\033[35;1m------------------------------------------\033[m')
print('\033[37;1mM\033[31;1ma\033[33;1md\033[32;1me \033[34;1mb\033[36;1my \033[35;1mH\033[m')
