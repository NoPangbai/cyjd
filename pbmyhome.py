import streamlit as st
from PIL import Image

page=st.sidebar.radio("次元基地",["好番必追","鬼畜图片","死宅也要学英语","老婆交流区","每日老婆选择器","老婆展示","支持作者"])

def ic(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(width):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(b,g,r)
def p1():
    st.write("陡然喜欢你1.8亿播放,307.6万弹幕,610.8万追番恋爱 / 校园 / 漫画改 / 搞笑 · 2017 · 已完结, 全12话(2024)声优：菅原卓郎：石川界人 高野千鹤：水濑祈 刚田武：前野智昭 上根绫香：小仓唯 赤木正文：小野贤章 梶亮子：佐仓绫音 高濑春彦：熊谷健太郎 神田沙希：三宅晴佳 皆川由纪：花泽香菜 古屋纯：天崎滉平 古屋萤：户松遥 香取慎一：浪川大辅 汤川英树：小野大辅 笹原五月：内田真礼简介：故事讲述了青梅竹马之间、学生会长与不良少女之间、前辈与后辈之间、同学之间等多种不同角色的恋爱群像剧。")
    st.image("陡然喜欢你.jpg")
    st.write("声之形4408.4万播放  ·  146.4万弹幕  ·  290.2万追剧动画 / 爱情 / 剧情 / 漫画改 · 2017 · 2017年09月08日上映(2024)出演演员：入野自由 / 早见沙织 / 松冈茉优 / 悠木碧 / 小野贤章 / 金子有希 / 石川由依 / 潘惠美简介： 西宫硝子（早见沙织 配音）天生患有听觉障碍，需依靠助听器与外界交流，她的口语发音也因此显得格外古怪。初中时，硝子转去了一所新学校，生理缺陷让她成为了班上的“独特”存在，她因此收获了友情，却也遭到了以男生石田将也（入野自由 配音）为首的小团体的欺凌。无论是出于少年无心，还是恶童有意，随着时间的推移，事态逐渐升级，一系列的事件之后，最终演变成为了无法挽回的伤害，硝子也永远地消失在了众人的眼前……")
    st.image("声之形.jpg")
    st.write("中二病也要谈恋爱！校园 / 恋爱 / 搞笑 / 小说改 · 2012 · 已完结, 全13话 · BV1gf4y117WN声优：富樫勇太：福山润 小鸟游六花：内田真礼 丹生谷森夏：赤﨑千夏 五月七日枯茗：浅仓杏美 凸守早苗：上坂堇 勇太の母：天野由梨 富樫樟叶：福原香织 富樫梦叶：设乐麻美 一色诚：保志总一朗简介：富㭴勇太于初中毕业的时候，决定同时为自己举办中二病毕业的仪式。打算顺利度过高中生活的他，在开学日以最后的中二语录完全封锁这段黑历史。可惜天意弄人，勇太遇上了现任中二病患者暨同班同学小鸟游六花，更被对方看出中二病的残余症状。六花于是以此威逼勇太与她“立下契约”。对方的行为举止惹来了不少同学、家人、甚至青梅竹马的注目，使勇太在享受“现充”的生活同时，又充满著难言之隐……")
    st.image("中二病.jpg")
    st.write("总之就是非常可爱2亿播放  ·  293.7万弹幕  ·  595.1万系列追番日常 / 恋爱 / 漫画改 · 2020 · 已完结, 全13话 · BV1pK411N7xH声优：由崎司：鬼头明里 由崎星空：榎木淳弥 有栖川要：芹泽优 有栖川绫：上坂堇 键之寺千岁：小原好美简介：由崎星空对神秘美少女——司一见钟情。面对星空决死的告白，她的回答是“如果你愿意和我结婚，那我就跟你交往”？！充满了星空与司的爱，可爱&高贵的新婚生活开始了！")
    st.image("可爱.jpg")
    st.write("未确认进行式1952.7万播放  ·  14.7万弹幕  ·  124.5万系列追番漫画改 / 萌系 / 搞笑 · 2014 · 已完结, 全12话 · BV1Gk4y1k7Dm声优：夜之森小红：照井春佳 夜之森红绪：松井惠理子 三峰真白：吉田有里 三峰白夜：羽多野涉 桃内真由罗：爱美 鹿岛抚子：佐仓绫音 大野仁子：角元明日香 末续木叶：藤田咲 夜之森茜：渡部优衣 三峰白雪：驹形友梨简介：故事讲述过着平凡生活的少女夜之森小红在其16岁生日时，遇到了自称是其婚约者的少年三峰白夜、以及白夜的妹妹三峰真白，并且要和他们二人开始一同生活。加上不但是妹控还是变态的小红的姐姐夜之森红绪，是一部描写他们的奇妙同居生活的恋爱喜剧。故事讲述过着平凡生活的少女夜之森小红在其16岁生日时，遇到了自称是其婚约者的少年三峰白夜、以及白夜的妹妹三峰真白，并且要和他们二人开始一同生活。加上不但是妹控还是变态的小红的姐姐夜之森红绪，是一部描写他们的奇妙同居生活的恋爱喜剧。")
    st.image("未.jpg")
def p2():
    st.write(":sunglasses:来鬼畜！:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色鬼畜')
            co = st.toggle('对比度鬼畜')
            bw = st.toggle('黑白鬼畜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)
def p3():
    st.write("死宅也要学英语")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split("\n")

    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list=f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input("死宅请问你要学习什么单词？")
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open("check_out_times.txt","w",encoding="utf-8") as f:
            message=""
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+"\n"
            message=message[:-1]
            f.write(message)
            st.write("死宅你查了这个单词的次数是:",times_dict[n])
            if word =="chicken":
                st.code("鸡你太美~~baby~~~鸡你太美~~baby~~~鸡你实在是太美~~baby~~~")
                st.snow()
def p4():
    st.write("有什么自己的老婆拿出来聊一聊啊~(●ˇ∀ˇ●)")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list=f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split("#")
    for i in messages_list:
        if i[1]=="阿短":
            with st.chat_message("🥛"):
                st.write(i[1],":",i[2])
        elif i[1]=="编程猫":
            with st.chat_message("🍭"):
                st.write(i[1],":",i[2])
        elif i[1]=="游客":
            with st.chat_message("🌳"):
                st.write(i[1],":",i[2])
    name=st.selectbox("我是......",["阿短","编程猫","游客"])
    new_message=st.text_input("想要说的话......")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message=""
            for i in messages_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            f.write(message)
def p5():
    cho=st.radio(
        "今天老婆是？",
        ["伊雷娜","十花","西宫硝子","由崎司","绫香"],
    )
    if cho == "伊雷娜":
        st.image("伊雷娜.png")
    elif cho == "十花":
        st.image("十花.jpg")
    elif cho == "西宫硝子":
        st.image("西宫硝子.jpg")
    elif cho == "由崎司":
        st.image("由崎司.jpeg")
    elif cho == "绫香":
        st.image("绫香.png")
    
def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img
def p6():
    a=["1.png","2.jpg","3.jpg","4.jpg","5.jpeg","6.jpg","7.png","7.jpg","陡然喜欢你.jpg","可爱.jpg","绫香.png","声之形.jpg","十花.jpg","未.jpg","西宫硝子.jpg","伊雷娜.png","由崎司.jpeg","中二病.jpg"]
    for i in a:
        st.image(a)

def p7():
    st.image("绫香.png")
    st.write("No_Pangbai")
    go = st.selectbox('我是纳西妲的狗也是一个up', ['github', '我的bilibili'])
    if go == 'github':
        st.link_button('小人不才劳动成果可使用github', 'https://github.com/NoPangbai/-')
    elif go == '我的bilibili':
        st.link_button('B站', 'https://space.bilibili.com/1283914589?spm_id_from=333.1007.0.0')

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

if page=="好番必追":
    p1()
elif page=="鬼畜图片":
    p2()
elif page=="死宅也要学英语":
    p3()
elif page=="老婆交流区":
    p4()
elif page=="每日老婆选择器":
    p5()
elif page=="老婆展示":
    p6()
elif page=="支持作者":
    p7()

