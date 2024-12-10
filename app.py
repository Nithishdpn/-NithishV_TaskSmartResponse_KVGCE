import streamlit as st
import openai

# Set your OpenAI API key
api_key = "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"
if not api_key:
    st.error("API key for OpenAI is missing. Please set the API key.")
else:
    openai.api_key = api_key

# Title and description
st.title("Harmony Hub: Personalized Music Recommendation 🎵")
st.markdown("Tell us about your music preferences, and our AI will recommend tracks tailored just for you!")

# User input fields
fav_genre = st.text_input("What's your favorite genre?", placeholder="E.g., Pop, Rock, Jazz...")
fav_artist = st.text_input("Who's your favorite artist?", placeholder="E.g., Taylor Swift, Ed Sheeran...")
current_mood = st.text_input("How are you feeling right now?", placeholder="E.g., Happy, Sad, Relaxed...")
preferred_language = st.text_input("What's your preferred language?", placeholder="E.g., English, Spanish, Hindi...")

# Button to fetch recommendations
if st.button("Get Recommendations"):
    if not (fav_genre or fav_artist or current_mood or preferred_language):
        st.error("Please provide at least one preference to get recommendations.")
    else:
        with st.spinner("Fetching personalized music recommendations..."):
            try:
                # Generate recommendations using OpenAI API
                prompt = f"""
                You are a music expert. Based on the following preferences, recommend 5 songs that match them:
                
                - Favorite genre: "{fav_genre}"
                - Favorite artist: "{fav_artist}"
                - Current mood: "{current_mood}"
                - Preferred language: "{preferred_language}"

                If some preferences are missing, base your recommendations on the provided details. 
                Provide the recommendations in a clean list format, with each song on a new line, mentioning the artist and song name.
                """
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # Adjust to your model (e.g., "gpt-3.5-turbo")
                    messages=[
                        {"role": "system", "content": "You are a music recommendation assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.7,
                    max_tokens=300,
                )

                # Extract response text
                recommendations = response.choices[0].message["content"].strip()

                # Display recommendations
                st.subheader("Your Personalized Music Recommendations 🎶:")
                st.text_area("Recommendations:", recommendations, height=200)

            except Exception as e:
                st.error(f"An error occurred: {e}")
