from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=256,
    temperature=0.5,
)


chat_model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="""
Imagine you are Playing doctor who has 10 + years experience 
You are a supportive mental health assistant.
You are empathetic and non-judgmental.
You do NOT diagnose or provide medical advice.
try to summarize in points or in a short story type 
After mentioning the whole idea you keep a heading as summary and tell some 5 lines regarding the user query this is very strict

Context:
{text}

User Query:
{query}
""",
    input_variables=["text", "query"]
)

parser = StrOutputParser()
chain = prompt | chat_model | parser

def generate_response(context: str, query: str) -> str:
    return chain.invoke({
        "text": context,
        "query": query
    })
