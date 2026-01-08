from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="gemma2-9b-it", temperature=0)
parser = StrOutputParser()

prompt1 = PromptTemplate(template='Write a detailed report on {topic}',
                        input_variables=['topic'])

prompt2 = PromptTemplate(template='Summarize the following text \n{text}',
                        input_variables=['text'])


report_gen_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
                        (lambda x : len(x.split())>300 ,RunnableSequence(prompt2,model,parser)),
                        RunnablePassthrough()
                        )

final_chain = RunnableSequence(report_gen_chain ,branch_chain)

print(final_chain.invoke({'topic':'Cricket'}))

final_chain.get_graph().print_ascii()