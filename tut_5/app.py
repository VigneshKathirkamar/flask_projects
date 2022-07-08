from flask import Flask, render_template
import os
import cv2
from utils import binaryImage

img_path = "./static/images/"
img_name = "index.jpeg"
binary_images_path = img_path+'/binary_images/'
blur_images_path = img_path+'/blur_images/'

processed_images_path = [binary_images_path,blur_images_path]

for i in processed_images_path:
    try:
        os.mkdir(i)
        print("Binary images file was created ")
    except FileExistsError:
        pass
    finally:
        print("Binary file was present before creation")

img = cv2.imread(img_path+"/"+img_name)
original_img = img.copy()

image_height, image_width  = original_img.shape[:2]
image_data_type = original_img.dtype

binary_image = binaryImage(img)
cv2.imwrite(binary_images_path+img_name.split('.')[0]+'_binary.jpeg',binary_image)

blur_image = cv2.GaussianBlur(original_img,(3,3),0)
cv2.imwrite(blur_images_path+img_name.split('.')[0]+'_blur.jpeg',blur_image)

app = Flask(__name__)

app.config['IMAGE_FOLDER'] = img_path
app.config['BINARY_IMAGE_FOLDER'] = binary_images_path
app.config['BLUR_IMAGE_FOLDER'] = blur_images_path

@app.route('/')
@app.route('/index')
def show_index():
    image_path = os.path.join(app.config['IMAGE_FOLDER'],'index.jpeg') 
    binary_images_path = os.path.join(app.config['BINARY_IMAGE_FOLDER'],'index_binary.jpeg')
    blur_images_path = os.path.join(app.config['BLUR_IMAGE_FOLDER'],'index_blur.jpeg')
    size = (str(image_height)+'x'+str(image_width))
    img_data_type = image_data_type
    return render_template("index.html", user_image = image_path,binary_image=binary_images_path,blur_image=blur_images_path,size=size
                ,img_data_type = img_data_type)



if __name__=="__main__":
    app.run(debug=True)