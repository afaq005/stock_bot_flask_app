from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    print("inside flask file")
    gdown.download('https://drive.google.com/file/d/1o8TAPB2AvaIvn9_4TcA39ukI48j0uYR5/view?usp=drive_link', 'colab.ipynb', quiet=True)
    return jsonify(message='colab notebook ran successfully')


if __name__ == '__main__':
    print("Runing main file")
    app.run()')
