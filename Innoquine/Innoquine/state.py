import reflex as rx
import requests
from typing import Dict, List
import base64
from PIL import Image

class AppState(rx.State):
    messages: List[Dict[str, str]] = []
    img: list[str] = []
    input_txt: str = ""
    encoded_images: str = ""

    def send_message(self, message):
        if len(self.input_txt) == 0:
            return
        
        # check if encoded images exists
        if len(self.encoded_images) == 0:
            instruction = "Act as a Home & Office decor assistance.\nYou are provided with the user question below, so provide accurate answer.\n"

            combined_message = instruction + "\n\nUser input:\n" + message
        else:
            instruction = "Act as a Home & Office decor assistance.\nYou have provided with message from user and an encoded image, so decode the image (Do not explain the image until user asks for it) and directly give the answer to question."

            combined_message = instruction + "\n\nUser input:\n" + message + "\n\nEncoded Image:\n" + f"data:image/jpeg;base64,{self.encoded_images}"

        self.messages.append({"user": "You", "text": message})

        # OpenAI API call
        api_key = "YOUR_API_KEY"
        endpoint = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "gpt-4-vision-preview", 
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": combined_message},
                    ],
                }
            ],
            "max_tokens": 50,
        }
        response = requests.post(endpoint, headers=headers, json=data).json()
        print(response)
        self.messages.append({"user": "Assistant", "text": response['choices'][0]['message']['content']})


    async def handle_upload_and_message(
        self, files: list[rx.UploadFile]
    ):
        self.img = []

        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

            # Encode the image
            image_path = f".web/public/{file.filename}" 
            encoded_image = self.encode_image(image_path)
            self.encoded_images += f"{encoded_image}\n"

        

    def encode_image(self, image_path):
        # resize the image
        image = Image.open(image_path)
        image = image.resize((256, 256))
        image.save(image_path)

        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            
        return encoded_string
    
    def on_load(self):
        self.reset()