from keras.preprocessing.image import load_img

from keras.preprocessing.image import img_to_array

img = load_img("image.png")

data = img_to_array(img)
print(data)