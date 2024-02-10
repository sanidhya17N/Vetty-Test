from flask import Flask, render_template, request
import chardet
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_file_content():
    try:
        # Get file name 
        file_name = request.args.get('file_name', 'file1.txt')
        with open(file_name, 'rb') as rawfile:
            result = chardet.detect(rawfile.read())
            encoding = result['encoding']

        # Read content of the specified file with the detected encoding
        with open(file_name, 'r', encoding=encoding, errors='ignore') as file:
            lines = file.readlines()

        # Get start and end line numbers from URL query parameters
        start_line = int(request.args.get('start_line', 1))
        end_line = int(request.args.get('end_line', len(lines)))

        # Validate line numbers
        start_line = max(1, min(start_line, len(lines)))
        end_line = max(start_line, min(end_line, len(lines)))

        # Extract lines based on start and end line numbers
        content = ''.join(lines[start_line-1:end_line])

        # Render HTML page with preserved markup
        return render_template('file_render.html', content=content)

    except Exception as e:
        # Handle exceptions gracefully and display error page with details
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
