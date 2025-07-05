from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from rag import load_vectorstore
import os
from dotenv import load_dotenv

load_dotenv()
def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-05-20",
        temperature=0.2,
        convert_system_message_to_human=True,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

def build_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    prompt_template = PromptTemplate.from_template("""
                        You are a helpful and factual AI assistant specializing in medical information.

                        Use only the provided context to answer the user’s question. Do NOT use any prior knowledge. If the context does not contain the answer, say you don't know.

                        For every paragraph, add a citation to the source like this: [filename.pdf, Page X].

                        At the end of your response, include a list of all sources used in the format:
                        

                        ---

                        Context:
                        {context}

                        Question: {question}

                        Answer:
                        """)
    llm = load_llm()
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt_template}
    )
