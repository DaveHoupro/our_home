'''我的主页'''
import streamlit as st
#from streamlit_drawable_canvas import st_canvas
#from PIL import Image

#st(background_image = Image.open("宇宙.gif"))

page = st.sidebar.radio('我的首页', ['王者荣耀', '和平精英', '音游专区', '其它游戏'])

def page_1():
    '''王者荣耀'''
    st.write('这里是王者荣耀专区，发表你的神操作吧')

def page_2():
    '''和平精英'''
    st.write('这里是和平精英专区，发表你的神操作吧')

def page_3():
    '''音游'''
    st.write('这里是音游专区，发表你的神操作吧')

def page_4():
    '''其它游戏'''
    st.write('这里是其它专区，发表你的神操作吧')
    st.write('注意：发表格式为：#游戏名 内容')
if page == '王者荣耀':
    page_1()
elif page == '和平精英':
    page_2()
elif page == '音游专区':
    page_3()
elif page == '其它游戏':
    page_4()
