#!/usr/bin/python3
from PIL import _imaging
from PIL import Image
import sys
from os import system, name
import os.path
import time                                     
from colorama import Fore, Back, Style          # pip3 install colorama



def main():


    path = "default.jpg"
    clear_screen()
    print(Style.BRIGHT + Fore.RED)
    print(" .S    S.           sSSs_sSSs           .S       S.          .S_sSSs           .S         .S_sSSs           .S")
    print(".SS    SS.         d%%SP~YS%%b         .SS       SS.        .SS~YS%%b         .SS        .SS~YS%%b         .SS")
    print("S%S    S%S        d%S'     `S%b        S%S       S%S        S%S   `S%b        S%S        S%S   `S%b        S%S")
    print("S%S    S%S        S%S       S%S        S%S       S%S        S%S    S%S        S%S        S%S    S%S        S%S")
    print("S%S SSSS%S        S&S       S&S        S&S       S&S        S%S    S&S        S&S        S%S    S&S        S&S")
    print("S&S  SSS&S        S&S       S&S        S&S       S&S        S&S    S&S        S&S        S&S    S&S        S&S")
    print("S&S    S&S        S&S       S&S        S&S       S&S        S&S    S&S        S&S        S&S    S&S        S&S")
    print("S&S    S&S        S&S       S&S        S&S       S&S        S&S    S&S        S&S        S&S    S&S        S&S")
    print("S*S    S*S        S*b       d*S        S*b       d*S        S*S    d*S        S*S        S*S    S*S        S*S")
    print("S*S    S*S        S*S.     .S*S        S*S.     .S*S        S*S   .S*S        S*S        S*S    S*S        S*S")
    print("S*S    S*S         SSSbs_sdSSS          SSSbs_sdSSS         S*S_sdSSS         S*S        S*S    S*S        S*S")
    print("SSS    S*S          YSSP~YSSY            YSSP~YSSY          SSS~YSSY          S*S        S*S    SSS        S*S")
    print("       SP                                                                     SP         SP                SP")
    print("       Y                                                                      Y          Y                 Y")
    print(Style.RESET_ALL)
    print("\n\nUse this program to hide a message within a given picture file or to reveal a hidden message!\n\n")    
    print("\n\nType in:\n\n\t[" + Fore.CYAN + "1" + Style.RESET_ALL + "]\t\t\t=>\tto hide a message within the default picture"+
                                    "\n\t[" + Fore.CYAN + "2" + Style.RESET_ALL + "]\t\t\t=>\tto hide a message within a custom picture"+
                                    "\n\t[" + Fore.CYAN + "3" + Style.RESET_ALL + "]\t\t\t=>\tto reveal a hidden message" +
                                    "\n\t[" + Fore.CYAN + "any other key" + Style.RESET_ALL + "]\t\t=>\tto exit the program\n\n")
    option = input(Fore.RED + "HOUDINI >>  " + Style.RESET_ALL)
    if option != "1" and option != "2" and option != "3":
        sys.exit(0)


    elif option == "1":
        clear_screen()                          
        time.sleep(0.6)
        print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Using default image ...")
        image = open_image(path)
        hide_msg(image)
   
    elif option == "2":
        path_set = False
        clear_screen()
        while path_set == False:
            print("[" + Fore.GREEN + "!" + Style.RESET_ALL + "] Type in the path or [" + Fore.CYAN + "exit" + Style.RESET_ALL + "] to leave:\n")
            file_path = input(Fore.RED + "HOUDINI >>  " + Style.RESET_ALL)
            if file_path == "exit":
                sys.exit(0)
            
            elif os.path.exists(file_path):
                clear_screen()                  
                print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Using custom image ...")
                image = open_image(file_path)
                hide_msg(image)
                path_set = True

            else:
                print("\n\n[" + Fore.RED + "/" + Style.RESET_ALL + "] Path does not exitst. Type in new path ...\n")

            

    else:
        path_set = False
        clear_screen()
        while path_set == False:           
            print("[" + Fore.GREEN + "!" + Style.RESET_ALL + "] Type in the path or [" + Fore.CYAN + "exit" + Style.RESET_ALL + "] to leave:\n")
            file_path = input(Fore.RED + "HOUDINI >>  " + Style.RESET_ALL)

            if file_path == "exit":
                sys.exit(0)

            elif os.path.exists(file_path):
                clear_screen()
                time.sleep(0.6)
                print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Open file ...")
                image = open_image(file_path)
                reveal_msg(image)
                path_set = True

            else:
                print("\n\n[" + Fore.RED + "/" + Style.RESET_ALL + "] Path does not exitst. Type in new path ...\n")
    
    
       
              


