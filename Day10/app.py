from flask import Flask, render_template, request, jsonify
from langchain.chains import LLMChain  # Updated import
from langchain_core.prompts import PromptTemplate  # Updated import
#from langchain_community.llms import MistralAI
from langchain_mistralai import ChatMistralAI
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

mistral_api_key = "YOUR_MISTRAL_API_KEY"
llm = ChatMistralAI(api_key=mistral_api_key)

prompt_template = PromptTemplate(
    input_variables=["query"],
    template="You are a helpful assistant. Answer the following question: {query}"
)


chain = LLMChain(llm=llm, prompt=prompt_template)


conversation_history = []

@app.route("/")
def home():
    return render_template("index.html", history=conversation_history)

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.form["query"]
    
   
    response = chain.run(query=user_query)
    
    
    conversation_history.append({"query": user_query, "response": response})
    
    return jsonify({"response": response, "history": conversation_history})

if __name__ == "__main__":
    app.run(debug=True)