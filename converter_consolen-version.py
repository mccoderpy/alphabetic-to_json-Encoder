import json
import os
import time


class converter():
    print('░▒▓███Welcome to the  alphabetic-to_json-encoder of mccoderpy aka. mccuber04#2960██▓▒░ ©mccoderpy 2021')
    loop= 0
    while True:
        inpu = input("Please enter the name of the file(with the ending) you want to convert in to an JSON>> ")
        if not inpu == '':
            if not os.path.isfile(inpu):
                print(f"Could not find the file <{inpu}> in this directiony. Please put it in the same directory this script is is placed in")

            if os.path.isfile(inpu):
                alphint0 = 0
                alphint1 = 0
                alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü']
                alp1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü']
                data = {}
                data["list"] = {}
                D = data["list"]

                for letter in alp:
                    alphint0 += 1
                    D[letter] = {}
                    for let in alp:
                        name = alp[alphint0-1]+let
                        D[letter][name] = []

                print(end='|█')
                zeile = 0
                with open(inpu, "r", encoding='utf-8') as file:
                    
                    for wort in file:
                        zeile += 1
                        if zeile == 300:
                            print(end='█')
                            time.sleep(0.1)
                            zeile = 0
                        weg_damit = wort.split('\n')
                        l = weg_damit.pop(0)
                        #print(l)
                        
                        for lu in alp1:
                            alphint1 += 1
                            if l.upper().startswith(lu):
                                b0 = lu.lower()
                                for let in alp:
                                    if l[1:2] == let:
                                        b1 = let
                                        #print(alphint1)
                                        #print(b0+b1)
                                        D[b0][b0+b1].append(f"{l}")
                print(end='| [100%]')
                weg_mit_die_endung = inpu.split(".")
                neuer_name = weg_mit_die_endung[0]
                with open(f'{neuer_name}.json', 'w', encoding='utf-8') as new:
                    json.dump(data, new)
                print(f"\nConverted file successfully\nFile saved as {os.getcwd()}\{neuer_name}.json")
                #(f'{neuer_name}.json')
                #print(data)
