from PIL import Image
from numpy import array 
import os


def encodeImg():
    img_loc = ''
    string = ''
    saveName = ''
    os.system('cls')
    print("   --------------------------------Image Steganography T1-------------------------------\n")
    print("   ---------------------------------Insert Text To Image--------------------------------\n")
    img_loc = input("   --Select the Image location: ")
    if img_loc.find("\\")!=-1:
        img_loc.replace("\\", "//")
    if os.path.isfile(img_loc)==False:
        print("Sorry the file do not exist")
        input("Press enter to continue: ")
        main()
    string = input("   --Enter the text to Insert: ")
    saveName = input("   --Name of the output file[except: <>/?|\\*:-]: ")
    try:
        img = Image.open(img_loc)
    except Exception as e:
        print(" Something error with the Image file: " + str(e))
        input("Press enter to continue: ")
        main()
    encodeArray = array(img)    #saving the image as an array so that operation can be performed
    size = img.size
    print("log: ")
    print("Image Dimension: " + str(size[0]) + "x" + str(size[1]))
    totalChar = size[0]*size[1] - 100
    print("Total number of Charactor Possible: " + str(int(totalChar/8)))
    print("Inseting the text.........")
    to_binary = []
    for head in range(0, 3, 1):
        to_binary.append('00000000')
    to_binary.extend([bin(ord(x))[2:].zfill(8) for x in string])   #cponvert str to binary 8bit
    for tail in range(0, 5, 1):
        to_binary.append('00000000')
    print("Number of charactor added: " + str(len(string)))
    row = 0
    column = 0
    size_column, size_row = img.size
    for eachchar in to_binary:
        for bit in eachchar:
            if bit=='1':
                if encodeArray[row][column][0]%2==1 and encodeArray[row][column][0]!=255:
                    encodeArray[row][column][0] += 1
                elif encodeArray[row][column][0]%2==1 and encodeArray[row][column][0]==255:
                    encodeArray[row][column][0] -= 1
                column += 1
            elif bit=='0':
                if encodeArray[row][column][0]%2==0 and encodeArray[row][column][0]!=0:
                    encodeArray[row][column][0] -= 1
                elif encodeArray[row][column][0]%2==0 and encodeArray[row][column][0]==0:
                    encodeArray[row][column][0] += 1
                column += 1
            if column >= size_column:
                    column = 0
                    row += 1
    print("Saving the file...........")
    try:
        Image.fromarray(encodeArray).save(img_loc.replace(os.path.basename(img_loc), saveName + ".PNG"))
    except Exception as e:
        print("Something went wrong while saving the file: ")
        input("Press enter to continue: ")
        main()
    img.close()
    print("File saved: " + img_loc.replace(os.path.basename(img_loc), saveName + ".PNG"))
    input("   --Press enter to continue: ")
    main()


def decodeImg():
    img_loc = ''
    os.system('cls')
    print("   --------------------------------Image Steganography T1-------------------------------\n")
    print("   --------------------------------Extract Text from Image------------------------------\n")
    img_loc = input("   --Select the Image location: ")
    if img_loc.find("\\")!=-1:
        img_loc.replace("\\", "//")
    if os.path.isfile(img_loc)==False:
        print("File not found: ")
        input("Press enter to continue: ")
        main()
    print("Decoding the text......")
    try:
        img2 = Image.open(img_loc)
    except Exception as e:
        print("Not able to import image: " + str(e))
        input("Press enter to continue: ")
        main()
    decodeArray = array(img2)    #saving the image as an array so that operation can be performed
    x = 0
    data = ''
    store = []
    for n in range(0, 24, 1):
        if decodeArray[0][n][0]%2==1:
            x += 1
    if x==24:
        for x in range(0, len(decodeArray), 1):
            for y in range(0, len(decodeArray[x]), 1):
                if decodeArray[x][y][0]%2==0:
                    data = data + '1'
                elif decodeArray[x][y][0]%2==1:
                    data = data + '0'
                if len(data)==8:
                    store.append(data)
                    data = ''
                if len(store)>=5 and store[-1]=='00000000' and store[-2]=='00000000' and store[-3]=='00000000' and store[-4]=='00000000' and store[-5]=='00000000':
                    break
            if len(store)>=5 and store[-1]=='00000000' and store[-2]=='00000000' and store[-3]=='00000000' and store[-4]=='00000000' and store[-5]=='00000000':
                    break
    else:
        print("   --Sorry the file do not contain any infromation, or the file may be tempered.")
    encoded = ''.join([chr(int(x, 2)) for x in store])
    print("Text: \n" + encoded)
    input("   --Press enter to continue: ")
    main()


def about():
    os.system('cls')
    print("\n   --------------------------------Image Steganography T1-------------------------------\n")
    print("PROJECT IMAGE STEGANOGRAPHY T1\n")
    print("            This tool convert the text to 8bit ASCII and then 1 denote even and 0 denote the odd this relation")
    print("   are made in the red end of the spectrum. No encoding of the bits are made. It has a head of 3 '00000000'")
    print("   and tail of 5 '00000000', this help the software to understand where to start and where to end. Image can")
    print("   be of .JPG or .PNG format, and the text can contain any of the letters and symbols. Text can only be smaller")
    print("   than the height*width/8 letters. Any thing greater than this will raise error. The image will be slightly")
    print("   changed and will not be visible to the human eye. Do not alter the Image using any Image Editor or converter")
    print("   any type of Image manipulation will result in inability to decode.")
    print("\n   Some Donots: ")
    print("            [1].Do not Manipulate the Image.")
    print("            [2].Do not convert the Image.")
    print("            [3].Do not upload the Image to Online sites, as this may change the Image.")
    input("Press enter to continue.")
    main()


def main():
    os.system('cls')
    print("   --------------------------------Image Steganography T1-------------------------------\n")
    print("\n   --A tool to hide text inside a Image, without much of the resolution of the image being changed.")
    print("   --Takes image with: .jpg or .png or any other common format and adds text and saved it to a .PNG file")
    print("   --Decode with the same decose window here.")
    print("\n            [1].Insert Text to Image            [2].Extract text from Image")
    print("\n            [3].About                           [4].Exit\n")
    try:
        inp = int(input("   --Enter the action to perform: "))
    except Exception as e:
        print("   --Enter a valid digit: ")
        input("   --Press enter to continue.")
        main()
    if inp==1:
        encodeImg()
    elif inp==2:
        decodeImg()
    elif inp==3:
        about()
    elif inp==4:
    	exit()

os.system('cls')
main()