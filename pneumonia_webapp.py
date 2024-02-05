import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from util import classify, set_background



# set title
st.title('Pneumonia classification')

# set header
st.header('Please upload a chest X-ray image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('https://github.com/abh1shank/Respiratory-Disease-Classification-using-CNN/blob/main/Pnumonia_model.h5')

# load class names
class_names=['Unhealthy','Healthy']

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))