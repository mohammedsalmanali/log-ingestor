from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()

@app.route('/search', methods=['GET'])
def search_logs():
    try:
        query_params = request.args.to_dict()
        result = es.search(index='logs', body={'query': {'match': query_params}})
        hits = result.get('hits', {}).get('hits', [])
        return jsonify({"status": "success", "logs": hits}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3001)