def open_image(file_path):

    tmp = Image.open(file_path)
    return tmp


def hide_msg(img):
    
    image = img
    tmp_img = image.load()
    width, height = image.size
    bin_msg = []
    split_bin_msg = []
    escape_seq = "#~#~#"

    msg = fetch_message(width, height)
    time.sleep(0.6)
    print("\n\n[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Hiding the message ...")
    msg += escape_seq
    list(msg)


    for symbol in msg:
        tmp = ''.join(format(ord(i), 'b') for i in symbol)
        if len(tmp) < 8:
            tmp = tmp.zfill(8)
        bin_msg.append(tmp)

    for word in range(0, len(bin_msg)):
        for bin in bin_msg[word]:
            split_bin_msg.append(bin)

    count = 0
    finished = False

    for i in range(0, width):
        if finished == True:
            break

        for j in range(0, height):
            pixel_value = img.getpixel((i,j))
            tmp_pix = format(pixel_value[2], 'b')
            tmp = str(tmp_pix)
            list(tmp)

            if tmp[-1] != split_bin_msg[count]:
                tmp = tmp[:len(tmp)-1] + split_bin_msg[count]

            number = int(tmp, 2)
            new_val = (pixel_value[0], pixel_value[1], number)
            tmp_img[i,j] = new_val
            count += 1

            if count == len(split_bin_msg):
                finished = True
                break

    time.sleep(0.6)
    print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Message successfully hidden!")
    image_name = "/new_image.png"

    home = os.path.expanduser("~")
    home = home.replace("\\","/")
    save_path = home + image_name
    image.save(save_path)
    time.sleep(0.6)
    print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Picture with hidden message saved to: ", save_path)


def reveal_msg(img):
    
    width, height = img.size
    hidden_msg = []
    bin_msg = []
    decoded_msg = []
    finished = False
    time.sleep(0.6)
    print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Revealing original message ...")


    for i in range(0, width):
        if finished == True:
            break


        for j in range(0, height):
            pixel_value = img.getpixel((i,j))
            tmp_pix = format(pixel_value[2], 'b')
            tmp = str(tmp_pix)
            list(tmp)
            hidden_msg.append(tmp[-1])

            if len(hidden_msg) == 8:
                letter_bin = "".join(hidden_msg)
                bin_msg.append(letter_bin)
                hidden_msg = []
                if len(bin_msg) > 5:
                    for symbol in bin_msg:
                        number = int(symbol, 2)
                        decode = ''.join(format(chr(number)))
                        decoded_msg.append(decode)
                    
                    message = ''.join(decoded_msg)

                    if message.find("#~#~#") != -1:
                        finished = True
                        original_message = message[:-5]
                        time.sleep(0.6)
                        print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "] Message successfully revealed!\n")
                        break

                    else:
                        decoded_msg = []
                        message = ""

    time.sleep(0.6)
    print("\n[" + Fore.GREEN + "!" + Style.RESET_ALL + "] The hidden message is: \n\n")
    print(original_message + "\n\n\n")

def fetch_message(width, height):
    
    text_complete = False
    msg = ""

    max_length = (width * height) / 8 - (8 * 5)

    print("\n[" + Fore.GREEN + "!" + Style.RESET_ALL + "] Your message must not be longer than " + str(int(max_length)) + " characters.\n"+
          "    If you need more characters, use a larger picture file.")
    print("\n[" + Fore.GREEN + "!" + Style.RESET_ALL + "] Start new line and type [" + Fore.CYAN + "message_complete" + Style.RESET_ALL + "] when your message is complete.\n\n")

    while not text_complete:
        line = input(Fore.RED + "HOUDINI >>  " + Style.RESET_ALL)
        
        if line.find("message_complete") != -1:
            if len(msg) < max_length:
                text_complete = True
                break
            
            else:
                print("\n[" + Fore.RED + "/" + Style.RESET_ALL + "] Message too long. You used " + str(len(msg)) + " characters, but only " + str(int(max_length)) + " characters are possible."+
                      "\n\n[" + Fore.GREEN + "!" + Style.RESET_ALL + "] Start new line and type [" + Fore.CYAN + "message_complete" + Style.RESET_ALL + "] when your message is complete.\n\n")
                msg = ""

        msg += line + "\n"

    return msg


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
