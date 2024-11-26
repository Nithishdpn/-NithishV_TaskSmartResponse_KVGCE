import streamlit as st
import google.generativeai as genai
import os
from urllib.parse import quote
 
api_key = "AIzaSyD06QicT-sfVtlzEKaOgtYulX5ovgicfAQ"    
if not api_key:
    st.error("API key for Google Generative AI is missing. Please set the environment variable 'GOOGLE_GENAI_API_KEY'.")
else:
    genai.configure(api_key=api_key)

 
GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 500,
}

 
st.title("Custom Email Generator")

 
st.markdown("### Input Structured Data:")
user_input = st.text_area(
    "Paste the structured data (as shown in the example) below:",
    height=300,
    placeholder=(
        "From Name: Jesna\n"
        "Client First Name: Geminas\n"
        "Client Last Name: Ket\n"
        "Client Email: GeminasKet@gmail.com\n"
        "Client Country: Romania\n"
        "Client Location (if provided): Romania\n"
        "Project Type: Content with Databases\n"
        "Service Category: Web Development\n"
        "Client Website (if any): No\n"
        "Additional Information (if any):\n"
        '"I need 4 dynamic pages for a real estate web-application: one each for apartments, '
        'houses, business centres, and land. I need 2 filters for "for sale" and "for rent", '
        'and they should be connected. Don\'t bother with the design; I\'ll handle that. '
        'I just need the functionality. The budget should be $100000. Thank you!"'
    ),
)
 
if st.button("Generate Output"):
    if user_input.strip() == "":
        st.error("Please provide structured input before generating the output.")
    else:
        with st.spinner("Generating professional email content..."):
            try:
                
                prompt = f"""
                You are a professional assistant. Generate a polite and professional email response based on the following structured data.
                Remove placeholders like '[Your Company Name/Title]' and '[Your Contact Information]', avoid using bullet points or stars (*), and format it cleanly for an email client.
                
                Input data:
                {user_input}
                
                Make sure to end the email with 'Sincerely, Jesna' as the signature, and avoid adding any other placeholders like '[Your Name]', '[Your Title]', '[Your Company Name]', '[Your Phone Number]', or '[Your Email Address]'.
                """

                 
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config=GENERATION_CONFIG,
                )
                chat_session = model.start_chat(history=[])
                response = chat_session.send_message(prompt)

                
                output = response.text.strip()

                 
                st.subheader("Generated Email Content:")
                st.text_area("Output:", output, height=300)

                 
                subject = "Re: Web Application Development Inquiry"
                body = f"Dear Geminas Ket,\n\n{output}\n\nSincerely,\nJesna"
                mailto_link = f"mailto:?subject={quote(subject)}&body={quote(body)}"

                
                st.markdown(f"""
                    <style>
                        .send-button {{
                            background-color: white;
                            border: 2px solid red; /* Red border */
                            color: black;
                            padding: 10px 20px;
                            font-size: 16px;
                            border-radius: 5px;
                            text-align: center;
                            cursor: pointer;
                            text-decoration: none;
                            font-weight: bold;
                            transition: all 0.3s ease;
                        }}
                        .send-button:hover {{
                            color: red; /* Red text on hover */
                            border-color: red; /* Red border on hover */
                            background-color: white;
                        }}
                    </style>
                    <a href="{mailto_link}" class="send-button" target="_blank">Send via Gmail</a>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {e}")
