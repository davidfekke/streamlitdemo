import io
import time
from datetime import date, time as dtime
import streamlit as st

st.set_page_config(page_title="Streamlit Widgets Gallery", layout="wide")

st.title("🧰 Streamlit Widgets & Components Gallery")
st.caption(
    "This page showcases most commonly used built‑in Streamlit input widgets, layout helpers, status elements, data display components, and a small session_state demo."
)

# --- Helper functions -------------------------------------------------------

def section(title: str):
    st.markdown(f"## {title}")


def sub(title: str):
    st.markdown(f"### {title}")


def code_note(msg: str):
    st.info(msg, icon="ℹ️")


# --- Session State Demo -----------------------------------------------------
with st.sidebar:
    st.header("Session State Demo")
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    inc = st.button("➕ Increment counter")
    if inc:
        st.session_state.counter += 1
    st.metric("Counter value", st.session_state.counter)
    st.write("Session state keys:", list(st.session_state.keys()))

# --- Basic Inputs -----------------------------------------------------------
section("Basic Input Widgets")
cols = st.columns(3)
with cols[0]:
    if st.button("Primary Button"):
        st.success("Button clicked")
    st.link_button("Open Streamlit Docs", "https://docs.streamlit.io")
    st.download_button(
        "Download sample text",
        data="Hello from Streamlit!\n",
        file_name="sample.txt",
        mime="text/plain",
    )
    chk = st.checkbox("Enable feature")
    tog = st.toggle("Dark mode (demo only)")
    st.write("Checkbox:", chk, "Toggle:", tog)

with cols[1]:
    choice = st.radio("Pick a color", ["Red", "Green", "Blue"], horizontal=True)
    sel = st.selectbox("Select a fruit", ["Apple", "Banana", "Cherry", "Dragonfruit"])
    msel = st.multiselect("Select toppings", ["Cheese", "Mushrooms", "Olives", "Onions"])  # noqa: E501
    st.write("You picked:", choice, sel, msel)

with cols[2]:
    val = st.slider("Slider (0-100)", 0, 100, 25)
    sval = st.select_slider("Select Slider", options=["XS", "S", "M", "L", "XL"], value="M")
    num = st.number_input("Number input", value=3, min_value=0, step=1)
    st.write("Values:", val, sval, num)

# Text inputs
col_a, col_b = st.columns(2)
with col_a:
    txt = st.text_input("Text input", placeholder="Type something...")
    area = st.text_area("Text area", height=100)
with col_b:
    pwd = st.text_input("Password input", type="password")
    st.write("(Hidden)")

# Date & time inputs
col1, col2, col3 = st.columns(3)
with col1:
    d = st.date_input("Date", value=date.today())
with col2:
    t = st.time_input("Time", value=dtime(12, 30))
with col3:
    # datetime_input introduced in Streamlit 1.31.0; fallback for earlier versions.
    try:
        dt = st.datetime_input("DateTime", value=None, step=60)
    except Exception:  # pragma: no cover
        dt = None
        st.caption("datetime_input not available in this version")

st.write("Date:", d, "Time:", t, "DateTime:", dt)

# File & Media inputs
colf, colc, colcam = st.columns(3)
with colf:
    up = st.file_uploader("Upload a file", type=["txt", "csv", "png", "jpg"])  # noqa: E501
    if up is not None:
        st.success(f"Uploaded: {up.name} ({up.size} bytes)")
with colc:
    color = st.color_picker("Color picker", value="#4CAF50")
    st.write("Picked color:", color)
with colcam:
    try:
        pic = st.camera_input("Take a picture")
        if pic is not None:
            st.image(pic)
    except Exception:
        st.caption("camera_input not supported here")

# --- Forms ------------------------------------------------------------------
section("Forms")
with st.form("profile_form"):
    st.write("Form groups widgets. Submission triggers a rerun once.")
    fname = st.text_input("First name")
    age = st.number_input("Age", 0, 120, 30)
    newsletter = st.checkbox("Subscribe to newsletter")
    submitted = st.form_submit_button("Submit form")

