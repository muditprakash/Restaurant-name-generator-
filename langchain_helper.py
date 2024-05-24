from langchain_google_genai import GoogleGenerativeAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from secret_key import google_key
 

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_key, temperature=0.6)

def get_resturant_name_and_items (cuisine):

        prompt_template_name=PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a resturent for {cuisine} food suggest me a fancy name for this just one name"
    )
        name_chain = LLMChain(llm=llm , prompt=prompt_template_name , output_key="resturant_name")
        prompt_template_items=PromptTemplate(
        input_variables=["returant_name"],
        template="Suggest me some meny items for {resturant_name} return it as comma seperated list and don't include {resturant_name} in this list"
    )
        food_item_chain = LLMChain(llm=llm,prompt=prompt_template_items, output_key="menu_items")
        
        chain =  SequentialChain(
                chains = [name_chain,food_item_chain],
                 input_variables = ['cuisine'],
                 output_variables = ["resturant_name","menu_items"]
                 )
        response =chain({'cuisine':cuisine})

        return response

if __name__=="__main__":
        print(get_resturant_name_and_items("Italian"))
