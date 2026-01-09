from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0)
parser = StrOutputParser()

prompt1 = PromptTemplate(template='Write a joke about topic {topic}',
                        input_variables=['topic'])

prompt2 = PromptTemplate(template='Explain the following joke {text}',
                        input_variables=['text'])

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))

chain.get_graph().print_ascii()