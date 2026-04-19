"""
app.py — AI Code Assistant  |  Main Streamlit entry point
"""

import streamlit as st
from router import route
from config import TAGS, APP_TITLE, APP_ICON

# ─── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #0d1117 !important;
    font-family: 'Space Grotesk', sans-serif;
}

[data-testid="stAppViewContainer"] > .main {
    background: #0d1117 !important;
    padding: 0 !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }

/* ── App Shell ── */
.app-shell {
    min-height: 100vh;
    background: #0d1117;
    display: flex;
    flex-direction: column;
}

/* ── Top Bar ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 32px;
    background: rgba(22, 33, 48, 0.95);
    border-bottom: 1px solid rgba(99, 179, 187, 0.15);
    backdrop-filter: blur(12px);
    position: sticky;
    top: 0;
    z-index: 100;
}

.topbar-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.topbar-logo {
    width: 34px; height: 34px;
    background: linear-gradient(135deg, #63b3bd 0%, #3a7bd5 100%);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 700; color: white;
    box-shadow: 0 0 14px rgba(99, 179, 187, 0.5);
}

.topbar-title {
    font-size: 15px; font-weight: 600;
    color: #e2e8f0; letter-spacing: 0.3px;
}

.topbar-right {
    display: flex; align-items: center; gap: 14px;
}

.topbar-badge {
    font-size: 10px; font-weight: 600;
    background: rgba(99, 179, 187, 0.15);
    color: #63b3bd;
    border: 1px solid rgba(99, 179, 187, 0.3);
    padding: 3px 8px; border-radius: 20px;
    letter-spacing: 0.5px;
}

/* ── Main Content ── */
.main-content {
    flex: 1;
    padding: 32px 32px 20px;
    display: flex;
    flex-direction: column;
}

/* ── Hero (landing) ── */
.hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 48px 0 36px;
    text-align: center;
}

.hero-eyebrow {
    font-size: 11px; font-weight: 600; letter-spacing: 3px;
    color: #63b3bd; text-transform: uppercase; margin-bottom: 12px;
}

