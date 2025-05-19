from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq  import  ChatGroq
import os 
from dotenv import load_dotenv

# helps to create apis 
from langserve import add_routes
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Initializing the groq model
groq_model = ChatGroq(
    model="Gemma2-9b-It",
    groq_api_key=groq_api_key,
)


#Create a prompt template
system_template="Translate the following into {language}:"
prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)

# Creating the output parser
output_parser = StrOutputParser()

## Crate the chain

chain=prompt_template | groq_model | output_parser


#App definition

app = FastAPI(
    title="LangChain Groq API",
    description="A simple API for LangChain Groq model",
    version="1.0",
)


# adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1", port=8000) 
