import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 111)    # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # use 0 for men
engine.setProperty('pitch', 69)  # to set pitc
# Prompt the user to enter text
user_input = input("Enter text to speak: ")

# Convert text to speech
engine.say(user_input)

# Wait for the speech to finish
engine.runAndWait()