.hero-title {
    font-size: clamp(28px, 4vw, 48px); font-weight: 700;
    color: #f0f6fc; line-height: 1.15; margin-bottom: 14px;
    background: linear-gradient(135deg, #f0f6fc 30%, #63b3bd 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: 15px; color: #7a90a4; max-width: 480px;
    line-height: 1.65;
}

/* ── Tag Grid ── */
.tag-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    justify-content: center;
    margin-top: 36px;
    transition: all 0.45s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Compact mode (after selection) */
.tag-grid.compact {
    gap: 8px;
    margin-top: 0;
}

.tag-card {
    position: relative;
    cursor: pointer;
    transition: all 0.45s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 16px;
    overflow: hidden;
    user-select: none;
    transform: translateY(0);
}

/* Default (landing) card */
.tag-card.default {
    width: 100%;
    max-width: 280px;
    margin: 0 auto;
    box-sizing: border-box;
    background: linear-gradient(135deg, rgba(22, 40, 58, 0.9) 0%, rgba(18, 32, 46, 0.95) 100%);
    border: 1px solid rgba(99, 179, 187, 0.15);
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
    padding: 28px 24px 24px;
    animation: cardEntrance 0.6s cubic-bezier(0.4, 0, 0.2, 1) both;
}

/* Compact card */
.tag-card.compact-card {
    width: auto;
    padding: 8px 16px 8px 12px;
    border-radius: 30px;
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(22, 40, 58, 0.85);
    border: 1px solid rgba(99, 179, 187, 0.15);
    font-size: 13px; font-weight: 600;
}

.tag-card.compact-card .card-icon { font-size: 16px; }
.tag-card.compact-card .card-label { font-size: 13px; font-weight: 600; color: #c8d8e8; }
.tag-card.compact-card .card-desc  { display: none; }
.tag-card.compact-card .card-glow  { display: none; }

/* Active state */
.tag-card.active {
    border-color: var(--card-color) !important;
    box-shadow: 0 0 0 2px var(--card-color), 0 8px 32px rgba(0,0,0,0.5) !important;
    background: linear-gradient(135deg, rgba(22, 40, 58, 1) 0%, rgba(18, 32, 46, 1) 100%) !important;
    transform: translateY(-2px);
}

.tag-card.active .card-label { color: var(--card-color) !important; }
.tag-card.active .card-icon  { filter: drop-shadow(0 0 6px var(--card-color)); }

/* Dimmed state */
.tag-card.dimmed {
    opacity: 0.4;
    transform: scale(0.97);
    filter: saturate(0.4);
}

.tag-card:hover:not(.dimmed) {
    transform: translateY(-4px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    border-color: rgba(99, 179, 187, 0.4);
}

/* Card internals */
.card-glow {
    position: absolute; top: -40px; right: -40px;
    width: 100px; height: 100px;
    border-radius: 50%;
    background: radial-gradient(circle, var(--card-color) 0%, transparent 70%);
    opacity: 0.12;
    pointer-events: none;
}

.card-icon-wrap {
    width: 42px; height: 42px;
    border-radius: 10px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 14px;
    font-size: 20px;
    backdrop-filter: blur(4px);
}

.card-label {
    font-size: 16px; font-weight: 700;
    color: #e2e8f0; margin-bottom: 6px; letter-spacing: 0.2px;
}

.card-desc {
    font-size: 12px; color: #637080; line-height: 1.5;
}

/* Card entrance animation */
@keyframes cardEntrance {
    from { opacity: 0; transform: translateY(20px) scale(0.96); }
    to   { opacity: 1; transform: translateY(0)    scale(1);    }
}

/* Staggered delays */
.tag-card:nth-child(1) { animation-delay: 0.05s; }
.tag-card:nth-child(2) { animation-delay: 0.12s; }
.tag-card:nth-child(3) { animation-delay: 0.19s; }
.tag-card:nth-child(4) { animation-delay: 0.26s; }
.tag-card:nth-child(5) { animation-delay: 0.33s; }
.tag-card:nth-child(6) { animation-delay: 0.40s; }

/* ── Chat Area ── */
.chat-area {
    flex: 1;
    max-width: 820px;
    width: 100%;
    margin: 0 auto;
    padding-top: 20px;
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.chat-area-title {
    font-size: 13px; font-weight: 600; letter-spacing: 1.5px;
    color: #4a6070; text-transform: uppercase; text-align: center;
    margin-bottom: 6px;
}

.msg-row { display: flex; gap: 10px; align-items: flex-start; }
.msg-row.user  { justify-content: flex-end;  }
.msg-row.assistant { justify-content: flex-start; }

.msg-avatar {
    width: 32px; height: 32px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; flex-shrink: 0;
}

.msg-avatar.user-av {
    background: linear-gradient(135deg, #3a7bd5, #63b3bd);
}

.msg-avatar.ai-av {
    background: linear-gradient(135deg, #1a3a4a, #2a5068);
    border: 1px solid rgba(99, 179, 187, 0.3);
}

.msg-bubble {
    max-width: 78%;
    padding: 12px 16px;
    border-radius: 16px;
    font-size: 14px; line-height: 1.65;
}

.msg-bubble.user {
    background: linear-gradient(135deg, #1e3a5a, #254a6a);
    color: #d4e8f5;
    border: 1px solid rgba(99, 179, 187, 0.2);
    border-bottom-right-radius: 4px;
}

.msg-bubble.assistant {
    background: rgba(22, 33, 48, 0.9);
    color: #c8d8e8;
    border: 1px solid rgba(99, 179, 187, 0.12);
    border-bottom-left-radius: 4px;
}

/* Code blocks inside responses */
.msg-bubble pre {
    background: #0a0f17 !important;
    border: 1px solid rgba(99, 179, 187, 0.2);
    border-radius: 8px;
    padding: 12px 14px;
    overflow-x: auto;
    margin: 10px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #a8d5e2;
}

/* ── Input Bar ── */
.input-section {
    max-width: 820px;
    width: 100%;
    margin: 16px auto 20px;
}

.active-mode-chip {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 11px; font-weight: 600;
    color: var(--active-color, #63b3bd);
    background: rgba(99, 179, 187, 0.08);
    border: 1px solid rgba(99, 179, 187, 0.2);
    border-radius: 20px;
    padding: 4px 10px;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}

/* Streamlit text area */
[data-testid="stTextArea"] textarea {
    background: rgba(18, 28, 42, 0.95) !important;
    border: 1px solid rgba(99, 179, 187, 0.2) !important;
    border-radius: 14px !important;
    color: #c8d8e8 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 14px !important;
    padding: 14px 16px !important;
    resize: vertical !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
    transition: border-color 0.2s ease !important;
}

[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(99, 179, 187, 0.5) !important;
    box-shadow: 0 0 0 3px rgba(99, 179, 187, 0.08) !important;
    outline: none !important;
}

/* Streamlit buttons */
.stButton > button {
    background: linear-gradient(135deg, #1e4060 0%, #0f2535 100%) !important;
    color: #63b3bd !important;
    border: 1px solid rgba(99, 179, 187, 0.35) !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 8px 20px !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.3px !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #264d78 0%, #163048 100%) !important;
    border-color: rgba(99, 179, 187, 0.6) !important;
    box-shadow: 0 4px 16px rgba(99, 179, 187, 0.2) !important;
    transform: translateY(-1px) !important;
}

/* Send button special style */
.send-btn > button {
    background: linear-gradient(135deg, #1e6060 0%, #0f3535 100%) !important;
    color: #a0e8d8 !important;
    border-color: rgba(99, 187, 179, 0.4) !important;
    min-width: 100px !important;
}

/* Streamlit expander */
[data-testid="stExpander"] {
    background: rgba(18, 28, 42, 0.7) !important;
    border: 1px solid rgba(99, 179, 187, 0.12) !important;
    border-radius: 12px !important;
    margin-bottom: 10px !important;
}

[data-testid="stExpander"] summary {
    color: #7a9aaa !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(99, 179, 187, 0.25); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(99, 179, 187, 0.45); }

/* Divider */
hr { border-color: rgba(99, 179, 187, 0.1) !important; margin: 16px 0 !important; }

/* Streamlit markdown */
.stMarkdown p { color: #9ab0c0; font-size: 14px; }

/* Spinner */
[data-testid="stSpinner"] { color: #63b3bd !important; }

/* Remove default padding from columns */
[data-testid="column"] { padding: 0 4px !important; }
</style>
""", unsafe_allow_html=True)


# ─── State init ───────────────────────────────────────────────────────────────
if "active_tag"   not in st.session_state: st.session_state.active_tag   = None
if "messages"     not in st.session_state: st.session_state.messages     = []
if "show_chat"    not in st.session_state: st.session_state.show_chat    = False


# ─── Tag colour map ───────────────────────────────────────────────────────────
TAG_COLORS = {k: v["color"] for k, v in TAGS.items()}


# ─── Top bar ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-left">
    <div class="topbar-logo">AI</div>
    <span class="topbar-title">AI Code Assistant</span>
  </div>
  <div class="topbar-right">
    <span class="topbar-badge">GROK-3</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ─── Tag cards ────────────────────────────────────────────────────────────────
def render_cards(compact: bool = False):
    """Render the six mode cards. compact=True means chip-style row."""
    tag_keys = list(TAGS.keys())
    active   = st.session_state.active_tag

    if compact:
        cols = st.columns(len(tag_keys), gap="small")
        for i, key in enumerate(tag_keys):
            cfg = TAGS[key]
            with cols[i]:
                is_active = (key == active)
                extra_style = (
                    f"border-color:{cfg['color']}; color:{cfg['color']};"
                    f"box-shadow:0 0 0 2px {cfg['color']}30;"
                ) if is_active else ""
                dim_style   = "opacity:0.38; filter:saturate(0.3);" if (active and not is_active) else ""
                if st.button(
                    f"{cfg['icon']}  {cfg['label']}",
                    key=f"tag_compact_{key}",
                    use_container_width=True,
                ):
                    if st.session_state.active_tag == key:
                        # deselect
                        st.session_state.active_tag = None
                        st.session_state.show_chat  = False
                        st.session_state.messages   = []
                    else:
                        st.session_state.active_tag = key
                        st.session_state.show_chat  = True
                    st.rerun()
    else:
        # Landing grid — 3 columns, 2 rows
        row1 = st.columns(3, gap="medium")
        row2 = st.columns(3, gap="medium")
        rows = [row1, row2]
        for idx, key in enumerate(tag_keys):
            cfg      = TAGS[key]
            row_idx  = idx // 3
            col_idx  = idx % 3
            is_active = (key == active)

            with rows[row_idx][col_idx]:
                card_html = f"""
                <div class="tag-card default {'active' if is_active else ''}"
                     style="--card-color:{cfg['color']}">
                  <div class="card-glow"></div>
                  <div class="card-icon-wrap">
                    <span class="card-icon">{cfg['icon']}</span>
                  </div>
                  <div class="card-label">{cfg['label']}</div>
                  <div class="card-desc">{cfg['description']}</div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                if st.button("Select", key=f"tag_grid_{key}", use_container_width=True):
                    st.session_state.active_tag = key
                    st.session_state.show_chat  = True
                    st.session_state.messages   = []
                    st.rerun()


# ─── Main layout ──────────────────────────────────────────────────────────────
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if not st.session_state.show_chat:
    # ── Landing view ──────────────────────────────────────────────────────
    st.markdown("""
    <div class="hero">
      <div class="hero-eyebrow">Powered by Grok-3</div>
      <div class="hero-title">Your AI Code Assistant</div>
      <div class="hero-sub">Choose a mode below to start. Fix bugs, generate code,
        brainstorm ideas, or get visual explanations — all in one place.</div>
    </div>
    """, unsafe_allow_html=True)

    render_cards(compact=False)

else:
    # ── Compact tag bar ────────────────────────────────────────────────────
    st.markdown('<div style="padding-bottom:10px;">', unsafe_allow_html=True)
    render_cards(compact=True)
    st.markdown('</div>', unsafe_allow_html=True)

    active    = st.session_state.active_tag
    active_cfg = TAGS[active]
    color     = active_cfg["color"]

    st.markdown(f"""
    <div style="text-align:center; margin: 8px 0 16px;">
      <span style="display:inline-flex; align-items:center; gap:8px;
                   background:rgba(22,40,58,0.8); border:1px solid {color}40;
                   border-radius:24px; padding:6px 16px;">
        <span style="font-size:18px;">{active_cfg['icon']}</span>
        <span style="font-size:13px; font-weight:700; color:{color}; letter-spacing:0.5px;">
          {active_cfg['label'].upper()} MODE
        </span>
        <span style="font-size:12px; color:#6a8090;">— {active_cfg['description']}</span>
      </span>
    </div>
    """, unsafe_allow_html=True)

    # ── Chat history ───────────────────────────────────────────────────────
    st.markdown('<div class="chat-area">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        role   = msg["role"]
        content = msg["content"]
        if role == "user":
            st.markdown(f"""
            <div class="msg-row user">
              <div class="msg-bubble user">{content}</div>
              <div class="msg-avatar user-av">👤</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.container():
                st.markdown(f"""
                <div class="msg-row assistant">
                  <div class="msg-avatar ai-av">⚡</div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(content)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Input area ─────────────────────────────────────────────────────────
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Optional code paste
    with st.expander("📎 Paste code snippet (optional)", expanded=False):
        code_input = st.text_area(
            "Code",
            placeholder="# Paste your code here...",
            height=160,
            label_visibility="collapsed",
            key="code_input",
        )
    code_input = st.session_state.get("code_input", "")

    # Message input
    col_msg, col_btn = st.columns([6, 1], gap="small")

    with col_msg:
        user_msg = st.text_area(
            "Message",
            placeholder=f"Ask anything in {active_cfg['label']} mode…",
            height=80,
            label_visibility="collapsed",
            key="user_input",
        )

    with col_btn:
        st.markdown('<div class="send-btn" style="padding-top:22px;">', unsafe_allow_html=True)
        send = st.button("⚡ Send", key="send_btn", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Clear button
    col_clr, _ = st.columns([1, 5])
    with col_clr:
        if st.button("🗑 Clear chat", key="clear_btn"):
            st.session_state.messages = []
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Send logic ─────────────────────────────────────────────────────────
    if send and user_msg.strip():
        st.session_state.messages.append({"role": "user", "content": user_msg.strip()})

        with st.spinner(f"{active_cfg['icon']} Thinking…"):
            response_chunks = []
            placeholder = st.empty()
            full_response = ""

            try:
                for chunk in route(active, user_msg.strip(), code_input):
                    full_response += chunk
                    placeholder.markdown(full_response + "▌")

                placeholder.markdown(full_response)
                st.session_state.messages.append({
                    "role":    "assistant",
                    "content": full_response,
                })
            except Exception as exc:
                err_msg = f"⚠️ **Error calling Grok API:** `{exc}`\n\nPlease check your API key in `config.py`."
                placeholder.markdown(err_msg)
                st.session_state.messages.append({
                    "role":    "assistant",
                    "content": err_msg,
                })

        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)  # main-content