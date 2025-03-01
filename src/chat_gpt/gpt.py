import openai 
import requests
from bs4 import BeautifulSoup


#barcode = "3017620422003"


#function to get the response from the model
def get_gpt_response(barcode):
    # Set your OpenAI API key
    openai.api_key='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'
    #openai.api_key = st.secrets["api_key"]
    
    # Get the product information from the OpenFoodFacts API
    url = f"https://world.openfoodfacts.org/product/{barcode}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    
    # Prompt the model with the product information
    prompt = f"analyse this product and  give me some specific and the best insights regarding the healthiness of the product, return just 3 specific bullet points:\n\n{text[:4000]}"
    
    # Get the response from the model
    response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a nutrition expert reviewing a product."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=250

    )
    return response.choices[0].message.content

#print(get_gpt_response(barcode))
