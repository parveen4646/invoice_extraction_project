
import os
from sysconfig import get_python_version
import cv2

import matplotlib.pyplot as plt

from IPython.display import Image
import pytesseract
import re
import openai
import json
from dotenv import load_dotenv
load_dotenv()



openai.api_key = os.getenv("OPENAI_API_KEY")



img=cv2.imread('/Users/parveensharma/Desktop/invoice_sample.png')


plt.figure(figsize=(10,8))
plt.imshow(img)



def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(img)
    return text
    
   

def extract_data(text):
    message = [
        {'role': 'system', 'content': 'you are an helping assistant,expert in extracting data from invoices'},
        {'role': 'user', 'content': f'1.extract all the information from invoice >>>{text}<<< . give the outputin a json format'}
    ]

    response = openai.ChatCompletion.create(messages=message, model='gpt-3.5-turbo')

    df=response.choices[0].message['content']
    data_dict=json.loads(df)
    return data_dict


def invoice(image):
    text=extract_text_from_image(image)
    data_jason=extract_data(text)
    print(data_jason)
    return data_jason


# 
invoice('/Users/parveensharma/Desktop/invoice_sample.png')




#

