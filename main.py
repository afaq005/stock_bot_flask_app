import subprocess
from flask import Flask, jsonify
import gdown

app = Flask(__name__)

file_url = "https://drive.google.com/uc?export=download&id=1o8TAPB2AvaIvn9_4TcA39ukI48j0uYR5"
output_file = "tradingBot.ipynb"
output_format = "html"
@app.route('/run-colab')
def run_colab():
    print("inside flask file")
    gdown.download(file_url, output_file, quiet=False)
    
    try:
        subprocess.run(["jupyter", "nbconvert", "--execute", "--to", output_format, output_file], check=True)
        return jsonify(message='Colab notebook ran successfully')
    except subprocess.CalledProcessError:
        return jsonify(message='Failed to run Colab notebook')

if __name__ == '__main__':
    print("Running main file")
    app.run()
