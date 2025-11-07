from langchain_community.document_loaders import TextLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline

load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Step 1: Create the Hugging Face pipeline object.
# This is where you specify the task, model, and generation parameters.
pipe = pipeline(
    task="text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature=0.5,
    max_new_tokens=500
)

# Step 2: Pass the pipeline object to the HuggingFacePipeline class.
# This class's job is just to be a wrapper around the existing pipeline.
llm = HuggingFacePipeline(
    pipeline=pipe
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader(r"E:\RAG\cricket.txt", encoding="utf-8")

docs = loader.load()

# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem":docs[0].page_content}))