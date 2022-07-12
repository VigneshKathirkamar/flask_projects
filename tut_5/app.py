from flask import Flask, render_template
import os
import cv2
from utils import binaryImage,colorHistogram

img_path = "./static/images/"
img_name = "index.jpeg"
binary_images_path = img_path+'/binary_images/'
blur_images_path = img_path+'/blur_images/'
histogram_path = img_path+'/historgram/'
blur_histogram_path = img_path+'/blur_histogram/'

processed_images_path = [binary_images_path,blur_images_path,histogram_path,blur_histogram_path]

for i in processed_images_path:
    try:
        os.mkdir(i)
        print("Binary images file was created ")
    except FileExistsError:
        pass
    finally:
        print("Binary file was present before creation")

img = cv2.imread(img_path+img_name)
original_img = img.copy()

image_height, image_width  = original_img.shape[:2]
image_data_type = original_img.dtype

binary_image = binaryImage(img)
cv2.imwrite(binary_images_path+img_name.split('.')[0]+'_binary.jpeg',binary_image)

blur_image = cv2.GaussianBlur(original_img,(7,7),0)
cv2.imwrite(blur_images_path+img_name.split('.')[0]+'_blur.jpeg',blur_image)

histogram = colorHistogram(original_img,histogram_path)
blur_histogram = colorHistogram(blur_image,blur_histogram_path)

app = Flask(__name__)

app.config['IMAGE_FOLDER'] = img_path
app.config['BINARY_IMAGE_FOLDER'] = binary_images_path
app.config['BLUR_IMAGE_FOLDER'] = blur_images_path
app.config['HISTOGRAM_FOLDER'] = histogram_path
app.config['BLUR_HISTOGRAM_FOLDER'] = blur_histogram_path

@app.route('/')
@app.route('/index')
def show_index():
    image_path = os.path.join(app.config['IMAGE_FOLDER'],'index.jpeg') 
    binary_images_path = os.path.join(app.config['BINARY_IMAGE_FOLDER'],'index_binary.jpeg')
    blur_images_path = os.path.join(app.config['BLUR_IMAGE_FOLDER'],'index_blur.jpeg')
    histogram_path = os.path.join(app.config['HISTOGRAM_FOLDER'],'histogram.png')
    blur_histogram_path = os.path.join(app.config['BLUR_HISTOGRAM_FOLDER'],'histogram.png')
    size = (str(image_height)+'x'+str(image_width))
    img_data_type = image_data_type
    return render_template("index.html", user_image = image_path,binary_image=binary_images_path,blur_image=blur_images_path,size=size
                ,img_data_type = img_data_type,histogram = histogram_path,blur_histogram=blur_histogram_path)



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)