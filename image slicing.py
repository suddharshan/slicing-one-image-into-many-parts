from PIL import Image 
  
# Opens a image in RGB mode 
im = Image.open(r"C:\Users\suddharshan\Downloads\Cali.png")
  
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 
left=35
right=200
a=7
b=0
top=130
# Setting the points for cropped image
for top in range(130,2080,260):
    for left in range(33,1600,200):
        right = left+201
        bottom = height-157-(a*260)

        # Cropped image of above dimension 
        # (It will not change orginal image) 
        im1 = im.crop((left, top, right, bottom)) 

        # Shows the image in image viewer 
        im1.show()
        im1.save(str(b)+'.jpg')
        b=b+1
    a=a-1