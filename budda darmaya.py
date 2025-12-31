import streamlit as st
import time  # පණිවිඩය පෙන්වීමට කාලය ලබා ගැනීමට

st.set_page_config(page_title="බුද්ධ ධර්මය ප්‍රශ්නාවලිය", page_icon="🙏")

# CSS - Buttons ලස්සනට පෙන්වීමට
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ff9933;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        height: 3.5em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

def play_sound(url):
    st.markdown(f'<audio autoplay><source src="{url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# ප්‍රශ්න 50 (කලින් දුන් ලැයිස්තුවම මෙතනට දාන්න - මම කෙටියෙන් දක්වන්නම්)
questions = [
    {"question": "සිදුහත් බෝසතාණන් වහන්සේ සම්මා සම්බුද්ධත්වයට පත් වූයේ කුමන පොහොය දිනකද?", "options": ["වෙසක්", "පොසොන්", "ඇසළ", "දුරුතු"], "answer": "වෙසක්"},
    {"question": "බුදුරජාණන් වහන්සේ බුදු වී මුල් සති ය හත ගත කළ කාලය හඳුන්වන්නේ කුමන නමකින්ද?", "options": ["සත් සතිය", "අටමස්ථානය", "සොළොස්මස්ථානය", "සූවිසි විවරණය"], "answer": "සත් සතිය"},
    # ... අනෙක් ප්‍රශ්න 48ම මෙතැන තිබිය යුතුය ...
]

# Session State
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False

st.title("☸️ බුද්ධ ධර්මය ප්‍රශ්නාවලිය")

if not st.session_state.quiz_complete:
    q_idx = st.session_state.current_q
    
    if q_idx < len(questions):
        st.subheader(f"ප්‍රශ්නය {q_idx + 1} / {len(questions)}")
        st.write(questions[q_idx]['question'])

        col1, col2 = st.columns(2)
        opts = questions[q_idx]["options"]
        
        # පිළිතුර පරීක්ෂා කිරීමේ logic එක
        for i, option in enumerate(opts):
            with col1 if i % 2 == 0 else col2:
                if st.button(option, key=f"btn_{q_idx}_{i}"):
                    if option == questions[q_idx]["answer"]:
                        st.success("නිවැරදියි! 🎉")
                        st.session_state.score += 1
                        play_sound("https://www.soundjay.com/buttons/sounds/button-3.mp3")
                    else:
                        st.error(f"වැරදියි! ❌ නිවැරදි පිළිතුර: {questions[q_idx]['answer']}")
                        play_sound("https://www.soundjay.com/buttons/sounds/button-10.mp3")
                    
                    # තත්පර 2ක් පණිවිඩය පෙන්වා සිටින්න
                    time.sleep(2) 
                    
                    st.session_state.current_q += 1
                    if st.session_state.current_q >= len(questions):
                        st.session_state.quiz_complete = True
                    st.rerun()

else:
    st.balloons()
    st.title("තරඟය අවසන්! 🏁")
    st.header(f"ඔබේ ලකුණු සංඛ්‍යාව: {st.session_state.score} / {len(questions)}")
    if st.button("නැවත ආරම්භ කරන්න"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.rerun()
