import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello_world():
  args = request.args
  lang = args.get("extensionPrompt")

  if lang=='French':
      json_response = {"extensionOutput": "bonjour"}
  elif lang=='Spanish':
      json_response = {"extensionOutput": "hola"}
  else:
      json_response = {"extensionOutput": "hello"}
  return json.dumps(json_response)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
