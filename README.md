# Restaurant-name-generator

Thinking about starting a new restaurant? Choosing a catchy name and a perfect menu can be a very tricky and tiresome task. This application, made with GoogleGenerativeAI, is here to assist you to do this task effectively.

# Technical diagram 
![Capture](https://github.com/muditprakash/Restaurant-name-generator-/assets/75181670/ca4bf3f5-1fac-4e0b-a691-6b47263f1b96)

We are taking input ethnicity via a Streamlit app using the ```sidebar selection method``` and passing it through LangChain's ```SequentialChain``` in order to obtain the restaurant name as well as menu items.
We are using GoogleGenerativeAI's ```text-bison-001 model``` for this project and techniques like``` prompt engineering``` via prompt template to achieve these results.

# Running it locally

clone the repo first 
```
https://github.com/muditprakash/Restaurant-name-generator-.git
```
navigate to `secret_key.py` and put your own api key there. You can read about how to generate your aoi key here :

```
https://ai.google.dev/palm_docs/setup
```
Then install requirements.txt file as 
```
pip install -r requirements.txt
```
And lastly 
```
streamlit run main.py
```

