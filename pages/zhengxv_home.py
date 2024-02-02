'''我的主页'''
import streamlit as st


page = st.sidebar.radio('我的首页', ['引语', '网站分享论坛', '点评大师', '在线体验'])

def page_1():
    '''引语'''
    st.audio("zhengxv_背景音乐.mp3",format='audio/mp3',start_time=0)
    st.write("欢迎光临网络中转站！图灵曾说：This is not only a foretaste that is going to come, but also a shadow  of what is going to be.（这不仅仅是未来之事的前兆，也是将来之事的影子。） 现在就让我们一起开启一段网站之旅吧！")
    st.image('zhengxv_出发.jpg')

def page_2():
    '''网站分享论坛'''
    st.write("这里是网络分享论坛。你可以在这里分享你所发现的网址。（注意：本网站禁止发布、传送、传播、储存违反国家法律法规的内容）")
    st.write("-----------------------------------")

def page_3():
    '''点评大师'''
    st.write("欢迎来到点评大师栏目，你可以点评一些网站。（注意：本网站禁止发布内容：(1)违反宪法确定的基本原则的;(2)损害国家荣誉和利益的;(3)散布谣言，扰乱社会秩序，破坏社会稳定的;(4)侵害他人合法权益的;(5)含有法律、行政法规禁止的其他内容的。）")
    st.write("-----------------------------------")

def page_4():
    '''在线体验'''
    st.write("欢迎在线体验网站，如果你要对一些网站进行测试，请使用此页面。（本网站不会储存你的信息）")
    st.write("-----------------------------------")

if page == '引语':
    page_1()
elif page == '网站分享论坛':
    page_2()
elif page == '点评大师':
    page_3()
elif page == '在线体验':
    page_4()

#python -m streamlit run zhengxv_home.py