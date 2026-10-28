import random
import streamlit as st

# Personalize these before deploying
CRUSH_NAME = "Hana"
YOUR_NAME = "Lix Aldrin"

st.set_page_config(
    page_title="A Little Something for You 💗",
    page_icon="💌",
    layout="centered",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5 0%, #ffe0eb 50%, #fff8fb 100%);
    color: #63334b;
}
.block-container { max-width: 760px; padding-top: 2rem; }
.love-card {
    background: rgba(255,255,255,0.88);
    border: 2px solid #ffc4d8;
    border-radius: 24px;
    padding: 2rem 1.5rem;
    text-align: center;
    box-shadow: 0 12px 35px rgba(214, 51, 108, 0.10);
}
.big-heart { font-size: 3.2rem; }
h1, h2, h3 { color: #d6336c !important; }
div.stButton > button {
    border-radius: 16px;
    border: 1px solid #ff9fbd;
    background: #ff5c93;
    color: white;
    min-height: 3rem;
    font-weight: 600;
}
div.stButton > button:hover {
    background: #d6336c;
    border-color: #d6336c;
    color: white;
}
.soft-note {
    background: #fff0f5;
    border-radius: 16px;
    padding: 1rem;
    border: 1px solid #ffd0df;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = []

def go(page):
    st.session_state.page = page
    st.rerun()

def header(emoji, title, subtitle=""):
    st.markdown(
        f'<div class="love-card"><div class="big-heart">{emoji}</div>'
        f'<h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )

def home():
    header("💗", f"Hey, {CRUSH_NAME}!", "I made a little something just for you...")
    st.write("")
    st.markdown(
        '<div class="soft-note" style="text-align:center">'
        'A tiny question from someone who likes you…<br><br>'
        'There is a little note, a fun quiz, and a surprise waiting inside. 💌'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    left, right = st.columns(2)
    with left:
        if st.button("Open your surprise 💌", use_container_width=True):
            go("confession")
    with right:
        if st.button("Play a tiny quiz 🌷", use_container_width=True):
            st.session_state.quiz_index = 0
            st.session_state.quiz_answers = []
            go("quiz")
    st.markdown(
        f'<p style="text-align:center;color:#9b7185;margin-top:2rem">'
        f'Made with courage and 💗 — {YOUR_NAME}</p>',
        unsafe_allow_html=True,
    )

def confession():
    header("💌", "Something I've Been Meaning to Tell You", f"For {CRUSH_NAME}")
    st.write("")
    st.markdown(
        '<div class="soft-note" style="text-align:center">'
        "I don't know if you already noticed, but I think you're really special.<br><br>"
        "You have this way of making an ordinary day feel a little brighter. "
        "I like your smile, your energy, and the little things that make you who you are.<br><br>"
        "I don't want to put any pressure on you. I just wanted to be honest "
        "about how I feel. Whatever your answer is, thank you for being you. 💗"
        '</div>',
        unsafe_allow_html=True,
    )
    st.subheader("Would you like to go on a date with me sometime?")
    st.caption("Whatever your answer, no pressure at all. ❤️")
    yes, time, back = st.columns(3)
    with yes:
        if st.button("Yes! 💖", use_container_width=True):
            go("yes")
    with time:
        if st.button("I need time 🌷", use_container_width=True):
            go("time")
    with back:
        if st.button("Home", use_container_width=True):
            go("home")

def quiz():
    questions = [
        ("What's the best kind of date?", [
            "A cozy café and a long talk ☕",
            "A fun little adventure 🌈",
            "A movie and snacks 🍿",
        ]),
        ("Pick a tiny happy moment:", [
            "A random sweet message 💌",
            "Laughing at silly jokes 😂",
            "Watching the sunset 🌇",
        ]),
        ("Choose a perfect vibe:", [
            "Soft music and warm lights 🎶",
            "Flowers and a handwritten note 🌷",
            "Spontaneous fun together 🎉",
        ]),
    ]
    idx = st.session_state.quiz_index
    if idx >= len(questions):
        go("quiz_result")
        return
    header("🌷", "A Tiny Love Quiz", f"Question {idx + 1} of {len(questions)}")
    question, answers = questions[idx]
    st.subheader(question)
    choice = st.radio("Choose your favorite:", answers, key=f"quiz_{idx}", label_visibility="collapsed")
    if st.button("Next question →", use_container_width=True):
        st.session_state.quiz_answers.append(choice)
        st.session_state.quiz_index += 1
        st.rerun()
    if st.button("Back to home", use_container_width=True):
        go("home")

def quiz_result():
    header("✨💗", "That's the end!", "Thanks for playing.")
    st.write("Your picks were:")
    for answer in st.session_state.quiz_answers:
        st.write(f"♡ {answer}")
    st.info("There's no score—this quiz is just a cute way to share a smile. 💕")
    if st.button("See the surprise 🎁", use_container_width=True):
        go("surprise")
    if st.button("Play again", use_container_width=True):
        st.session_state.quiz_index = 0
        st.session_state.quiz_answers = []
        go("quiz")

def surprise():
    header("🎁", "One Last Little Thing…", "A message just for you.")
    st.markdown(
        f'<div class="soft-note" style="text-align:center">'
        f'{CRUSH_NAME},<br><br>'
        "If this made you smile even a little, then it was worth making. "
        "You deserve kindness, honesty, and happiness—always.<br><br>"
        "Thanks for being someone worth making a little app for. 💗"
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown(f"<h3 style='text-align:center'>With a little courage, {YOUR_NAME} ♡</h3>", unsafe_allow_html=True)
    if st.button("Back to home", use_container_width=True):
        go("home")

def answer_page(positive):
    if positive:
        header("🥹💖", "Awww, really?!", "This is a very happy moment.")
        st.success("YOU JUST MADE MY DAY! 💗\n\nLet's plan something fun together. No pressure to decide everything now!")
        st.balloons()
        st.snow()
    else:
        header("🌷", "No pressure at all", "Take your time.")
        st.info("Of course. Take all the time you need. Thank you for hearing me out. Your comfort matters to me.")
    if st.button("Back to home", use_container_width=True):
        go("home")

st.markdown("<div style='text-align:center;font-size:1rem'>♡ a little corner of the internet made with courage ♡</div>", unsafe_allow_html=True)
st.write("")

if st.session_state.page == "home":
    home()
elif st.session_state.page == "confession":
    confession()
elif st.session_state.page == "quiz":
    quiz()
elif st.session_state.page == "quiz_result":
    quiz_result()
elif st.session_state.page == "surprise":
    surprise()
elif st.session_state.page == "yes":
    answer_page(True)
elif st.session_state.page == "time":
    answer_page(False)
