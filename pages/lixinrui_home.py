'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.audio("lixinrui_Summer.mp3",format='audio/mp3',start_time=0)
    st.image("lixinrui_bag.png")
    st.write('我最喜爱的音乐是：')
    st.write(':orange[海阔天空——Beyond]')
    st.write('我最喜爱的书籍是：')
    st.write(':blue[俗世奇人——冯骥才]')
    st.write('我最喜爱的游戏是：')
    st.write(':red[FIFA23]')
    st.image("lixinrui_FIFA23.png")
    
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