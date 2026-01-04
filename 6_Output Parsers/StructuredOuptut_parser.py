from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0.5)


# Create Schema
schema = [
        ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
        ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
        ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
        ]

parser = StructuredOutputParser.from_response_schemas(schema)

# Prompt
template1 = PromptTemplate(
            template ='Give me 3 facts about {topic} \n {format_instructions}',
            input_variables=['topic'],
            partial_variables={'format_instructions': parser.get_format_instructions()}
            )

# prompt = template1.invoke({'topic':"Black Hole"})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template1 | model | parser
result = chain.invoke({'topic':"Black Hole"})

print(result)
print(type(result))