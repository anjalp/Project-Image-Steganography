from PIL import Image
from numpy import array
import os
import binascii


def hide_file():
    os.system('cls')
    print("\n   --------------------------------Image Steganography T2-------------------------------\n")
    print("   ------------------------------Hide a File Inside an Image----------------------------\n")
    print("   --Select the file to hide, Image to store and Output file name.\n")
    to_binary = []   #stores the binary of the file data: in order: FirstHeader--Filename--SecondHeader--FileData--Tail(10 digit long).
    for head in range(0, 3, 1):  
        to_binary.append('00000000')    #first head to find weather it contain a valid hidden data 3 digit long
    file = input("   --Enter the location of the file to hide(.txt, .pdf, .jpg, .png, .zip or any other type): ")
    if file.find("\\")!=-1:
        file.replace("\\", "//")
    if os.path.isfile(file)==False:
        print("   --Sorry no such file found..")
        print("   --Please try again")
        input("Press enter to continue.")
        main()
    else:
        file_name = os.path.basename(file)   #filename for storing in the data
        to_binary.extend([bin(ord(x))[2:].zfill(8) for x in file_name])   #encoding the filename into the image.
        for head in range(0, 4, 1):    #second head to differentiate from the first head-filename-second head-data-tail. 4digit long
            to_binary.append('00000000')
        with open(file, 'rb') as fileOpen:
            byte = fileOpen.read(1)
            try:
                i = ord(byte)
                data = "{0:b}".format(i)
                if len(data)!=8:
                    for x in range(0, 8-len(data), 1):
                        data = "0" + data
                to_binary.append(data)
            except:
                print("   --Oops file seems empty.")
                input("Press enter to continue:")
                main()
            while byte:
                byte = fileOpen.read(1)
                try:
                    i = ord(byte)
                    data = "{0:b}".format(i)
                    if len(data)!=8:
                        for x in range(0, 8-len(data), 1):
                            data = "0" + data
                    to_binary.append(data)
                except:
                    print("   --Finish Reading the File.")
    for tail in range(0, 5, 1):   #Tail contain 2 types of code each alternating. 10 digit long
        to_binary.append('10101010')
        to_binary.append('11001100')
    img_loc = input("   --Select the Image location: ")
    if img_loc.find("\\")!=-1:
        img_loc.replace("\\", "//")
    if os.path.isfile(img_loc)==False:
        print("Sorry the file do not exist")
        input("Press enter to continue: ")
        main()
    saveName = input("   --Name of the output file[except: <>/?|\\*:-]: ")
    try:
        img = Image.open(img_loc)
    except Exception as e:
        print("Something error with the Image file: " + str(e))
        input("Press enter to continue: ")
        main()
    encodeArray = array(img)    #saving the image as an array so that operation can be performed
    size = img.size
    print("log: ")
    print("Image Resolution: " + str(size[0]) + "x" + str(size[1]))
    totalChar = size[0]*size[1] - 100
    possible_char = int(totalChar/8)
    present_char = len(to_binary)
    if possible_char >= present_char:
        print("Maximum size of file to Hide: " + str(int(totalChar/8000)) + "KB" + " for the selected Image.")
        print("Size of Your file to hide: " + str(len(to_binary)/1000) + "KB")
        print("Inseting the file.........")
        row = 0
        column = 0
        size_column, size_row = img.size
        for eachchar in to_binary:   #Algorithm to change odd or even for 0 or 1 respectively.
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
        print("File successfully inserted.............")
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
    else:
        print("   --Sorry the file is quite bigger than the Image selected, try with a higher resolution Image")
        input("Press enter to continue.")
        main()


def find_filename(data):
    filename = ''
    next_stop = 0
    for each in range(0, len(data[3:]), 1):
        if each<=len(data[3:])-4:
            if data[each]=='00000000' and data[each+1]=='00000000' and data[each+2]=='00000000' and data[each+3]=='00000000':
                position = each
                break
    name_data = data[3:position]
    filename = ''.join([chr(int(x, 2)) for x in name_data])
    next_stop = position + 4
    return next_stop, filename

