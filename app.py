import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import time
import streamlit.components.v1 as components

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="To Ruirui",
    page_icon="❤️",
    layout="centered"
)

# --- 2. CSS 样式：定义粒子雪花和爱心雨 ---
st.markdown("""
    <style>
    /* 全局背景黑色 */
    .stApp {
        background-color: #000000;
        color: #FF69B4;
    }
    
    /* 隐藏组件 */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* 按钮样式优化 */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF69B4;
        font-size: 16px;
        padding: 10px 24px;
        transition: all 0.3s;
        width: 100%;
        box-shadow: 0 0 10px rgba(255, 20, 147, 0.5); /* 按钮发光 */
    }
    .stButton>button:hover {
        background-color: #C71585;
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.8);
    }

    /* Altair 图表去边框 */
    #altair-viz-1 canvas { background-color: transparent !important; }

    /* --- 自定义粒子雪花样式 --- */
    .particle-snow {
        position: fixed;
        top: -10px;
        background: white;
        border-radius: 50%; /* 圆形粒子 */
        pointer-events: none;
        z-index: 9998;
        box-shadow: 0 0 5px white; /* 粒子发光 */
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 核心功能函数 ---

def generate_particle_heart(n_points=10000): # 增加到1万个点！
    """生成高密度爱心粒子"""
    t = np.linspace(0, 2 * np.pi, n_points)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # 增加更多随机扩散，让心看起来更毛茸茸、更饱满
    x += np.random.normal(0, 0.35, n_points)
    y += np.random.normal(0, 0.35, n_points)
    
    # 随机打乱顺序，绘制时更有质感
    indices = np.arange(n_points)
    np.random.shuffle(indices)
    return pd.DataFrame({'x': x[indices], 'y': y[indices]})

def create_particle_snow():
    """生成微小粒子雪花 JS"""
    js_code = """
    <script>
    function createSnowParticle() {
        const snow = document.createElement('div');
        snow.className = 'particle-snow';
        // 随机大小：2px 到 5px
        const size = Math.random() * 3 + 2; 
        snow.style.width = size + 'px';
        snow.style.height = size + 'px';
        snow.style.left = Math.random() * 100 + 'vw';
        // 随机透明度
        snow.style.opacity = Math.random() * 0.5 + 0.3;
        
        document.body.appendChild(snow);

        // 飘落动画
        const duration = Math.random() * 5000 + 3000; // 3-8秒
        const keyframes = [
            { transform: 'translate(0, 0)' },
            { transform: `translate(${Math.random() * 50 - 25}px, 110vh)` } // 稍微左右飘动
        ];
        
        const animation = snow.animate(keyframes, {
            duration: duration,
            easing: 'linear',
            fill: 'forwards'
        });

        animation.onfinish = () => snow.remove();
    }
    // 每 50ms 生成一个粒子
    setInterval(createSnowParticle, 50);
    </script>
    """
    components.html(js_code, height=0)

def trigger_heart_rain():
    """全屏爱心雨"""
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
        for (let i = 0; i < 200; i++) { // 200个爱心
            const heart = document.createElement('div');
            heart.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            heart.style.position = 'absolute';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.top = -50 + 'px';
            heart.style.fontSize = (Math.random() * 25 + 15) + 'px';
            heart.animate([
                { transform: 'translateY(0px)' },
                { transform: 'translateY(110vh)' }
            ], {
                duration: Math.random() * 2000 + 2000,
                easing: 'linear'
            });
            container.appendChild(heart);
        }
        setTimeout(() => container.remove(), 4000);
    }
    createHeartRain();
    </script>
    """
    components.html(js_code, height=0)

# --- 4. 状态管理初始化 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'stage3_played' not in st.session_state:
    st.session_state.stage3_played = False # 专门用来解决“跳回图片”的锁

# --- 5. 主流程 ---

def main():
    
    # 始终在后台播放粒子雪花（除了第一步）
    if st.session_state.step > 0:
        create_particle_snow()

    # === 阶段 0：密码解锁 ===
    if st.session_state.step == 0:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>🔒 专属空间 Access</h3>", unsafe_allow_html=True)
        password = st.text_input("请输入通关密码（名字）：", type="password")
        
        if password in ["刘蕊萌", "睿睿", "ruirui", "Ruimeng", "宝宝"]:
            st.session_state.step = 1
            st.rerun()

    # === 阶段 1：初次见面 ===
    elif st.session_state.step == 1:
        st.markdown("<br><br>", unsafe_allow_html=True)
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
        
        # 绘制 10000 个粒子的爱心
        df_heart = generate_particle_heart(10000)
        
        chart = alt.Chart(df_heart).mark_circle(size=2, color='#FF1493', opacity=0.8).encode(
            x=alt.X('x', axis=None),
            y=alt.Y('y', axis=None),
            tooltip=alt.value(None)
        ).properties(
            width=500, height=500, background='transparent'
        ).configure_view(strokeWidth=0)

        st.altair_chart(chart, use_container_width=True)
        
        st.markdown("<h4 style='text-align: center; color: #FFB6C1;'>用 10,000 个粒子凝聚成对你的喜欢 💓</h4>", unsafe_allow_html=True)
        
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.rerun()

    # === 阶段 3：时光机 & 合照（修复了跳回图片的问题） ===
    elif st.session_state.step == 3:
        
        placeholder = st.empty()
        
        # --- 关键修复：加锁逻辑 ---
        # 只有第一次进入这个阶段时，才播放动画（倒计时、照片）
        # 点击按钮后，因为 stage3_played 已经是 True，会跳过这些，直接显示按钮
        if not st.session_state.stage3_played:
            with placeholder.container():
                # 倒计时动画
                st.markdown("### 📅 我们的故事开始于...")
                dates = ["Listening...", "Loading...", "2021-06-06"]
                for d in dates:
                    st.markdown(f"<h1 style='text-align: center; color: white;'>{d}</h1>", unsafe_allow_html=True)
                    time.sleep(0.8)
                
                # 触发一次爱心雨
                trigger_heart_rain()
                time.sleep(1)
                
                # 显示合照
                try:
                    st.image("love.png", caption="那时候的我们", use_column_width=True)
                    time.sleep(4)
                except:
                    st.warning("（记得传照片 love.png）")
                    time.sleep(2)
            
            # 播放完后清空占位符
            placeholder.empty()
            # 标记为已播放
            st.session_state.stage3_played = True
            # 强制刷新一次，进入稳定状态
            st.rerun()

        # --- 稳定状态（动画播完后显示的内容） ---
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>这是我们要一起过的第 <span style='color:red; font-size:30px'>5</span> 个情人节</h3>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>✨ 我们还要过好多个情人节 ✨</h2>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 这个按钮现在点击非常丝滑，因为不会再去跑上面的动画代码了
        if st.button("点我接收满屏爱心 💖"):
            st.session_state.step = 4
            st.rerun()

    # === 阶段 4：大结局 ===
    elif st.session_state.step == 4:
        # 进入瞬间触发爱心雨
        trigger_heart_rain()
        
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
            # 重置所有状态
            st.session_state.step = 0
            st.session_state.stage3_played = False
            st.rerun()

if __name__ == "__main__":
    main()
