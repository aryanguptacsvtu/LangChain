from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGroq(model="gemma2-9b-it")  

# Create Schema 
class Review(TypedDict):
    summary : str
    sentiment : str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.""")

print(result)
print("👉 Type :",type(result))
print("👉 Summary : ",result['summary'])
print("👉 Sentiment :",result['sentiment'])