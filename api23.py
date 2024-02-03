import streamlit as st
import cv2
import numpy as np
from PIL import Image
from streamlit_javascript import st_javascript
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
import cv2
import time
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from PIL import Image, ImageOps
import numpy as np





class_name = ['Bangus', 'Big Head Carp', 'Black Spotted Barb', 'Catfish', 'Climbing Perch', 'Fourfinger Threadfin',
        'Freshwater Eel', 'Glass Perchlet', 'Goby', 'Gold Fish', 'Gourami', 'Grass Carp', 'Green Spotted Puffer',
        'Indian Carp', 'Indo-Pacific Tarpon', 'Jaguar Gapote', 'Janitor Fish', 'Knifefish', 'Long-Snouted Pipefish',
        'Mosquito Fish', 'Mudfish', 'Mullet', 'Pangasius', 'Perch', 'Scat Fish', 'Silver Barb', 'Silver Carp',
        'Silver Perch', 'Snakehead', 'Tenpounder', 'Tilapia']

model = load_model('FishModelClassifier_V6.h5')
new_model = load_model('models\\imageclassifier3.h5')
def isfish(img):
    resize = tf.image.resize(img, (256,256))
    yhat = new_model.predict(np.expand_dims(resize/255, 0))
    return yhat

mydic={}

def predict(path):
    img=load_img(path,target_size=(224,224,3))#
    img=img_to_array(img)
    img=img/255 
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    x = list(np.argsort(answer[0])[::-1][:5])
    ma=0.0
    for i in x:
        print("{className}: {predVal:.2f}%".format(className=class_name[i], predVal=float(answer[0][i])*100))
        mydic[class_name[i]]=float(answer[0][i])*100
        predVal=float(answer[0][i])*100
        ma=max(ma,predVal)
    y_class=answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = class_name[y]
    # st.write('Accuracy Percentage')
    # latest_iteration = st.empty()
    # bar = st.progress(0)
    # num =int(ma)
    # for i in range(num):
    #     latest_iteration.text(f'{num - i} seconds left')
    #     bar.progress((100//num)*i)
    #     time.sleep(1)
    return res

new_title = '<p style="font-family:sans-serif; color:Blue; font-size: 36px;">List of Fish</p>'

# link='check out this [link](https://retailscope.africa/)'
# st.markdown(link,unsafe_allow_html=True)
var='https://en.wikipedia.org//wiki/'
side=st.sidebar.markdown(new_title, unsafe_allow_html=True)
#side=st.sidebar.markdown("List of Fish :dolphin:")
for i in class_name:
    st.sidebar.markdown(i)
def predict_species(image_data):
    # Preprocess the image
    # img = image.load_img(image_data, target_size=(150, 150))
    # img = image.img_to_array(img)
    # img = np.expand_dims(img, axis=0)
    # #img = preprocess_input(img)

    # # Make predictions
    # predictions = model.predict(img)
    image = ImageOps.fit(image_data, (224,224), Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img=img/255
    #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
    img_reshape = img[np.newaxis,...]
    
    prediction = model.predict(img_reshape)
    print(prediction)
    return prediction

# Streamlit app
st.title('Fish Species Detection :fish:')
#progress_color = st.color_picker("Choose a color", "#00ff00")
col1, col2, col3 = st.columns([3,2,1])



with col3:
    progress_color = "#EA1A55"
    progress_bar_style = f"""
    <style>
        .stProgress > div > div > div {{
            background-color: {progress_color} !important;
        }}
    </style>
"""
    st.markdown(progress_bar_style, unsafe_allow_html=True)
def fun():
    

    for i in mydic:
        st.write("{className}   :fish:  {predVal:.2f}%".format(className=i,predVal=mydic[i]))
        print(mydic[i])
        progress_bar = st.progress(int(mydic[i]))

option = st.radio("Choose an option:", ('Upload Image', 'Capture Image'))

if option == 'Upload Image':
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        yhat=isfish(image)
        if yhat < 0.5:
            re = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">This is a fish and belongs to our classes</p>' 
            st.write(re,unsafe_allow_html=True)
            st.balloons()
        
        
            if st.button('Detect'):
                # img = image.load_img(uploaded_file, target_size=(150, 150))
                # img = image.img_to_array(img)
                # img = np.expand_dims(img, axis=0)
                #img = preprocess_input(img)

                # Make predictions
                #predictions = model.predict(img)
                predictions = predict(uploaded_file)
                #st.write(predictions[0])
                progress_text = "Operation in progress. Please wait."
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                per=predictions[0]
                print(per)
                re1 = '<p style="font-family:sans-serif; color:Green; font-size: 24px;">The predicted class of fish :</p>' 
                st.write(re1,unsafe_allow_html=True)
                
                #st.write(predictions+':fish:')
                fun()
                
                
                #st.write(f"Predicted class: {labels[predictions.argmax()]}")
        else:
            import webbrowser
            url = 'https://6ff224aadcd3f394e2.gradio.live'
            st.snow()
            re2 = '<p style="font-family:sans-serif; color:Red; font-size: 30px;">Sorry! This image does not belong to our class :</p>'
            st.write(re2,unsafe_allow_html=True)
            
            time.sleep(1)
            progress_text = "We are taking to you another model. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            
            #webbrowser.open_new_tab(url)

            
                
            
elif option == 'Capture Image':
    st.write("Click the 'Capture Image' button to take a picture with your camera.")
    capture_button = st.button('Capture Image')
    
    if capture_button:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                st.image(frame, channels="BGR", caption='Captured Image', use_column_width=True)
                st.write("")
                img=cv2.imwrite("captured_image.jpg", frame)
                print("1")
                
                
                import webbrowser
                url = 'https://6ff224aadcd3f394e2.gradio.live'
                st.snow()
                st.info("Your image don't belongs to any of our classes :pensive:")
                time.sleep(1)
                progress_text = "We are taking to you another model. Please wait."
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                
                #webbrowser.open_new_tab(url)

                    # print(2)
                    # print(predict_species(img))
                    # predictions = predict(img)
                    # print(predictions)
                    # print(3)
                    # progress_text = "Operation in progress. Please wait."
                    # my_bar = st.progress(0, text=progress_text)
                    # print(4)
                

                    
                    #st.write(':dolphin:',predictions)
                    #st.write(f"Predicted class: {predictions.argmax()}")
            cap.release()



#st.markdown(java)

