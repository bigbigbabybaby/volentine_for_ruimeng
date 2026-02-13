import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import os

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="To Ruirui",
    page_icon="❤️",
    layout="centered"
)

# --- 2. CSS 样式 ---
st.markdown("""
    <style>
    /* 全局背景黑色 */
    .stApp {
        background-color: #000000;
        color: #FF69B4;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 按钮样式 */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF69B4;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 28px;
        transition: all 0.3s;
        width: 100%;
        box-shadow: 0 0 15px rgba(255, 20, 147, 0.6);
        position: relative;
        z-index: 10000;
    }
    .stButton>button:hover {
        background-color: #C71585;
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(255, 20, 147, 1.0);
    }

    /* 漂浮物样式 */
    .floater {
        position: fixed;
        top: -10vh;
        z-index: 9999;
        pointer-events: none;
        animation: fall linear forwards;
    }

    @keyframes fall {
        to { transform: translateY(120vh); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 辅助函数 ---

def find_love_image():
    """智能查找图片，不区分大小写和格式"""
    # 可能的文件名列表
    possible_names = [
        "love.png", "love.PNG", 
        "love.jpg", "love.JPG", 
        "love.jpeg", "love.JPEG",
        "Love.png", "Love.jpg"
    ]
    
    for name in possible_names:
        if os.path.exists(name):
            return name
    return None

def inject_snow():
    """注入 HTML 雪花"""
    snow_html = ""
    for _ in range(50):
        left = random.randint(0, 100)
        duration = random.uniform(3, 8)
        delay = random.uniform(0, 5)
        size = random.uniform(4, 8)
        opacity = random.uniform(0.4, 0.9)
        
        style = f"""
            left: {left}vw;
            width: {size}px;
            height: {size}px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 0 5px white;
            opacity: {opacity};
            animation-duration: {duration}s;
            animation-delay: {delay}s;
        """
        snow_html += f"<div class='floater' style='{style}'></div>"
    st.markdown(snow_html, unsafe_allow_html=True)

def inject_heart_rain():
    """注入 HTML 爱心雨"""
    rain_html = ""
    emojis = ['❤️', '💖', '💗', '💓', '💞']
    for _ in range(60):
        left = random.randint(0, 100)
        duration = random.uniform(2, 5)
        delay = random.uniform(0, 2)
        size = random.uniform(20, 40)
        emoji = random.choice(emojis)
        
        style = f"""
            left: {left}vw;
            font-size: {size}px;
            animation-duration: {duration}s;
            animation-delay: {delay}s;
        """
        rain_html += f"<div class='floater' style='{style}'>{emoji}</div>"
    st.markdown(rain_html, unsafe_allow_html=True)

def draw_particle_heart():
    """Matplotlib 粒子爱心"""
    t = np.random.uniform(0, 2 * np.pi, 8000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    x += np.random.normal(0, 0.4, 8000)
    y += np.random.normal(0, 0.4, 8000)
    
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.scatter(x, y, s=2, c='#FF1493', alpha=0.6, edgecolors='none')
    ax.axis('off')
    return fig

# --- 4. 状态管理 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'animation_done' not in st.session_state:
    st.session_state.animation_done = False

# --- 5. 主程序 ---
def main():
    
    # 全局特效：除了密码页，其他页都下雪
    if st.session_state.step > 0:
        inject_snow()

    # === 阶段 0：密码 ===
    if st.session_state.step == 0:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>🔒 专属空间 Access</h3>", unsafe_allow_html=True)
        password = st.text_input("请输入通关密码（名字）：", type="password")
        if password in ["刘蕊萌", "睿睿", "ruirui", "Ruimeng", "宝宝"]:
            st.session_state.step = 1
            st.rerun()

    # === 阶段 1：初次见面 ===
    elif st.session_state.step == 1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #FF69B4; text-align: center;'>❄️ 睿睿，情人节快乐 ❄️</h1>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>是否愿意和大宝一起过情人节？</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("是，我愿意 💖"):
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("否 💔"):
                st.error("⚠️ 大宝不允许！禁止选这个！只能选愿意！")

    # === 阶段 2：粒子爱心 ===
    elif st.session_state.step == 2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.pyplot(draw_particle_heart())
        st.markdown("<h4 style='text-align: center; color: #FFB6C1;'>爱你呦 💓</h4>", unsafe_allow_html=True)
        
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.session_state.animation_done = False 
            st.rerun()

    # === 阶段 3：回忆杀 ===
    elif st.session_state.step == 3:
        placeholder = st.empty()
        
        # 只有在“动画未完成”时才播放
        if not st.session_state.animation_done:
            with placeholder.container():
                # 倒计时
                dates = ["来波回忆杀", "恋爱开始", "2021-06-06"]
                for d in dates:
                    st.markdown(f"<h1 style='text-align: center; color: white; margin-top: 50px;'>{d}</h1>", unsafe_allow_html=True)
                    time.sleep(1.2)
                
                inject_heart_rain()
                time.sleep(1)
                
                # --- 智能寻找并显示图片 ---
                img_path = find_love_image()
                if img_path:
                    st.image(img_path, caption="那时候的我们", use_column_width=True)
                    time.sleep(5)
                else:
                    # 如果真的找不到，显示错误提示方便调试
                    st.error("⚠️ 没找到图片！请确认已上传 love.png 或 love.jpg")
                    st.write(f"当前目录下的文件: {os.listdir('.')}") # 帮你查错
                    time.sleep(3)
            
            st.session_state.animation_done = True
            st.rerun()
        
        else:
            # 动画播完后的稳定界面
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>这是我们要一起过的第 <span style='color:red; font-size:30px'>5</span> 个情人节</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>✨ 我们还要过好多个情人节 ✨</h2>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("点我接收满屏爱心 💖"):
                st.session_state.step = 4
                st.rerun()

    # === 阶段 4：大结局 ===
    elif st.session_state.step == 4:
        inject_heart_rain()
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>💖 永远爱你 💖</h1>", unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; color: #FF69B4; font-size: 20px; margin-top: 50px;">
                Happy Valentine's Day, Ruirui.<br>
                From 2021.06.06 to Forever.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("再看一遍我们的故事 🔄"):
            st.session_state.step = 0
            st.rerun()

if __name__ == "__main__":
    main()


