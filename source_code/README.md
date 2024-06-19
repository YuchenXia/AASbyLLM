This folder contains the simplified source code for reproducibility, taking into account the copyright restrictions of external libraries used in the RAG mechanism. These libraries have been excluded without significantly affecting functionality.

## Live Prototype

For research purpose, a more complete version is currently hosted at [https://aasbyllmappv16-yawjvp4zbq-ew.a.run.app](https://aasbyllmappv16-yawjvp4zbq-ew.a.run.app). Please note that it might take between 30 seconds to 2 minutes for the elastic server system to boot up.

The server automatically shuts down after being idle for 10 minutes and clears all the data.

## Installation
To set up the project locally, follow these steps:

1. Download the code and open with IDE, **python 3.9** is recommended for the environment.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app.py after you integrating an LLM to the model, this can be simply done by using an LLM API, for example, a GPT3.5 model from OpenAI:
   
   create an *.env* file at the project folder and add your OpenAI API key in it.
   ```
   in .env:
   OPENAI_API_KEY="your_key_here"
   ```
4. run app.py
