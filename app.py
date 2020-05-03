from flask import Flask, render_template, request
import numpy as np
from src import sudoku_solver_bactracking 

app = Flask(__name__)

grid = []

@app.route('/')
def home():
    global grid

    return render_template('index.html')

@app.route('/generate')
def generate():
    global grid
    level=request.args.get('level', default=1, type=int)
    grid = sudoku_solver_bactracking.generate(level=level)
    grid = grid.tolist()

    if level == 1:
        level = 'Easy'
    elif level == 2:
        level = 'Medium'
    elif level == 3:
        level = 'Hard'
    else :
        level = 'Insane'

    return render_template('index.html', grid=grid, level=level)


@app.route('/solve',methods = ['POST', 'GET'])
def solve():
    global grid
    grid = sudoku_solver_bactracking.solve(np.matrix(grid))
    grid = grid.tolist()
    return render_template('index.html', grid=grid)


@app.route('/verify',methods = ['POST', 'GET'])
def verify():
    global grid
    result = sudoku_solver_bactracking.verify(np.matrix(grid))
    return render_template('result.html', result=result)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 