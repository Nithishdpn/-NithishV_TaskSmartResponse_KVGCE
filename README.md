It takes user input as structured data through a text area in the Streamlit interface, allowing the user to input project details.
The data is then processed by Google’s generative AI model (gemini-1.5-flash) to generate a professional email based on the input.
The email content is displayed for the user to review in the Streamlit interface.
It generates a custom "mailto" link that allows the user to send the generated email directly via Gmail.
It provides a button styled with custom CSS, which, when clicked, opens the Gmail compose window with the generated email content.


I faced a problem while using the OpenAI API for email generation. The free access limits were exceeded, and I had to submit the project to the client within the deadline. To ensure the project was completed on time, I decided to switch to the Gemini AI API

Run the Script : streamlit run app.py
