from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

llm = OpenAI(model="gpt-3.5-turbo")

# Create a Prompt Template
prompt = PromptTemplate(
    template = "Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

# Define the input
topic = input("Enter the topic :")

# Create a LLM Chain
chain = LLMChain(llm=llm , prompt=prompt)

# Call the llm directly 
blog_title = chain.run(topic)

# Predict the output 
print("Generated Blog Title : ", blog_title)