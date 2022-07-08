from flask import Flask, render_template
import os
import cv2
from utils import binaryImage

img_path = "./static/images/"
img_name = "index.jpeg"
binary_images_path = img_path+'/binary_images/'

try:
    os.mkdir(binary_images_path)
    print("Binary images file was created ")
except FileExistsError:
    pass
finally:
    print("Binary file was present before creation")

img = cv2.imread(img_path+"/"+img_name)
binary_image = binaryImage(img)
cv2.imwrite(binary_images_path+img_name.split('.')[0]+'_binary.jpeg',binary_image)

app = Flask(__name__)

app.config['IMAGE_FOLDER'] = img_path
app.config['BINARY_IMAGE_FOLDER'] = binary_images_path

@app.route('/')
@app.route('/index')
def show_index():
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'chimp.jpeg')
    # binary_filename = os.path.join(app.config['BINARY_IMAGE'],'chimp_binary_img.jpeg')
    print("IMage folder is",app.config['IMAGE_FOLDER'])
    image_path = os.path.join(app.config['IMAGE_FOLDER'],'index.jpeg') 
    binary_images_path = os.path.join(app.config['BINARY_IMAGE_FOLDER'],'index_binary.jpeg')
    # binary_image = binaryImage(img)
    # print("full filename is",full_filename)
    return render_template("index.html", user_image = image_path,binary_image=binary_images_path)



if __name__=="__main__":
    app.run(debug=True)