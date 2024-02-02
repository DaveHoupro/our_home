'''我的主页'''
import streamlit as st
#from streamlit_drawable_canvas import st_canvas
#from PIL import Image

st.write('背景音乐1')
st.audio("xianghaoyu_calm1.ogg", format="我的网络根据地/ogg")
st.write('背景音乐2')
st.audio("xianghaoyu_calm2.ogg", format="我的网络根据地/ogg")
st.write('背景音乐3')
st.audio("xianghaoyu_calm3.ogg", format="我的网络根据地/ogg")
st.image('xianghaoyu_picture2.png')
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write('事先说明：作者社恐且网站后期为个人使用，不喜勿喷。')
    st.write('=============================')
    st.write('最喜欢的电影：《举起手来》')
    st.write('最喜欢的片段：')
    st.image('xianghaoyu_picture.png')
    st.write('=============================')
    st.write('偶像：')
    st.image('xianghaoyu_picture3.png')
    st.write('=============================')
    st.write('最开心的时候：')
    st.image('xianghaoyu_picture4.png')
    st.write('=============================')
    st.write('最喜欢的音乐风格：我的世界风格')
    st.write('=============================')
    st.write('最喜欢的游戏：你说呢？')
    st.write('=============================')
    st.write('最喜欢的书：《鲁滨逊漂流记》')
    st.write('=============================')
    st.write('最喜欢干的事：做梦，然后写成书')
    st.write('=============================')
    st.write('最喜欢的音乐风格：我的世界风格')
    st.write('=============================')
    
def page_2():
    '''我的图片处理工具'''
    pass

def page_3():
    '''我的智能词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
