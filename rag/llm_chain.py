# from langchain.chains import ConversationalRetrievalChain
# from langchain.llms import HuggingFacePipeline
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
# import torch
# from rag import load_vectorstore

# def load_llm():
#     model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
#     tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=True)
#     model = AutoModelForCausalLM.from_pretrained(
#         model_id,
#         torch_dtype=torch.float16,
#         device_map="auto",
#         trust_remote_code=True
#     )
#     pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)
#     return HuggingFacePipeline(pipeline=pipe)

# def build_chain():
#     vectorstore = load_vectorstore()
#     retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
#     llm = load_llm()
#     return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, return_source_documents=True)


from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from rag import load_vectorstore

def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-05-20",
        temperature=0.2,
        convert_system_message_to_human=True
    )

def build_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = load_llm()
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
