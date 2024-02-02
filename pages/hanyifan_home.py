'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['主界面', '常用网址', '音乐播放区', '施工中'])

def page_1():
    '''主界面'''
    # st.image('BingWallpaper.jpg')
    st.write('欢迎访问本网站！')
    st.write('点击左侧的选项以切换页面')
    # st.audio('IslandWind,PIKASONIC - Forever.mp3', format='audio/mp3', start_time=0)

def page_2():
    '''常用网址'''
    st.write('这里是一些常用的网址：')
    st.write('百度：https://www.baidu.com/')
    st.write('必应：https://cn.bing.com/')
    st.write('编程猫社区：https://shequ.codemao.cn/')
    st.write('网易云音乐：https://music.163.com/')

def page_3():
    '''音乐播放区'''
    st.write('这里是作者推荐的音乐：')
    st.write('（随便放了点歌进去，下载歌曲要vip，作者开不起，只能下载一些😭😭😭）')
    st.write('PS：歌曲可以同时播放，但是不建议（废话）')
    st.write('')
    st.write('IslandWind,PIKASONIC - Forever.mp3')
    st.audio('hanyifan_IslandWind,PIKASONIC - Forever.mp3', format='audio/mp3', start_time=0)
    st.write('Richard Clayderman - Les premiers sourires de Vanessa.mp3')
    st.audio('hanyifan_Richard Clayderman - Les premiers sourires de Vanessa.mp3', format='audio/mp3', start_time=0)
    st.write('陈致逸,HOYO-MiX - 璃月 Liyue.mp3')
    st.audio('hanyifan_陈致逸,HOYO-MiX - 璃月 Liyue.mp3', format='audio/mp3', start_time=0)
    st.write('のみこ - Bad Apple!!.mp3')
    st.audio('hanyifan_のみこ - Bad Apple!!.mp3', format='audio/mp3', start_time=0)
    st.write('花澤香菜 - 恋愛サーキュレーション.mp3')
    st.audio('hanyifan_花澤香菜 - 恋愛サーキュレーション.mp3', format='audio/mp3', start_time=0)
def page_4():
    '''施工中'''
    st.write('没做好（）')

if page == '主界面':
    page_1()
elif page == '常用网址':
    page_2()
elif page == '音乐播放区':
    page_3()
elif page == '施工中':
    page_4()

# python -m streamlit run hanyifan_home.py