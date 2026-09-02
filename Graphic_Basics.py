from PIL import Image
from PIL import ImageFilter
#for bonus task
from PIL import ImageEnhance

#open file with the original image 
with Image.open('original.jpg') as pic_original:
    print('Image is opne\nSize:', pic_original.size)
    print('format:', pic_original.format)
    print('Type:', pic_original.mode)
    pic_original.show()

    #change the color of original to white and black 
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print('Image is created\nsize:', pic_gray.size)
    print('Format:', pic_gray.format)
    print('Type:', pic_gray.mode) #bw
    pic_gray.show

    #make the image blur 
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()

    #rotate original by 180 degrees
    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save('up.jpg')
    pic_up.show()
