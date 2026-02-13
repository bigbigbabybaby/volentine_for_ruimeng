import streamlit as st
import time
from PIL import Image

# --- 页面配置 ---
st.set_page_config(
    page_title="To 睿睿 - 情人节",
    page_icon="💖",
    layout="centered"
)

# --- 隐藏默认菜单和页脚，添加自定义CSS ---
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* 整体背景设置 */
    .stApp {
        background-image: linear-gradient(to bottom right, #fff0f5, #ffe4e1);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    /* 标题样式 */
    h1 {
        color: #ff69b4;
        text-align: center;
        text-shadow: 2px 2px 4px #cccccc;
    }
    /* 自定义文字样式 */
    .highlight-text {
        font-size: 20px;
        color: #555555;
        text-align: center;
        margin-bottom: 20px;
    }
    .love-letter {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #ffb6c1;
        font-size: 18px;
        line-height: 1.6;
        color: #333;
    }
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# --- 侧边栏（增加一点神秘感） ---
with st.sidebar:
    st.write("🔒 **专属认证**")
    name_input = st.text_input("请输入你的名字解锁礼物：")
    
# --- 主逻辑 ---
def main():
    # 简单的认证逻辑，输入“刘蕊萌”或者“蕊萌”或者昵称都可以，增加互动感
    if name_input in ["睿睿", "蕊萌", "Ruimeng", "老婆", "宝宝"]:
        show_content()
    elif name_input == "":
        st.title("🔒 这是一个加密的爱意空间")
        st.info("请在左侧侧边栏输入名字解锁哦~")
        st.write("提示：是世界上最可爱的女孩子的名字")
    else:
        st.error("哎呀，名字好像不对，是不是输入了外号？再试一次！")

def show_content():
    # --- 标题区 ---
    st.markdown("<h1>💖 亲爱的睿睿，情人节快乐！ 💖</h1>", unsafe_allow_html=True)
    
    # --- 计数器区（第5个情人节） ---
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric(label="我们一起度过的", value="第 5 个情人节", delta="To Be Continued...")
    
    st.write("---")

    # --- 海绵宝宝区域 ---
    st.markdown("<div class='highlight-text'>✨ 我们还要在一起过下一个节日 ✨</div>", unsafe_allow_html=True)
    
    try:
        # 尝试加载图片，如果没有图片则显示文字替代
        image = Image.open('spongebob.png')
        st.image(image, caption="Love you like SpongeBob loves Patrick", use_column_width=True)
    except FileNotFoundError:
        st.warning("（这里本来有一张合照，但是路径好像没对上，不过不影响我爱你！）")
        st.markdown("🐙 ⭐ 🍍")

    st.write("")
    st.write("")

    # --- 互动按钮 ---
    if st.button("点我接收爱心发射 ❤️"):
        st.balloons() # 第一次点击放气球
        time.sleep(1)
        st.success("biu biu biu~ 爱意已送达！")
        
        # --- 展开情书 ---
        st.write("")
        with st.expander("💌 点击查看给蕊萌的一封信", expanded=True):
            st.markdown("""
            <div class='love-letter'>
            <p>亲爱的蕊萌：</p>
            <p>这是我们一起度过的第 5 个情人节了。时间过得真快，对吧？</p>
            <p>在这个特别的日子里，我本来想写很多代码来证明各种算法，但最后发现，没有任何算法能计算我对你的喜欢。</p>
            <p>你总是奇奇怪怪又可可爱爱，照亮了我的生活。</p>
            <p>如果你是 <code>True</code>，那我永远不会是 <code>False</code>；</p>
            <p>如果你是 <code>while(1)</code>，那我愿做那个永远在循环里陪你的人。</p>
            <p><b>未来不管是第 10 个，还是第 50 个情人节，我都想和你一起过。</b></p>
            <p style='text-align: right;'>—— 爱你的男朋友</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 再次触发爱心雨
            if st.button("再来一次爱心雨？❄️"):
                st.snow() # 这里的雪花可以看作是另一种浪漫氛围

if __name__ == "__main__":
    main()