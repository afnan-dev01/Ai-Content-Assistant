import streamlit as st
from groq import Groq

# Page Configuration
st.set_page_config(page_title="AI Content Assistant", page_icon="✨", layout="centered")

st.title("✨ AI Content Assistant")
st.write("Generate tailored posts with captions and hashtags powered by Groq AI.")

# Sidebar for API Key input
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Groq API Key", type="password", help="Get your free key at https://console.groq.com")

# Dropdowns and Options
col1, col2 = st.columns(2)

with col1:
    content_type = st.selectbox(
        "Content Type",
        ["Social Media Post", "Educational Tip", "Product Announcement", "Opinion / Thought Leadership", "Storytelling"]
    )
    
    platform = st.selectbox(
        "Platform",
        ["LinkedIn", "Twitter / X", "Instagram", "Facebook", "Threads"]
    )

with col2:
    tone = st.selectbox(
        "Tone of Voice",
        ["Professional", "Casual & Friendly", "Persuasive", "Humorous", "Inspirational", "Informative"]
    )

    model_choice = st.selectbox(
        "Select Model",
        ["openai/gpt-oss-120b", "openai/gpt-oss-120b"]
    )

topic = st.text_input("Topic", placeholder="e.g., The benefits of morning walks for developers")
target_audience = st.text_input("Target Audience", placeholder="e.g., Software Engineers, Remote Workers")

# Generation Logic
if st.button("Generate Content", type="primary"):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar to proceed.")
    elif not topic or not target_audience:
        st.warning("Please fill in both Topic and Target Audience.")
    else:
        with st.spinner("Writing your post..."):
            try:
                # Initialize Groq client
                client = Groq(api_key=api_key)

                # Construct Prompt
                prompt = f"""
                You are an expert content creator. Write a high-converting post tailored to the following specifications:
                
                - **Content Type**: {content_type}
                - **Platform**: {platform}
                - **Topic**: {topic}
                - **Target Audience**: {target_audience}
                - **Tone**: {tone}
                
                **Requirements**:
                1. Adapt formatting (emojis, line breaks, structure) specifically for {platform}.
                2. Write a captivating hook in the first sentence.
                3. Include a relevant Call to Action (CTA) at the end.
                4. Provide 5–8 highly relevant hashtags matching the platform style.
                """

                # Call Groq API
                response = client.chat.completions.create(
                    model=openai/gpt-oss-120b,
                    messages=[
                        {"role": "system", "content": "You are a professional social media content assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )

                generated_text = response.choices[0].message.content

                # Output Display
                st.success("Post generated successfully!")
                st.subheader("Your Post")
                st.markdown(generated_text)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
