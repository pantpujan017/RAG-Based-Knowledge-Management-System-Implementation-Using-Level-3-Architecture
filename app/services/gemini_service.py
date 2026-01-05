# services/gemini_service.py  (rename this file)
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os

class GeminiService:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        
        # Initialize Gemini models
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=self.api_key,
            temperature=0.7,
            max_output_tokens=2048
        )
        
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=self.api_key
        )
        
        # Create QA chain
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self):
        prompt_template = """Use the following context to answer the question.
        If you don't know the answer, say "I don't have enough information."
        
        Context: {context}
        Question: {question}
        
        Answer:"""
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(),
            chain_type_kwargs={"prompt": prompt}
        )

    def get_response(self, question):
        """Get response from Gemini using RAG"""
        try:
            result = self.qa_chain.run(question)
            return result
        except Exception as e:
            return f"Error generating response: {str(e)}"