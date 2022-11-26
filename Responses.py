from datetime import datetime
import pyttsx3
from PyDictionary import PyDictionary


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message == 'women':
        return 'Ha Ha Ha'

    return PyDictionary().meaning(user_message)