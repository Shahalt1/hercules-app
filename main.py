import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="TestZeus Hercules",
    page_icon="⚡",
    layout="wide"
)

# Title with Icon
st.markdown("<h1 style='text-align: center;'>⚡ TestZeus Hercules ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Revolutionize your testing with Gherkin-powered automation</p>", unsafe_allow_html=True)

# Main Form
with st.form(key="main-form", clear_on_submit=True):
    st.markdown("### 🚀 Test Input")
    
    st.text_area(
        label="Input Gherkin Feature File",
        height=200,
        help="Paste your Gherkin feature file here for testing.",
        placeholder="""Feature: Text Input Multiline Placeholder
Scenario: Display multiline placeholder for text input
    Given I am on the input form page
    When I focus on the text input field
    Then I should see the following multiline placeholder:
"""
    )
    
    file = st.file_uploader(
        "📂 Upload Test Data",
        type=["txt"],
        help="Upload a text file with test data for execution."
    )
    
    submitted = st.form_submit_button("🚀 Execute Test")

# Output Section
if submitted:
    if file:
        st.success("✅ Test executed successfully! Results are ready to download.")
        st.download_button("📥 Download Test Results", data="Sample Test Results")
    else:
        st.error("❌ Please upload test data to proceed!")

# Sidebar Configuration
st.sidebar.title("⚙️ Configuration")
st.sidebar.markdown("### Select OpenAI Model")

models = [
    "gpt-4o",
    "gpt-4-turbo",
    "gpt-4",
    "Mistral", 
    "Gemini 1.5 Flash"
    "Gemma 2 9B"
    "Llama 3.2 8B"
]
selected_model = st.sidebar.selectbox("Supported Models", options=models, help="""\f Supported AI Models for TestZeus-Hercules\n
\tAnthropic Haiku: Compatible with Haiku 3.5 and above.\n
\tGroq: Supports any version with function calling and coding capabilities.\n
\tMistral: Supports any version with function calling and coding capabilities.\n
\tOpenAI: Fully compatible with GPT-4o and above. Note: OpenAI GPT-4o-mini is not supported.\n
\tOllama: Not supported based on current testing.""")

api_key = st.sidebar.text_input(
    "🔑 OpenAI API Key",
    type="password",
    placeholder="Enter your API Key"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Browser & Execution Parameters")

HEADLESS = st.sidebar.checkbox("Enable Headless Mode", value=True)
RECORD_VIDEO = st.sidebar.checkbox("Record Video")
TAKE_SCREENSHOTS = st.sidebar.checkbox("Take Screenshots")
CAPTURE_NETWORK = st.sidebar.checkbox("Capture Network Logs")
BROWSER_TYPE = st.sidebar.selectbox("Browser Type", ["Chromium", "Firefox", "Safari"])

st.sidebar.markdown("---")

# Features Section
st.markdown("""
## 💡 Features

- **:blue-background[Gherkin-Powered Testing]** : Input Gherkin features, get results effortlessly.
- **:blue-background[Multi-Platform Support]** : Seamless with complex UIs like Salesforce.
- **:blue-background[CI/CD Ready]** : Integrates easily into pipelines with Docker-native builds.
- **:blue-background[Precise and Autonomous]** : Auto-healing, network logs, and video capture.
- **:blue-background[Multilingual]** : Supports diverse teams across the globe.
""")
st.markdown("---")

# Footer
st.markdown(
    "<p style='text-align: center;'>⚡ Powered by TestZeus Hercules. Your one-stop automation testing solution.</p>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; font-size: 20px;'>
        <a href='https://github.com/test-zeus-ai/testzeus-hercules' target='_blank' style='text-decoration: none; color: inherit;'>
            <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' alt='GitHub Logo' style='width: 30px; vertical-align: middle; margin-right: 10px;'>
            <span style='background: linear-gradient(90deg, #b73a3c, #ff8c42); 
                         -webkit-background-clip: text; 
                         -webkit-text-fill-color: transparent;
                         font-weight: bold; 
                         padding: 5px 10px; 
                         border-radius: 10px;'>
                TestZeus Hercules
            </span>
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
