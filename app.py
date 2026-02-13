import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import time
import streamlit.components.v1 as components

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
    .stDeployButton {display:none;} /* 隐藏部署按钮 */
    
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

    /* Altair 图表背景透明 */
    #altair-viz-1 canvas {
        background-color: transparent !important;
    }
    
    </style>
""", unsafe_allow_html=True)

# --- 3. 辅助函数 ---

def generate_particle_heart(n_points=3000):
    """生成组成爱心的粒子数据"""
    t = np.linspace(0, 2 * np.pi, n_points)
    # 心形公式
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # 添加一些随机噪点，制造“粒子”感
    x += np.random.normal(0, 0.3, n_points)
    y += np.random.normal(0, 0.3, n_points)
    
    return pd.DataFrame({'x': x, 'y': y})

def trigger_heart_rain():
    """触发满屏 Emoji 爱心雨的 JS 特效"""
    # 使用 components.html 确保脚本被执行
    js_code = """
    <script>
    function createHeartRain() {
        const container = document.createElement('div');
        container.style.position = 'fixed';
        container.style.top = '0';
        container.style.left = '0';
        container.style.width = '100vw';
        container.style.height = '100vh';
        container.style.pointerEvents = 'none';
        container.style.zIndex = '9999';
        document.body.appendChild(container);

        const emojis = ['❤️', '💖', '💗', '💓', '💞'];

        for (let i = 0; i < 150; i++) { // 生成150个爱心
            const heart = document.createElement('div');
            heart.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            heart.style.position = 'absolute';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.top = -50 + 'px';
            heart.style.fontSize = (Math.random() * 25 + 15) + 'px';
            heart.style.opacity = Math.random();
            // 随机下落动画
            heart.animate([
                { transform: 'translateY(0px)' },
                { transform: 'translateY(110vh)' }
            ], {
                duration: Math.random() * 3000 + 2000, // 2-5秒
                easing: 'linear',
                iterations: 1
            });
            
            container.appendChild(heart);
        }
        // 6秒后清理容器
        setTimeout(() => { container.remove(); }, 6000);
    }
    // 立即执行
    createHeartRain();
    </script>
    """
    # 设置 height=0 隐藏这个组件
    components.html(js_code, height=0)

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

    # === 阶段 2：粒子爱心凝聚 ===
    elif st.session_state.step == 2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>正在凝聚爱的粒子...</h3>", unsafe_allow_html=True)
        
        # 生成粒子数据
        df_heart = generate_particle_heart()
        
        # 使用 Altair 绘制粒子图
        chart = alt.Chart(df_heart).mark_circle(size=3, color='#FF1493', opacity=0.6).encode(
            x=alt.X('x', axis=None), # 隐藏坐标轴
            y=alt.Y('y', axis=None), # 隐藏坐标轴
            tooltip=alt.value(None)  # 禁用鼠标悬停提示
        ).properties(
            width=500,
            height=500,
            background='transparent' # 背景透明
        ).configure_view(strokeWidth=0) # 去掉边框

        st.altair_chart(chart, use_container_width=True)
        
        st.markdown("<h4 style='text-align: center; color: #FFB6C1;'>每一颗粒子，都是想你的瞬间 💓</h4>", unsafe_allow_html=True)
        
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.rerun()

    # === 阶段 3：时光机 & 合照 & 承诺 ===
    elif st.session_state.step == 3:
        # --- 日历动画 ---
        st.markdown("### 📅 我们的故事开始于...")
        date_display = st.empty()
        
        dates = ["Listening...", "Loading memories...", "2021-06-06"]
        for d in dates:
            date_display.markdown(f"<h1 style='text-align: center; color: white;'>{d}</h1>", unsafe_allow_html=True)
            time.sleep(0.8)
        
        # 触发一次爱心雨
        trigger_heart_rain()
        
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
        # 点击按钮触发满屏爱心
        if st.button("点我接收满屏爱心 💖"):
            st.session_state.step = 4
            st.rerun()

    # === 阶段 4：大结局 ===
    elif st.session_state.step == 4:
        # 触发持续的爱心雨
        trigger_heart_rain()
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>💖 永远爱你 💖</h1>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; color: #FF69B4; font-size: 20px; margin-top: 50px;">
                Happy Valentine's Day, My Love.<br>
                From 2021.06.06 to Forever.
            </div>
        """, unsafe_allow_html=True)
        
        # 提供一个重来的按钮
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("再看一遍我们的故事 🔄"):
            st.session_state.step = 0
            st.rerun()

if __name__ == "__main__":
    main()
