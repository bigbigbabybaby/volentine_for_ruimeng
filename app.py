import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="To Ruirui",
    page_icon="❤️",
    layout="centered"
)

# --- 2. CSS 样式 (核心特效) ---
# 注意：这里定义了动画的关键帧，但具体的元素我们稍后用 Python 动态生成注入
st.markdown("""
    <style>
    /* 全局背景黑色 */
    .stApp {
        background-color: #000000;
        color: #FF69B4;
    }
    
    /* 隐藏顶部红线和脚部 */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 按钮样式增强 */
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
        z-index: 10000; /* 保证按钮在最上层，不被特效遮挡 */
    }
    .stButton>button:hover {
        background-color: #C71585;
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(255, 20, 147, 1.0);
    }

    /* 定义漂浮物的基础样式 */
    .floater {
        position: fixed;
        top: -10vh;
        z-index: 9999; /* 保证在最顶层 */
        pointer-events: none; /* 让鼠标可以穿透特效点击按钮 */
        animation: fall linear forwards;
    }

    @keyframes fall {
        to { transform: translateY(120vh); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 辅助函数 (用 Python 生成 HTML 注入) ---

def inject_snow():
    """直接注入 HTML 雪花，确保全屏可见"""
    snow_html = ""
    # 生成 50 个雪花
    for _ in range(50):
        left = random.randint(0, 100)
        duration = random.uniform(3, 8) # 飘落时间 3-8秒
        delay = random.uniform(0, 5)    # 随机延迟
        size = random.uniform(4, 8)     # 大小
        opacity = random.uniform(0.4, 0.9)
        
        # 这是一个发光的小圆点
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
    
    # 注入到页面
    st.markdown(snow_html, unsafe_allow_html=True)

def inject_heart_rain():
    """直接注入 HTML 爱心雨"""
    rain_html = ""
    emojis = ['❤️', '💖', '💗', '💓', '💞']
    # 生成 60 个爱心
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
    # 扩散效果
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
# 用来记录动画是否已播完，防止刷新重播
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
        st.markdown("<h4 style='text-align: center; color: #FFB6C1;'>用代码为你凝聚的粒子爱心 💓</h4>", unsafe_allow_html=True)
        
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.session_state.animation_done = False # 重置动画状态
            st.rerun()

    # === 阶段 3：回忆杀 (彻底修复跳闪问题) ===
    elif st.session_state.step == 3:
        
        placeholder = st.empty()
        
        # 只有在“动画未完成”时才播放动画
        if not st.session_state.animation_done:
            with placeholder.container():
                # 倒计时
                dates = ["Listening...", "Loading...", "2021-06-06"]
                for d in dates:
                    st.markdown(f"<h1 style='text-align: center; color: white; margin-top: 50px;'>{d}</h1>", unsafe_allow_html=True)
                    time.sleep(0.8)
                
                # 第一波爱心雨
                inject_heart_rain()
                time.sleep(0.5)
                
                # 照片
                try:
                    st.image("love.png", caption="那时候的我们", use_column_width=True)
                    time.sleep(3)
                except:
                    st.warning("（这里需要 love.png）")
                    time.sleep(2)
            
            # 动画播完，设置标志位，并刷新
            st.session_state.animation_done = True
            st.rerun()
        
        else:
            # === 稳定状态（动画播完后停留在这里） ===
            # 这里是刷新后直接显示的内容，没有 sleep，所以点击按钮不会跳
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>这是我们要一起过的第 <span style='color:red; font-size:30px'>5</span> 个情人节</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>✨ 我们还要过好多个情人节 ✨</h2>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            # 点击按钮去下一页
            if st.button("点我接收满屏爱心 💖"):
                st.session_state.step = 4
                st.rerun()

    # === 阶段 4：大结局 (满屏爱心) ===
    elif st.session_state.step == 4:
        # 这里每次刷新都会注入新的爱心雨
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
