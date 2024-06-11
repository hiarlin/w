import streamlit as st
st.title("想吃烤鱼！")
st.header("去哪儿吃啊")
st.subheader("烤鱼就吃半天妖")
st.text("欢迎光临")

st.markdown("这是招牌: \n \
            ![](https://ts1.cn.mm.bing.net/th/id/R-C.a423ca6213189973b0966d852cc3f330?rik=Gy3XAoFWh30zSA&riu=http%3a%2f%2fpic.ntimg.cn%2ffile%2f20190307%2f3529431_083249815088_2.jpg&ehk=QMW24cYbXnTCQmSgf7Me42F49N57q2z3G3sEVdUQ0o0%3d&risl=&pid=ImgRaw&r=0)")

if st.checkbox("Show/Hide"):
    st.text("你发现了美食")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['Hot',
                'Sour',
                'Salty'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    