def extract_file():
    img_loc = ''
    os.system('cls')
    print("\n   --------------------------------Image Steganography T2-------------------------------\n")
    print("   --------------------------------Extract File from Image------------------------------\n")
    print("   --Select the Image from where you want to extract the hidden file.")
    img_loc = input("   --Select the PNG Image location: ")
    if img_loc.find("\\")!=-1:
        img_loc.replace("\\", "//")
    if os.path.isfile(img_loc)==False:
        print("File not found: ")
        input("Press enter to continue: ")
        main()
    print("   --Decoding the image......")
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
    for n in range(0, 24, 1):   # checking for the head binary for verification.
        if decodeArray[0][n][0]%2==1:
            x += 1
    if x==24:  #if header verified then read the whole image
        for x in range(0, len(decodeArray), 1):   #algorith to extract the odd or even to 0 or 1 respectively.
            for y in range(0, len(decodeArray[x]), 1):
                if decodeArray[x][y][0]%2==0:
                    data = data + '1'
                elif decodeArray[x][y][0]%2==1:
                    data = data + '0'
                if len(data)==8:
                    store.append(data)
                    data = ''   #BELOW CODE: verify that the tail has been reached.
                if len(store)>=10 and store[-1]=='11001100' and store[-2]=='10101010' and store[-3]=='11001100' and store[-4]=='10101010' and store[-5]=='11001100' and store[-6]=='10101010' and store[-7]=='11001100' and store[-8]=='10101010' and store[-9]=='11001100' and store[-10]=='10101010':
                    break
            if len(store)>=10 and store[-1]=='11001100' and store[-2]=='10101010' and store[-3]=='11001100' and store[-4]=='10101010' and store[-5]=='11001100' and store[-6]=='10101010' and store[-7]=='11001100' and store[-8]=='10101010' and store[-9]=='11001100' and store[-10]=='10101010':
                    break
    else:
        print("   --Sorry the file do not contain any file, or the image may be tempered.")
        input("Press enter to continue.")
        main()
    encoded = ''.encode()   #engine to convert the binary 1 and 0 to hex bytes that can be written to a file.
    next_stop, filename = find_filename(store)
    print("   --File detected: " + filename)
    print("   --Trying to restore...........")
    for each in store[next_stop:-10]: 
        each = hex(int(each, 2))
        if each.find('0x')!=-1 and len(each)==4:
            encoded = encoded + binascii.unhexlify(each.replace('0x', ''))
        elif len(each)==3:
            encoded = encoded + binascii.unhexlify(each.replace('0x', '0'))
        else:
            encoded = encoded + each.encode()
    print("   --Restore successful........")
    print("   --Saving the file: " + filename)
    try:
        with open(img_loc.replace(os.path.basename(img_loc), filename), 'wb') as filesave:
            filesave.write(encoded)
            filesave.close()
    except Exception as e:
        print("   --Oops the file extraction was successful, but was not able to save the file.")
        print("   --It seems that the directory of the PNG image is a read only, try moving the PNG file and try again.")
        input("Press enter to continue:")
        main()
    print("   --File saved at: " + img_loc.replace(os.path.basename(img_loc), filename))
    input("Press enter to continue:")
    main()


def about():
    os.system('cls')
    print("\n   --------------------------------Image Steganography T2-------------------------------\n")
    print("PROJECT IMAGE STEGANOGRAPHY T2\n")
    print("         A step up from the Project Image Steganography T1. This tool help the user to store any")
    print("   file (be it: .png, .jpg, .pdf, .zip, .rar, .docx, .pptx, .~~ any file), inside an image file")
    print("   preferably a .jpg or .png file. Without any change in the image, this technique uses the same")
    print("   technique as the T1 version, i.e. to change the odd or even digit in red end of the spectrum")
    print("   Also the file name of the hidden file is encoded into the image, and so as soon as you choose the")
    print("   image to decode, it generated the total file without any glitch. The data of the file is stored as")
    print("   3 First Header >> FILENAME >> 4 Second Header >> File Data >> 10 Tail, the number respresent the ")
    print("   number of repeats of '00000000' for head and '10101010', '11001100' for the tail. This is essential")
    print("   for proper detection of the file data.")
    print("\n      As usual the Output PNG file should not be altered at any cost, and if so done then it will")
    print("   not be able to recover the hidden file, or the hidden file will be corrupted.")
    print("\n   Some Do Not's: \n")
    print("            [1].Do not Manipulate the Image.")
    print("            [2].Do not convert the Image.")
    print("            [3].Do not upload the Image to Online sites, as this may change the Image.")
    print("\n   Some Demerits: \n")
    print("            [a]. Please do not use this technique to hide your importnat files, as these technique")
    print("                 are vulnerable to attacks and not safe. Use this as an educational purpose only.")
    print("            [b]. The PNG generated will be quite large due to loss less compression employed.\n")
    input("Press enter to continue.")
    main()


def main():
    os.system('cls')
    print("\n   --------------------------------Image Steganography T2-------------------------------\n")
    print("\n   --A tool to hide File inside a Image, without much  of the image being changed.")
    print("   --Takes image with: .jpg or .png or any other common format and adds text and saved it to a .PNG file")
    print("   --Decode with the same decode window here.")
    print("\n            [1].Hide a File into Image          [2].Extract File from Image")
    print("\n            [3].About                           [4].Exit\n")
    try:
        inp = int(input("   --Enter the action to perform: "))
    except Exception as e:
        print("   --Enter a valid digit: ")
        input("Press enter to continue.")
        main()
    if inp==1:
        hide_file()
    elif inp==2:
        extract_file()
    elif inp==3:
        about()
    elif inp==4:
        exit()

os.system('cls')
main() 