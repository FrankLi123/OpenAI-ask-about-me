import os
import sys
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from flask import Flask,jsonify
from flask_cors import CORS

#1 pip install chromadb, tiktoken
#2 set a envrionment variable named "OPENAI_API_KEY" using export xxxx=xxxx


app= Flask(__name__)


CORS(app, resources={r"/api/*":{"origins:":"http://localhost:3000"}})


# # Define a decorator function to handle CORS headers
# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'  # Replace with your frontend's URL
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'  # Add any other allowed methods
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'  # Add any other allowed headers
#     return response
# app.after_request(add_cors_headers)

@app.route('/api/generator/<input>', methods=['GET'])
def generator(input):

    print("reached here!")
    try:
        query = input
        print(query)

        loader = TextLoader('./personal_info.txt')

        index = VectorstoreIndexCreator().from_loaders([loader])

        answer = index.query(query , llm=ChatOpenAI())
        print("answer is \n")
        print(answer)
        return jsonify({'result': answer})

    except Exception as e:
        print("the error is : ", e)
        return jsonify({'error':"Internal Server error"})

if __name__ == '__main__':
    app.run(debug=True)