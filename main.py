import os

print("< Welcome to your QRCode Generator App >\n")


def GENERATE():
    
    choice = 'y'


    while (choice == 'y'):


        askURL = input("Enter the Website's URL:")

        os.system("curl qrenco.de/" + askURL)


        #asking Whether to run again

        choice = input("Wanna Do it Again (Y/N):")

GENERATE()