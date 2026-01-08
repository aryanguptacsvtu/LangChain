from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatGroq(model="gemma2-9b-it", temperature=0)
parser = StrOutputParser()

prompt = PromptTemplate(template='Write a joke about topic {topic}',
                        input_variables=['topic'])


joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
                                'joke':RunnablePassthrough(),
                                'wordCount':RunnableLambda(word_count)
                                # 'wordCount':RunnableLambda(lambda x :len(x.split()))
                                 })

final_chain = RunnableSequence(joke_gen_chain ,parallel_chain)

print(final_chain.invoke({'topic':'Cricket'}))

final_chain.get_graph().print_ascii()