from langchain_core.prompts import PromptTemplate

template = PromptTemplate(  template='''
                            "\nPlease summarize the research paper titled \"{paper_input}\" with the following specifications:
                            \nExplanation Style: {style_input}  \nExplanation Length: {length_input}  \n
                          
                            1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  \n
                            2. Analogies:  \n   - Use relatable analogies to simplify complex ideas.  \n
                          
                            If certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  \n
                            Ensure the summary is clear, accurate, and aligned with the provided style and length.'''
                         )

template.save('template.json')