from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0.5)

# Create Schema
class Person(BaseModel):

    name : str = Field(description="Name of the person")
    age : int = Field(gt=18, description="Age of the person")
    city : str = Field(description="City of the person")


parser = PydanticOutputParser(pydantic_object=Person)

template1 = PromptTemplate(
                template ='Generate the name,age,city of a fictional {place} character\n {format_instructions}',
                input_variables=['place'],
                partial_variables={'format_instructions': parser.get_format_instructions()}
                )

# prompt = template.invoke({'place':"Indian"})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template1 | model | parser
result = chain.invoke({'place':"Indian"})

print(result)