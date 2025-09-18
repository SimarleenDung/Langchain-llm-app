from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

import re

load_dotenv()  # loads GOOGLE_API_KEY from .env

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)


def generate_cafe_name_and_items(cuisine, vibe="cozy"):
    """
    Generate a fancy cafe name and a list of menu items
    based on the given cuisine and vibe.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

    # Chain for cafe name
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine", "vibe"],
        template="I want to open a {vibe} cafe that serves {cuisine} food. Suggest only one fancy name for it."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="cafe_name")

    # Chain for menu items
    prompt_template_items = PromptTemplate(
        input_variables=['cafe_name'],
        template="Suggest some menu items for {cafe_name}. Return it as a comma separated list"
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Run the chains
    cafe_name = name_chain.run({"cuisine": cuisine, "vibe": vibe if vibe else "cozy"})
    menu_items = food_items_chain.run({"cafe_name": cafe_name})

    # Convert string to list
    menu_items = [item.strip() for item in menu_items.split(",")]

    return {"cafe_name": cafe_name, "menu_items": menu_items}
