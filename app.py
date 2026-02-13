import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- 1. 页面配置：黑色沉浸式 ---
st.set_page_config(
    page_title="To Ruirui",
    page_icon="❤️",
    layout="centered"
)

# --- 2. CSS 样式：黑色背景 + 动态效果 ---
st.markdown("""
    <style>
    /* 全局背景黑色 */
    .stApp {
        background-color: #000000;
        color: #FF69B4;
    }
    
    /* 隐藏不需要的元素 */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 按钮样式 */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF69B4;
        font-size: 16px;
        padding: 10px 24px;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #C71585;
        transform: scale(1.05);
    }

    /* 数学爱心图的容器动画（呼吸效果） */
    .heart-container {
        animation: heartbeat 1.5s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    /* 自定义爱心雨 (替代原本的气球) */
    .heart-rain {
        position: fixed;
        top: -10%;
        font-size: 24px;
        color: #FF1493;
        animation: fall linear forwards;
        z-index: 9999;
    }
    @keyframes fall {
        to { transform: translateY(110vh); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 辅助函数 ---

def draw_math_heart():
    """用数学公式画一个纯粹的粉色爱心"""
    t = np.linspace(0, 2 * np.pi, 1000)
    # 心形公式
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # 创建图表 (黑色背景)
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor('black') # 图表外背景黑
    ax.set_facecolor('black')        # 图表内背景黑
    
    # 画线和填充
    ax.plot(x, y, color='#FF1493', linewidth=3) # 深粉色线条
    ax.fill(x, y, color='#FF69B4', alpha=0.5)   # 浅粉色填充
    ax.axis('off') # 去掉坐标轴
    return fig

def rain_hearts():
    """生成满屏爱心雨 JS特效"""
    st.markdown("""
    <script>
    function createHeart() {
        const heart = document.createElement('div');
        heart.innerHTML = '❤️';
        heart.className = 'heart-rain';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = (Math.random() * 2 + 3) + 's';
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 5000);
    }
    setInterval(createHeart, 300);
    </script>
    """, unsafe_allow_html=True)

# --- 4. 状态管理 ---
if 'step' not in st.session_state:
    st.session_state.step = 0

# --- 5. 主流程 ---

def main():
    # === 阶段 0：密码解锁 ===
    if st.session_state.step == 0:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>🔒 专属空间 Access</h3>", unsafe_allow_html=True)
        password = st.text_input("请输入通关密码（名字）：", type="password")
        
        if password in ["刘蕊萌", "睿睿", "ruirui", "Ruimeng", "宝宝"]:
            st.session_state.step = 1
            st.rerun()

    # === 阶段 1：初次见面 & 飘雪 ===
    elif st.session_state.step == 1:
        st.snow()
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #FF69B4;'>❄️ 睿睿，情人节快乐 ❄️</h1>", unsafe_allow_html=True)
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

    # === 阶段 2：数学公式爱心闪现 ===
    elif st.session_state.step == 2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>正在计算爱的公式...</h3>", unsafe_allow_html=True)
        
        # 显示公式
        st.latex(r"x = 16\sin^3(t)")
        st.latex(r"y = 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t)")
        
        # 画图
        fig = draw_math_heart()
        st.pyplot(fig)
        
        st.markdown("<h4 style='text-align: center; color: #FFB6C1;'>这是专门为你计算的心跳 💓</h4>", unsafe_allow_html=True)
        
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.rerun()

    # === 阶段 3：时光机 & 合照 & 承诺 ===
    elif st.session_state.step == 3:
        # --- 日历动画 ---
        st.markdown("### 📅 我们的故事开始于...")
        date_display = st.empty()
        
        # 倒数动画效果
        dates = ["Listening...", "Loading memories...", "2021-06-06"]
        for d in dates:
            date_display.markdown(f"<h1 style='text-align: center; color: white;'>{d}</h1>", unsafe_allow_html=True)
            time.sleep(0.8)
        
        rain_hearts() # 触发爱心雨（替代气球）
        
        st.markdown(f"<h3 style='text-align: center;'>这是我们要一起过的第 <span style='color:red; font-size:30px'>5</span> 个情人节</h3>", unsafe_allow_html=True)
        time.sleep(1)
        
        # --- 合照 ---
        photo_placeholder = st.empty()
        try:
            photo_placeholder.image("love.png", caption="那时候的我们", use_column_width=True)
            time.sleep(4) 
            photo_placeholder.empty() # 照片消失
        except:
            photo_placeholder.warning("（这里需要一张 love.png 哦）")
            time.sleep(2)
            photo_placeholder.empty()

        # --- 承诺 ---
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>✨ 我们还要过好多个情人节 ✨</h2>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("点我接收满屏爱心 💖"):
            st.session_state.step = 4
            st.rerun()

    # === 阶段 4：大结局 ===
    elif st.session_state.step == 4:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>💖 永远爱你 💖</h1>", unsafe_allow_html=True)
        
        # 持续不断的爱心雨
        rain_hearts()
        
        st.markdown("""
            <div style="text-align: center; color: #FF69B4; font-size: 20px; margin-top: 50px;">
                Happy Valentine's Day, My Love.<br>
                From 2021.06.06 to Forever.
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("再看一遍我们的故事 🔄"):
            st.session_state.step = 0
            st.rerun()

if __name__ == "__main__":
    main()
