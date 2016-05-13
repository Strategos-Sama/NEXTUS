#Open Source Bubba #|h3h3| vapenation
import socket
import sys
import os

print("""Welcome to:
  _   _   ______  __   __  _______   _    _    _____ 
 | \ | | |  ____| \ \ / / |__   __| | |  | |  / ____|
 |  \| | | |__     \ V /     | |    | |  | | | (___  
 | . ` | |  __|     > <      | |    | |  | |  \___ \ 
 | |\  | | |____   / ^ \     | |    | |__| |  ____) |
 |_| \_| |______| /_/ \_\    |_|     \____/  |_____/    V.3
 
By: STATEGOS_SAMA - SAIKONO.ORG

-- Enter a command - type help for a list of commands.
""")

def getBanner(ip, port):
    try:
     socket.setdefaulttimeout(3) #For how long it tries. (For all socket processes.)
     s = socket.socket() #Class and instance
     s.connect((ip, port))
     banner = s.recv(1024) #How many bits of data to retrieve (it only needs 25-ish usually when headers are actually returned XD)
     return(str(banner)) #Why? Because you cant do jack shit with a bytes object
    except:
     return #Return Zilch

def checkIfVuln(banner): #Checks banner against some banners with exploit-db entries
    f = open('vuln-banners.txt','r') #make it all one function?
    listvulns = f.readlines()#reread w bookmarks
    for line in listvulns: #1 TODOTODO(remove the bangbang and add the commands like add vuln, TODO Yep, it works, but its detecting its vulmerable on line two and stopping because there is an /n that shouldnt be there
        if line.strip('\n') in banner: #stred for a reason check its removing /n?
            f.close() #why des space below dafuq- cus lstrip removes from fucking start. dont comment for others comment for urse;f')
            return('Vulnerable')
    f.close()
    return


def mainrangestyle():
    print('[+] Input the range of ports to scan -----') #Gets range
    port = int(input('[+] Start from this port (first port to scan E.G. 21): '))
    finalport = int(input('[+] Last port (port to end on E.G. 80): '))

    try:
        host = socket.gethostbyname(input('What website do you want to scan? (if you want to scan a non-hosting IP type "NOPE": ')) #Gets URL's IP
    except:
        host = input('OK, Input the IP: ')

    #IPs & Port used for as getBanner's parameters ^^^

    filename = input("What would you like to call the vulnerable port log file (saved to directory containing this script- use only numbers and letters in name): ") + '.txt'
    file = open(filename, 'w')
    file.write('Vulnerable Open ports: \n')

    while port <= finalport:
        print('[+] Scanning port: ' + str(port))
        banner = getBanner(host, port)
        port = port + 1 #Counter

        if banner: #If banner doesn't return null...
            vulnerable = checkIfVuln(banner)
            if vulnerable:
                print('Grabbing banner from IP adress: ' + str(host) + ' | '+ 'Port used: ' + str(port))
                print('[+] ' + 'banner: ' + banner + ' is vulnerable - added to log file.')
                file.write('Port: ')
                file.write(str(port))
                file.write(' Banner: ')
                file.write(str(banner))
                file.write('\n')
            else:
                print('[+]There is info on the port but it is not vulnerable.')
        else:
            print('[+] No info on this port.')
            
    file.close()

    fileinfo = os.stat(filename)
        
    if fileinfo.st_size < 26:
        os.remove(filename)
        print('No vulnerable banners were found so no file was created.')

    else:
        print('Open Vulnerable Port banners log file created. - More info on Port Exploitation "on-the-line." :P')

