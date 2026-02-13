import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image

# --- 1. 页面基础设置 ---
st.set_page_config(
    page_title="For My 蕊萌",
    page_icon="🤍", # 用白色爱心，显高级
    layout="centered"
)

# --- 2. 极简高级风 CSS (玻璃拟态 + 动态渐变) ---
# 这是一个非常流行的INS风配色和CSS样式
custom_css = """
<style>
    /* 隐藏默认菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 背景：高级灰粉渐变 */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }
    
    /* 玻璃拟态卡片效果 */
    div.css-1r6slb0, .stMetric {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    }
    
    /* 标题样式 */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #2c3e50;
        font-weight: 300;
        text-align: center;
        letter-spacing: 2px;
    }
    
    /* 名字的高亮 */
    .name-highlight {
        color: #e84393;
        font-weight: bold;
    }
    
    /* 自定义按钮样式 */
    .stButton>button {
        width: 100%;
        background-color: #ff7675;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #d63031;
        transform: scale(1.02);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- 3. 核心功能函数 ---

def draw_heart():
    """用数学公式画一个高级的爱心"""
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # 创建图表，设置透明背景
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(x, y, color='#e84393', linewidth=3) # 高级粉色线条
    ax.fill(x, y, color='#ffeaa7', alpha=0.3)   # 内部淡黄色填充
    ax.axis('off') # 去掉坐标轴
    fig.patch.set_alpha(0) # 图表背景透明
    return fig

def get_days_together():
    """计算在一起的天数（这里假设你们是5年前的今天在一起的，你可以修改日期）"""
    start_date = datetime(2021, 6, 6) # 修改这里为你们的纪念日
    now = datetime.now()
    delta = now - start_date
    return delta.days

# --- 4. 主页面逻辑 ---

def main():
    # 侧边栏解锁（保留这个互动，很有趣）
    with st.sidebar:
        st.write("🔐 Identity Verification")
        name = st.text_input("Please enter your name:", type="password") # 密码模式更有神秘感
        
    if name in ["睿睿", "Ruimeng", "ruimeng", "宝宝", "niu"]:
        # --- 页面头部 ---
        st.markdown("<h1>HEY, <span class='name-highlight'>LIU RUIMENG</span></h1>", unsafe_allow_html=True)
        st.caption("Happy Valentine's Day · 5th Anniversary")
        
        st.write("---")
        
        # --- 照片展示区 (拍立得风格) ---
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            try:
                # 记得上传一张名为 love.png 的合照
                image = Image.open('spongebob.png') 
                st.image(image, caption="You & Me", use_column_width=True)
            except:
                st.error("📷 请上传一张合照并命名为 spongebob.png")

        st.write("")
        
        # --- 数据可视化区 (理科生的浪漫) ---
        st.markdown("### ⏳ Time Record")
        days = get_days_together()
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("We have been together", f"{days} Days")
        with col_b:
            st.metric("Valentine's Day", "5th")

        st.write("")
        st.write("---")

        # --- 核心互动区：数学爱心 ---
        st.markdown("### 🎨 Code My Love")
        st.write("这是用 Python 的 Matplotlib 库为你画的专属心形线：")
        st.latex(r"x = 16\sin^3(t)")
        st.latex(r"y = 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t)")
        
        # 按钮互动
        if st.button("Generate Heart ❤️"):
            # 进度条增加仪式感
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
            
            # 展示爱心图
            st.pyplot(draw_heart())
            
            # 这里不用气球(balloons)，改用漫天雪花(snow)，雪花在白色背景下更唯美高级
            st.snow() 
            
            st.markdown("""
            > "Mathematics may not teach us how to add love or minus hate, 
            > but it gives us every reason to hope that every problem has a solution."
            > \n> 而你，就是我所有问题的最优解。
            """)
            
    elif name == "":
        st.title("🔒 这是一个被加密的浪漫")
        st.markdown("请在左侧输入你的名字解锁")
    else:
        st.error("Access Denied. 名字不对哦~")

if __name__ == "__main__":
    main()
