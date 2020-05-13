# 									Project-Image-Steganography
Developing tools for hiding text, documents, images, audio, video e.t.c files inside an Image.

-- The setup for the programe is present in the /exe folder, and source code in the /source folder.


>> Image Steganography T1

This tool help in hiding text inside an .jpg image. Source code is present in the source/ directory. Please install the exe and enjoy.

About:  This tool convert the text to 8bit ASCII and in it 1 denote even and 0 denote the odd this relation
		are made in the red end of the spectrum. The tool encodes a head of 3 '00000000'and tail of 5 '00000000', this help the software to understand where to start and where to end. Image can be of .JPG or .PNG format, and the text can contain any of the letters and symbols. Text can only be smaller than the (height*width)pixel/8 letters. Any thing greater than this will raise error. The image will be slightly changed and will not be visible to the human eye. Do not alter the Image using any Image Editor or any Image converter as this result in error to decode the message.

Built on Python with module in use: pillow, numpy, os. 
Compiled using the pyinstaller 3.6. 


>> Image Steganography T2

An Improved version of the T1, with features of hiding any type of file inside an image .jpg or .png, to a .png file.

About: 	A step up from the Project Image Steganography T1. This tool help the user to store any file (be it: .png, .jpg, .pdf, 				.zip, .rar, .docx, .pptx, or any file), inside an image file preferably a .jpg or .png file. Without any change in the 				image, this technique uses the same technique as the T1 version, i.e. to change the odd or even digit in red end of the 			spectrum, also the file name of the hidden file is encoded into the image, and so as soon as you choose the image to 				decode, it generated the file without any further assistance. The data of the file is stored as 3 First Header >> FILENAME 			>> 4 Second Header >> File Data >> 10 Tail, the number respresent the number of repeats of '00000000' for head and 					'10101010', '11001100' for the tail. This is essential for proper detection of the file data. As usual the Output PNG file 			should not be altered at any cost, and if so done then it will not be able to recover the hidden file, or the hidden file 			will be corrupted.

Built on Python with module in use: pillow, numpy, os, binascii
Compiled using the pyinstaller 3.6.