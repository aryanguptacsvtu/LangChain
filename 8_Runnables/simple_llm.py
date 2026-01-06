from langchain_core.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(model="llama2")

# Create a Prompt Template
prompt = PromptTemplate(
    template = "Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

# Define the input
topic = input("Enter the topic :")

# Format the prompt manually using Prompt Template
formatted_output = prompt.format(topic=topic)

# Call the llm directly 
blog_title = llm.predict(formatted_output)

# Predict the output 
print("Generated Blog Title : ", blog_title)