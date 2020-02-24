from flask import Flask, render_template, request
from Summarization import text_summary

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        get_data = request.form['news']
        summary=text_summary(get_data)

        data= {
            'summary': summary
        }

        return render_template('index.html', data=data)
    else:
        return render_template('index.html',data=[])


if __name__ == "__main__":
    app.run(debug=True)
