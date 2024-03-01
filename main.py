

import os
import time


print("< WELCOME TO THE QRCode GENERATOR APP >")
print() #for new line


def GENERATE():


    askURL = input("Enter the website's URL:")

    os.system("curl qrenco.de/" + askURL)






GENERATE()