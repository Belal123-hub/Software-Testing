from flask import Flask, render_template, request
from main import Solution

app = Flask(__name__)
solution = Solution()


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        m = int(request.form['m'])
        n = int(request.form['n'])
        result = solution.uniquePaths(m, n)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)



