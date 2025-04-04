import google.generativeai as genai
from google.generativeai.types import ContentType
from PIL import Image
from IPython.display import Markdown
import time
import cv2

GOOGLE_API_KEY = 'AIzaSyDj3_DitgO6rJ17xdww8ncB9vCSVYRonWk'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')


def gemini(prompt):
    response = model.generate_content(prompt)
    return response

