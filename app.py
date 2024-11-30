from flask import Flask, render_template, jsonify, request
from utils.nlp_processor import process_documents
from utils.graph_builder import build_graph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    documents = request.form.getlist('documents')
    entities, relationships = process_documents(documents)
    graph_data = build_graph(entities, relationships)
    return jsonify(graph_data)

if __name__ == "__main__":
    app.run(debug=True)
