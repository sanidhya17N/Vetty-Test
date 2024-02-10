from flask import Flask, render_template, request
app = Flask(__name__)

def get_file():
    try:
        # Get file , default to file1.txt
        file_name = request.args.get('file_name', 'file1.txt')

        # Read content of file
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

if __name__ == '__main__':
    app.run(debug=True)
