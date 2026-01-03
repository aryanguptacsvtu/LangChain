from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0.5)

parser = JsonOutputParser()

# 1st Prompt
template1 = PromptTemplate(
            template ='Give me 5 facts about {topic} \n {format_instructions}',
            input_variables=['topic'],
            partial_variables={'format_instructions': parser.get_format_instructions()}
            )

# prompt = template1.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)


chain = template1 | model | parser

result = chain.invoke({'topic':"Black Hole"})

print(result)
print(type(result))