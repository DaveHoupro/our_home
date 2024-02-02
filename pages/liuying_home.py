'''我的主页'''
import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# from PIL import Image

# st(background_image = Image.open("宇宙.gif"))
# python -m streamlit run liuying_home.py

page = st.sidebar.radio('我的首页', ['我的音乐推荐','我的动画推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    '''我的音乐推荐'''
    st.write("半山腰-焦亮")
    st.audio("liuying_半山腰.mp3", format='audio/mp3', start_time=0)
    st.write("刀剑如梦-成毅、曾舜晞、肖顺尧")
    st.audio("liuying_刀剑如梦.mp3", format='audio/mp3', start_time=0)
    st.write("山外-成毅、曾舜晞、肖顺尧")
    st.audio("liuying_山外.mp3", format='audio/mp3', start_time=0)
    st.write("天下-成毅、曾舜晞、肖顺尧")
    st.audio("liuying_天下.mp3", format='audio/mp3', start_time=0)
    # pass

def page_2():
    '''我的动画推荐'''
    st.write("烦人的村民真的很好看，每个人都守着自己心中的正义，溺尸王、him都超帅！！！")
    st.image('liuying_烦村1.png')
    st.image('liuying_烦村2.png')
    st.image('liuying_烦村3.png')
    st.write("火柴人也很好看，作者是哔站上的火柴人alanbaker，火柴人形象生动活泼，又可爱又强大。")
    st.image('liuying_火柴人1.png')
    st.image('liuying_火柴人2.png')
    st.image('liuying_火柴人3.png')

def page_3():
    '''我的图片处理工具'''
    pass

def page_4():
    '''我的智能词典'''
    pass

def page_5():
    '''我的留言区'''
    pass

if page == '我的音乐推荐':
    page_1()
elif page == '我的动画推荐':
    page_2()
elif page == '我的图片处理工具':
    page_3()
elif page == '我的智能词典':
    page_4()
elif page == '我的留言区':
    page_5()
