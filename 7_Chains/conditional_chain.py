from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)
parser1 = StrOutputParser()

# Create Schema
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"]= Field(description="Sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(template='Classify the sentiment of the following text into positive or negative\n{feedback}\n{format_instructions}',
                         input_variables=["feedback"],
                         partial_variables={"format_instructions": parser2.get_format_instructions()})

prompt2 = PromptTemplate(template="Write an appropriate response to this positive feedback\n{feedback}",
                         input_variables=["feedback"])

prompt3 = PromptTemplate(template="Write an appropriate response to this negative feedback\n{feedback}",
                         input_variables=["feedback"])


classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
                            (lambda x: x.sentiment == "positive", prompt2 | model | parser1),
                            (lambda x: x.sentiment == "negative", prompt3 | model | parser1),
                            RunnableLambda(lambda x: "No valid sentiment detected")  # Default case
                            )

final_chain = classifier_chain | branch_chain
result = final_chain.invoke({"feedback": "The product quality is excellent and I am very satisfied with my purchase."})
print(result)

final_chain.get_graph().print_ascii()