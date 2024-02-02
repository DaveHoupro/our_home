'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['我的歌曲推荐', '我的动漫推荐', '我的小说推荐', '我的游戏推荐'])

def page_1():
    '''我的歌曲推荐'''
    st.write('不遗憾')
    st.write('喜剧之王')
    st.write('江南')
    st.write('美人鱼')
    st.write('最长的电影')
    st.write('不该')
    st.write('圣诞星')
    st.write('Love Store')
def page_2():
    '''我的动漫推荐'''
    st.write('咒术回战')
    st.write('东京喰种')
    st.write('火影忍者')
    st.write('鬼灭之刃')
def page_3():
    '''我的小说推荐'''
    st.write('天堂旅行团')
    st.write('幻城')
    st.write('云边有个小卖部')
    st.write('明朝那些事儿')
    st.write('撒野')
def page_4():
    '''我的游戏推荐'''
    st.write('Undertale')
    st.image('qiuqifan_UT.PNG')
    st.write('Celeste')
    st.image('qiuqifan_蔚蓝.PNG')
    st.write('Hollow knight')
    st.image('qiuqifan_空洞.PNG')
    st.write('赛博朋克 2077')
    st.image('qiuqifan_2077.PNG')
    st.write('Terraria')
    st.image('qiuqifan_泰拉.PNG')
if page == '我的歌曲推荐':
    page_1()
elif page == '我的动漫推荐':
    page_2()
elif page == '我的小说推荐':
    page_3()
elif page == '我的游戏推荐':
    page_4()