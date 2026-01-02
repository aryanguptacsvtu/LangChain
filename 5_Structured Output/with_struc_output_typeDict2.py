from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal, List

load_dotenv()

model = ChatGroq(model="gemma2-9b-it")  

# Create Schema 
class Review(TypedDict):

    key_themes : Annotated[list[str], "Key themes discussed in the review in a list"]
    summary : Annotated[str, "A brief summary of the review"]
    sentiment : Annotated[Literal["pos", "neg"], "The sentiment of the review, either positive, negative"]

    pros : Optional[Annotated[list[str], "List of pros mentioned in the review"]]
    cons : Optional[Annotated[List[str], "List of cons mentioned in the review"]]
    name: Annotated[Optional[str], "Write the name of the reviewer,if mentioned "]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
                                 
Review by Aryan Gupta
""")


print(result)
print("\n👉 Type :",type(result))
print("👉 KEY Themes : ",result['key_themes'])
print("👉 Summary : ",result['summary'])
print("👉 Sentiment :",result['sentiment'])
print("\n👉 PROS :",result['pros'])
print("👉 CONS :",result['cons'])
print("👉 Name of Reviewer :",result['name'])