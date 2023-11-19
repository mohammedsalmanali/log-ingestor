from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()

@app.route('/ingest', methods=['POST'])
def ingest_log():
    try:
        log_data = request.get_json()
        es.index(index='logs', body=log_data)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)