if submitted:
    st.success(f"Submitted: {fname=}, {age=}, {newsletter=}")

# --- Layout helpers ---------------------------------------------------------
section("Layout Helpers")
col_l, col_r = st.columns([1, 2])
with col_l:
    st.write("Inside first column")
with col_r:
    with st.expander("Click to expand details"):
        st.write("This content is hidden until expanded.")
        st.code("st.expander('Title')")

# Tabs
try:
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Charts"])
    with tab1:
        st.write("Content for Tab 1")
    with tab2:
        st.write("Content for Tab 2")
    with tab3:
        st.write("Chart examples below")
except Exception:
    st.caption("Tabs not supported in this version")

# Container example
with st.container():
    st.write("This is inside a generic container.")

# Sidebar already used for session state.

# --- Data Display -----------------------------------------------------------
section("Data & Display Components")

import numpy as np  # noqa: E402

try:
    import pandas as pd  # noqa: E402
except Exception:  # pragma: no cover
    pd = None

arr = np.random.randn(5, 3)
st.write("st.write auto-detects types:", arr)
st.table(arr)
st.dataframe(arr)

if pd is not None:
    df = pd.DataFrame(arr, columns=list("ABC"))
    st.data_editor(df, num_rows="dynamic")
    st.json(df.describe().to_dict())
else:
    st.warning("pandas not installed; skipping DataFrame examples")

st.code("print('Hello, world!')", language="python")

# Metric & progress
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Revenue", "$10K", "+5%")
with col_m2:
    st.metric("Users", "1,245", "+56")
with col_m3:
    st.metric("Churn", "2.3%", "-0.4%")

progress_demo = st.empty()
bar = progress_demo.progress(0, text="Progress demo")
for i in range(0, 101, 10):
    time.sleep(0.05)
    bar.progress(i, text=f"Progress: {i}%")
progress_demo.empty()

# Charts (fallback if libs missing)
try:
    import altair as alt  # noqa: E402
except Exception:
    alt = None

if alt and pd is not None:
    chart_df = pd.DataFrame({"x": list(range(10)), "y": np.random.randn(10)})
    st.altair_chart(alt.Chart(chart_df).mark_line(point=True).encode(x="x", y="y"), use_container_width=True)  # noqa: E501
else:
    st.caption("Altair or pandas not available; skipping altair chart.")

# Images / media
try:
    from PIL import Image  # noqa: E402
    img = Image.new("RGB", (150, 80), color=(76, 175, 80))
    st.image(img, caption="Generated image (PIL)")
except Exception:
    st.caption("Pillow not installed; skipping image.")

# --- Status / Feedback ------------------------------------------------------
section("Status & Feedback")
st.success("Success message")
st.info("Info message")
st.warning("Warning message")
st.error("Error message")

with st.status("Running fake task", expanded=False) as status:
    st.write("Step 1")
    time.sleep(0.2)
    st.write("Step 2")
    time.sleep(0.2)
    status.update(label="All done!", state="complete", expanded=False)

st.toast("A quick toast notification", icon="✅")

col_fx1, col_fx2 = st.columns(2)
with col_fx1:
    if st.button("🎈 Balloons"):
        st.balloons()
with col_fx2:
    if st.button("❄️ Snow"):
        st.snow()

# --- Chat components (simple echo) -----------------------------------------
section("Chat Components")
chat_placeholder = st.container()
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Hi! Ask me something (I just echo)."}
    ]

for m in st.session_state.chat_messages:
    with chat_placeholder.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input("Type a message")
if prompt:
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    st.session_state.chat_messages.append({"role": "assistant", "content": f"You said: {prompt}"})
    st.experimental_rerun()

# --- Final notes ------------------------------------------------------------
section("Notes")
st.markdown(
    "- Some widgets (camera_input, datetime_input, status) depend on your installed Streamlit version and environment.\n"
    "- Optional libraries (pandas, altair, pillow) are used when present.\n"
    "- Feel free to copy sections into your own app as needed."
)
