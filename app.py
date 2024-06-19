from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    starting_balance = 0
    current_balance = 0
    if request.method == 'POST':
        try:
            starting_balance = float(request.form.get('starting_balance', '0'))
            current_balance = float(request.form.get('current_balance', '0'))
        except ValueError:
            starting_balance = 0  # Default to 0 if input is invalid
            current_balance = 0  # Default to 0 if input is invalid

    # Initialize data for the grid
    rows = 15  # Number of workweeks
    columns = 6  # Total columns including week number
    grid_data = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        grid_data[i][0] = i + 1  # Week number
        if i == 0:
            grid_data[i][1] = starting_balance * 1.03  # Week 1 starts with the starting balance
        else:
            grid_data[i][1] = grid_data[i-1][-1] * 1.03  # Start with the last value of the previous week
        for j in range(2, columns):
            grid_data[i][j] = grid_data[i][j-1] * 1.03  # Increment by 3%

    return render_template('index.html', grid_data=grid_data, starting_balance=starting_balance, current_balance=current_balance)

if __name__ == "__main__":
    app.run(debug=True)
