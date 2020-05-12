# 									Project-Image-Steganography
Developing tools for hiding text, documents, images, audio, video e.t.c files inside an Image.


>> Image Steganography T1

This tool help in hiding text inside an .jpg image. Source code is present in the source/ directory. Please install the exe and enjoy.

About:  This tool convert the text to 8bit ASCII and in it 1 denote even and 0 denote the odd this relation
		are made in the red end of the spectrum. The tool encodes a head of 3 '00000000'and tail of 5 '00000000', this help the software to understand where to start and where to end. Image can be of .JPG or .PNG format, and the text can contain any of the letters and symbols. Text can only be smaller than the (height*width)pixel/8 letters. Any thing greater than this will raise error. The image will be slightly changed and will not be visible to the human eye. Do not alter the Image using any Image Editor or any Image converter as this result in error to decode the message.

Built on Python with module in use: pillow, numpy, os. 
Compiled using the pyinstaller 3.6. 