def mainspecificstyle():
    
    iterations = int(input('How many ports will you want to scan? (Input a number E.G. 69) ')) # todo ! validation... sort of
    listUserPorts = []
    for x in range(0,iterations):        
        listUserPorts.append(int(input('Input a port you want to scan scan (Input a number E.G. 69): ')))
    print('All ports inputted... Moving on.')

    try:
        host = socket.gethostbyname(input('What website do you want to scan? (if you want to scan a non-hosting IP type "NOPE": ')) #Gets URL's IP
    except:
        host = input('OK, Input the IP: ')

    #IPs & Port used for as getBanner's parameters ^^^

    filename = input("What would you like to call the vulnerable port log file (saved to directory containing this script- use only numbers and letters in name.): ") + '.txt'
    file = open(filename, 'w')
    file.write('Vulnerable Open ports: \n')

    for port in listUserPorts: 
        print('[+] Scanning port: ' + str(port))
        banner = getBanner(host, port)
        port = port + 1 #Counter

        if banner: #If banner doesn't return null...
            vulnerable = checkIfVuln(banner)
            if vulnerable:
                print('Grabbing banner from IP adress: ' + str(host) + ' | '+ 'Port used: ' + str(port))
                print('[+] ' + 'banner: ' + banner + ' is vulnerable - added to log file.')
                file.write('Port: ')
                file.write(str(port))
                file.write(' Banner: ')
                file.write(str(banner))
                file.write('\n')
            else:
                print('[+] There is info on the port but it is not vulnerable.') #Consistent [+] refresh sublime
        else:
            print('[+] No info on this port.')

    file.close()

    fileinfo = os.stat(filename)
        
    if fileinfo.st_size < 26:
        os.remove(filename)
        print('No vulnerable banners were found so no file was created.')
    else:
        print('Open, Vulnerable Ports.Info and Uses log file created. - More info on Port Exp on-the-line. :P')


def maincommonstyle():
    listCommonPorts = [80, 443, 22, 21, 8080, 4567, 1723, 25, 53, 23, 3389, 110, 5000, 143, 8081, 135, 445, 111, 10000, 139] 

    try:
        host = socket.gethostbyname(input('What website do you want to scan? (if you want to scan a non-hosting IP type "NOPE": ')) #Gets URL's IP
    except:
        host = input('OK, Input the IP: ')

    #IPs & Port used for as getBanner's parameters ^^^

    filename = input("What would you like to call the vulnerable port log file (saved to directory containing this script- use only numbers and letters in name.): ") + '.txt'
    file = open(filename, 'w')
    file.write('Vulnerable Open ports: \n')

    for port in listCommonPorts:
        print('[+] Scanning port: ' + str(port))
        banner = getBanner(host, port)
        port = port + 1 #Counter

        if banner: #If banner doesn't return null...
            vulnerable = checkIfVuln(banner)
            if vulnerable:
                print('Grabbing banner from IP adress: ' + str(host) + ' | '+ 'Port used: ' + str(port))
                print('[+] ' + 'banner: ' + banner + ' is vulnerable - added to log file.')
                file.write('Port: ')
                file.write(str(port))
                file.write(' Banner: ')
                file.write(str(banner))
                file.write('\n')
            else:
                print('[+] There is info on the port but it is not vulnerable.')
        else:
            print('[+] No info on this port.')
            
    file.close()

    fileinfo = os.stat(filename)
        
    if fileinfo.st_size < 26:
        os.remove(filename)
        print('No commonly known vulnerable port banners were found so no file was created.')
    else:
        print('Open Vulnerable Ports log file created. - More info on Port Exp "on-the-line." Enjoy! - STRATEGOS@SAIKONO :P')

##def mainbody():


TypeOfPortScan = input('Would you like to scan COMMON ports, a RANGE of ports, or SPECIFIC ports. Answer with etiher: commonmode/rangemode/specificmode (no spaces): ')
TypeOfPortScan = TypeOfPortScan.upper()

if 'RANGEMODE' in TypeOfPortScan:
    mainrangestyle()

elif 'COMMONMODE' in TypeOfPortScan:
    maincommonstyle()

elif 'SPECIFICMODE' in TypeOfPortScan:
    mainspecificstyle()
    
else:
    print('Invalid Input, you will now exit the program.')
    sys.exit('Invalid Input, you will now exit the program.')

    #bruh it exits on terminal as soon as done, wont be a problem in browser?
    
#FInish it...    SQL, test it, UI  
#validate,recomment, beautify,optimise (1func)- Validation (or user's problem?)
#Use Exploit-DB Banner list API?
#Any way to get os and other info using this method?
#Nice Online GUI on SAIKONO _ HOSTING PHP ETC DJANGO
#Implement Command system - V3 Still works - Nevermind. Online UI. INIGO
#Reimplement for the WEB . sort of
#Make sure Exploits SQL is well done, PHP, Django course SAI.KO.NO Github Student hosting good website for meself
