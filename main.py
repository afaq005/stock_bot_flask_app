from flask import Flask, jsonify
import gdown
from nbconvert import NotebookExecutor
app = Flask(__name__)
file_url = "https://drive.google.com/uc?export=download&id=1o8TAPB2AvaIvn9_4TcA39ukI48j0uYR5"
output_file = "tradingBot.ipynb"
@app.route('/run-colab')
def run_colab():
    print("inside flask file")
    gdown.download(file_url, output_file, quiet=False)
    executor = NotebookExecutor(notebook=output_file)
    executor.run_notebook()
    return jsonify(message='colab notebook ran successfully')


if __name__ == '__main__':
    print("Runing main file")
    
    app.run()
    jsonify(message='Hello')
