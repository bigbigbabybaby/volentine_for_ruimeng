import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import streamlit.components.v1 as components

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="To Ruirui",
    page_icon="❤️",
    layout="centered"
)

# --- 2. CSS 样式 (定义雪花和爱心雨) ---
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
        box-shadow: 0 0 10px rgba(255, 20, 147, 0.5);
    }
    .stButton>button:hover {
        background-color: #C71585;
        transform: scale(1.05);
    }

    /* 粒子雪花动画 */
    .snowflake {
        position: fixed;
        top: -10px;
        background: white;
        border-radius: 50%;
        opacity: 0.8;
        pointer-events: none;
        z-index: 9998;
        box-shadow: 0 0 5px white;
        animation: fall linear forwards;
    }

    /* 爱心雨动画 */
    .heart-rain {
        position: fixed;
        top: -10vh;
        font-size: 24px;
        z-index: 9999;
        animation: fall linear forwards;
    }

    @keyframes fall {
        to { transform: translateY(110vh); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 核心功能函数 ---

def draw_particle_heart():
    """用 Matplotlib 画一个稳定的粒子爱心 (效果等同于之前的粒子图)"""
    # 生成 5000 个随机点
    t = np.random.uniform(0, 2 * np.pi, 5000)
    # 心形公式
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # 加入随机抖动，制造蓬松感
    x += np.random.normal(0, 0.5, 5000)
    y += np.random.normal(0, 0.5, 5000)
    
    # 绘图
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor('black') # 背景黑
    ax.set_facecolor('black')
    
    # 绘制散点 (s=大小, alpha=透明度)
    ax.scatter(x, y, s=3, c='#FF1493', alpha=0.6, edgecolors='none')
    ax.axis('off')
    return fig

def create_snow():
    """生成雪花 JS"""
    # 简单的 JS 生成 div
    js = """
    <script>
    function createSnow() {
        const el = document.createElement('div');
        el.className = 'snowflake';
        const size = Math.random() * 3 + 2;
        el.style.width = size + 'px';
        el.style.height = size + 'px';
        el.style.left = Math.random() * 100 + 'vw';
        el.style.animationDuration = (Math.random() * 3 + 2) + 's';
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 5000);
    }
    setInterval(createSnow, 100);
    </script>
    """
    components.html(js, height=0)

def create_rain():
    """生成爱心雨 JS"""
    js = """
    <script>
    function createRain() {
        const el = document.createElement('div');
        el.className = 'heart-rain';
        el.innerHTML = '❤️';
        el.style.left = Math.random() * 100 + 'vw';
        el.style.animationDuration = (Math.random() * 2 + 2) + 's';
        el.style.fontSize = (Math.random() * 20 + 15) + 'px';
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 4000);
    }
    // 密集生成
    const interval = setInterval(createRain, 50);
    // 3秒后停止生成，避免浏览器卡顿
    setTimeout(() => clearInterval(interval), 3000);
    </script>
    """
    components.html(js, height=0)

# --- 4. 状态管理 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'animation_played' not in st.session_state:
    st.session_state.animation_played = False

# --- 5. 主流程 ---

def main():
    
    # 只要不是第一页，就一直下雪
    if st.session_state.step > 0:
        create_snow()

    # === 阶段 0：密码 ===
    if st.session_state.step == 0:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>🔒 专属空间 Access</h3>", unsafe_allow_html=True)
        password = st.text_input("请输入通关密码（名字）：", type="password")
        
        if password in ["刘蕊萌", "睿睿", "ruirui", "Ruimeng", "宝宝"]:
            st.session_state.step = 1
            st.rerun()

    # === 阶段 1：问答 ===
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

    # === 阶段 2：粒子爱心 (最稳的 Matplotlib 版) ===
    elif st.session_state.step == 2:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 直接显示图表，绝对不会加载失败
        st.pyplot(draw_particle_heart())
        
        st.markdown("<h4 style='text-align: center; color: #FFB6C1;'>用代码为你凝聚的粒子爱心 💓</h4>", unsafe_allow_html=True)
        
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.rerun()

    # === 阶段 3：回忆杀 (逻辑修复版) ===
    elif st.session_state.step == 3:
        
        # 容器：用来放倒计时和照片
        placeholder = st.empty()
        
        # 如果动画没播过，就播一次
        if not st.session_state.animation_played:
            with placeholder.container():
                # 倒计时
                dates = ["Listening...", "Loading...", "2021-06-06"]
                for d in dates:
                    st.markdown(f"<h1 style='text-align: center; color: white; margin-top: 50px;'>{d}</h1>", unsafe_allow_html=True)
                    time.sleep(0.8)
                
                # 触发一次爱心雨
                create_rain()
                
                # 显示照片
                try:
                    st.image("love.png", caption="那时候的我们", use_column_width=True)
                    time.sleep(3)
                except:
                    st.warning("（这里需要 love.png）")
                    time.sleep(2)
            
            # 播完清空
            placeholder.empty()
            st.session_state.animation_played = True
            st.rerun() # 强制刷新，进入下面那个状态

        # 动画播完后，固定显示这一段
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>这是我们要一起过的第 <span style='color:red; font-size:30px'>5</span> 个情人节</h3>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>✨ 我们还要过好多个情人节 ✨</h2>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 这个按钮现在绝对不会跳回去了
        if st.button("点我接收满屏爱心 💖"):
            st.session_state.step = 4
            st.rerun()

    # === 阶段 4：结局 ===
    elif st.session_state.step == 4:
        # 触发爱心雨
        create_rain()
        
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
            st.session_state.animation_played = False
            st.rerun()

if __name__ == "__main__":
    main()
