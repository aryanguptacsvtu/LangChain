from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_groq import ChatGroq

load_dotenv()

st.header("Research Tool")
model = ChatGroq(model="gemma2-9b-it", temperature=0)

# user_input = st.text_input("Enter your prompt :")  # STATIC Prompt


paper_input = st.selectbox( "👉 Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "👉 Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "👉 Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# DYNAMIC Prompt :-
template = PromptTemplate(   template='''
                            "\nPlease summarize the research paper titled \"{paper_input}\" with the following specifications:
                            \nExplanation Style: {style_input}  \nExplanation Length: {length_input}  \n
                          
                            1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.\n
                            2. Analogies:  \n   - Use relatable analogies to simplify complex ideas.  \n
                            
                            If certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  \n
                            Ensure the summary is clear, accurate, and aligned with the provided style and length.'''
                         )

input_variables = ['paper_input','style_input','length_input']


# Fill the Placeholders
prompt = template.invoke({  'paper_input':paper_input,
                            'style_input':style_input,
                            'length_input':length_input
                        })

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result)

