# Innoquine 🌟

Welcome to Innoquine, your AI-powered design companion transforming interior decor with the intelligence of GPT-4. 🏡✨


## Overview

Innoquine revolutionizes decor by leveraging GPT-4's cutting-edge capabilities. It interprets your space through images and prompts, providing personalized design suggestions for homes, offices, and more. 🎨🤖


## Features

- **AI-Powered Design:** Innoquine uses GPT-4 to offer intelligent and creative design recommendations. 🚀
- **Image Upload:** Upload images of your space to receive personalized decor suggestions. 📸
- **Prompt Interaction:** Share prompts to guide Innoquine in understanding your design preferences. 💬


<br>

## Usage
Image Question
![Alt text](/Innoquine/assets/Image_question.gif)

Textual Question
![Alt text](/Innoquine/assets/Text_question.gif)


Note: Response is not complete in the video as example is shown using 50 tokens.


## Tech Stack

- **Python:** The project is built using the Python programming language.
- **Reflex Framework:** Innoquine utilizes the [Reflex framework](https://reflex.dev/) for seamless and reactive web interactions.

<br>

## Getting Started

1. Clone the repository
```bash
git clone https://github.com/HeetVekariya/Innoquine.git
```

2. Make virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```

3. Navigate to the project directory
```bash
cd Innoquine
``` 

4. Install the dependencies
```bash
pip install -r {path to requirements.txt}
reflex init
```

5. Add your OpenAI GPT-4 API key to the `state.py` file, replace `YOUR_API_KEY` with your API key.
```python
api_key = "YOUR_API_KEY"
```

6. Adjust `max_tokens` according to your API plan in the `state.py` file. Minimum suggested value is `100`. Currently, the app is configured to use `50` tokens per request.
```python
max_tokens = 100
```

7. Run the app
```bash
reflex run
```

### Note: 
- You can skip step 6.
- Must have GPT-4 API key to run the app, you can create [here](https://platform.openai.com/account/api-keys).

<br>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📄

## Acknowledgments

- Thanks to the OpenAI team for the powerful GPT-4 model. 👏
- To get your GPT-4 API key, visit [OpenAI](https://platform.openai.com/account/api-keys). 🔑

## Connect with Me

- [Heet Vekariya](https://www.linkedin.com/in/heet-vekariya-16326024b/)
