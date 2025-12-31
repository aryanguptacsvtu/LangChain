from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

from langchain_groq import ChatGroq

load_dotenv()
model = ChatGroq(model="gemma2-9b-it", temperature=0)
st.header("Research Tool")

# user_input = st.text_input("Enter your prompt :")  # STATIC Prompt


paper_input = st.selectbox( "👉 Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "👉 Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "👉 Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# DYNAMIC Prompt :-

input_variables = ['paper_input','style_input','length_input']

template = load_prompt('template.json')


if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({ 'paper_input':paper_input,
                            'style_input':style_input,
                            'length_input':length_input
                        })
    
    st.write(result.content)



# Why use PromptTemplate over f-strings?

# 1. "Default Validation" :-
# input_variables = ['paper_input','style_input', validate_template=True]  {Gives an Error}
# input_variables = ['paper_input','style_input','length_input','address', validate_template=True]  {Gives an Error}

# 2."Reusable" :-
# template = load_prompt('template.json')

#3. "Langchain Ecosystem" :-   
# chain = template | model

