from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFaceEndpoint(repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",task = "text-generation")
# model = ChatHuggingFace(llm=llm)


llm = HuggingFaceEndpoint(
                        repo_id="deepseek-ai/DeepSeek-V3.1-Terminus",
                        task="text-generation",
                        max_new_tokens=1024,
                        do_sample=False,
                        repetition_penalty=1.03,
                        provider="auto",  # let Hugging Face choose the best provider for you
                    )

model = ChatHuggingFace(llm=llm)
result = model.invoke("How did Mahatma Gandhi contribute to India's independence movement?")

print(result.content)
