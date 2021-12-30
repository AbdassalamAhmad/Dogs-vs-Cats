import numpy as np
import streamlit as st
from PIL import Image# to read & resize the image 
#import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.xception import preprocess_input



#loading the model
model = keras.models.load_model("xception_v9_03_0.965.h5")


def main():
    st.title("Dogs VS Cats")
    uploaded_file = st.file_uploader("Upload a picture to predict it is a cat or a dog", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        st.title("Here is the image you've uploded")
        image = Image.open(uploaded_file)
        st.image(image)
        #if st.button("Predict Class"):
        result=predict_class(image)
        st.write(result)
        
    

def predict_class(image):
    #preprocessing the test picture
    #image sizing
    test_image = image.resize((150,150))
    image_array = np.asarray(test_image)
    X = np.array([image_array])#because the next function expects a list.
    X = preprocess_input(X)

    #predicting
    pred = model.predict(X)
    #turning the numbers into text
    pred=pred.tolist()
    result = pred[0]
    result=result[0]
    if result<=0.5:
        picture = 'cat'
        result = "your picture contains a {} ".format(picture)
    else: 
        picture = 'dog'
        result = "your picture contains a {} ".format(picture)    
    return (result)

if __name__=='__main__':
    main()