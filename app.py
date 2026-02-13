import streamlit as st
import time
from datetime import datetime

# --- 1. 页面配置：黑色沉浸式 ---
st.set_page_config(
    page_title="To Ruirui",
    page_icon="❤️",
    layout="centered"
)

# --- 2. CSS 样式：黑色背景 + 粉色文字 + 动态效果 ---
st.markdown("""
    <style>
    /* 全局背景黑色 */
    .stApp {
        background-color: #000000;
        color: #FF69B4; /* 粉色文字 */
    }
    
    /* 隐藏顶部和脚部 */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 按钮样式 - 粉色霓虹感 */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF69B4;
        font-size: 18px;
        padding: 10px 30px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #C71585;
        border-color: white;
        transform: scale(1.1);
    }

    /* 标题样式 */
    h1, h2, h3 {
        color: #FF69B4 !important;
        text-align: center;
        text-shadow: 0 0 10px #FF1493;
    }
    
    /* 普通文字样式 */
    p {
        color: #FFB6C1;
        font-size: 18px;
        text-align: center;
    }

    /* 跳动爱心动画 */
    @keyframes heartbeat {
        0% { transform: scale(1); }
        25% { transform: scale(1.1); }
        40% { transform: scale(1); }
        60% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .heart-beat {
        font-size: 100px;
        color: #FF1493;
        text-align: center;
        animation: heartbeat 1.5s infinite;
        margin: 20px 0;
    }
    
    /* 满屏爱心雨特效 */
    .falling-heart {
        position: fixed;
        top: -10%;
        color: #FF1493;
        animation: fall linear forwards;
    }
    @keyframes fall {
        to { transform: translateY(110vh); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 状态管理（剧本控制） ---
if 'step' not in st.session_state:
    st.session_state.step = 0

# --- 4. 辅助函数 ---
def create_heart_rain():
    # 简单的满屏爱心飘落效果
    st.markdown("""
    <script>
    const body = document.body;
    for (let i = 0; i < 50; i++) {
        const heart = document.createElement('div');
        heart.innerHTML = '❤️';
        heart.className = 'falling-heart';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.fontSize = (Math.random() * 20 + 20) + 'px';
        heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
        body.appendChild(heart);
    }
    </script>
    """, unsafe_allow_html=True)

# --- 5. 主剧本逻辑 ---

def main():
    # === 阶段 0：密码解锁 ===
    if st.session_state.step == 0:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("### 🔒 这是一个专属空间")
        password = st.text_input("请输入暗号（名字）：", type="password")
        
        if password in ["刘蕊萌", "睿睿", "ruirui", "Ruimeng", "宝宝"]:
            st.session_state.step = 1
            st.rerun() # 刷新页面进入下一阶段

    # === 阶段 1：初次见面 & 飘雪 ===
    elif st.session_state.step == 1:
        st.snow() # 飘雪
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.title("❄️ 睿睿，情人节快乐 ❄️")
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.write("大宝想问你：")
        st.markdown("### 是否愿意和大宝一起过情人节？")
        
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("是，我愿意 ❤️"):
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("否 💔"):
                st.error("⚠️ 大宝不允许！禁止选这个！请重新选择！")

    # === 阶段 2：跳动的爱心 ===
    elif st.session_state.step == 2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        # 纯CSS实现的跳动爱心
        st.markdown('<div class="heart-beat">❤️</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("让我们一起开始 🚀"):
            st.session_state.step = 3
            st.rerun()

    # === 阶段 3：时光机 & 合照 & 承诺 ===
    elif st.session_state.step == 3:
        # --- 3.1 日历动画 ---
        st.markdown("### 📅 我们的故事开始于...")
        date_text = st.empty()
        
        # 模拟日历翻动效果
        start_date = "2021-06-06"
        for i in range(1, 11):
            date_text.markdown(f"<h2 style='opacity: {i/10}'>{start_date}</h2>", unsafe_allow_html=True)
            time.sleep(0.1)
        
        time.sleep(1)
        st.balloons() # 气球飘上来
        
        st.markdown(f"### 这是我们要一起过的第 <span style='color:red; font-size:30px'>5</span> 个情人节", unsafe_allow_html=True)
        time.sleep(1)
        
        # --- 3.2 合照出现又消失 ---
        photo_placeholder = st.empty()
        try:
            # 显示合照
            photo_placeholder.image("love.png", caption="那时候的我们", use_column_width=True)
            time.sleep(4) # 合照停留4秒
            photo_placeholder.empty() # 合照消失
        except:
            photo_placeholder.warning("（这里本该有一张合照，但大宝忘了传 love.png）")
            time.sleep(2)
            photo_placeholder.empty()

        # --- 3.3 承诺文字 ---
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### ✨ 我们还要过好多个情人节 ✨")
        st.markdown("❤ ❤ ❤ ❤ ❤") # 许多爱心点缀
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("点我接收满屏爱心 💖"):
            st.session_state.step = 4
            st.rerun()

    # === 阶段 4：大结局 ===
    elif st.session_state.step == 4:
        st.title("💖 永远爱你 💖")
        st.balloons() # 第一波气球
        
        # 再次触发雪花，营造唯美感
        st.snow()
        
        st.markdown("""
            <div style="text-align: center; color: #FF69B4; font-size: 20px;">
                Happy Valentine's Day, My Love.<br>
                From 2021.06.06 to Forever.
            </div>
        """, unsafe_allow_html=True)
        
        # 提供一个重来的按钮，防止想再看一遍
        if st.button("再看一遍我们的故事 🔄"):
            st.session_state.step = 0
            st.rerun()

if __name__ == "__main__":
    main()
