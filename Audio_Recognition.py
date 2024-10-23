import speech_recognition as sr


def record_audio_and_recognize():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Please speak into the microphone...")

        # Adjust the recognizer sensitivity to ambient noise level
        recognizer.adjust_for_ambient_noise(source)

        # Listen for the user's input
        audio = recognizer.listen(source)

        try:
            # Convert speech to text using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except sr.RequestError:
            print("Could not request results; check your network connection")


if __name__ == "__main__":
    record_audio_and_recognize()