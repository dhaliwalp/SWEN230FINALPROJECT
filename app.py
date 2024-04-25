from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    stats_df = pd.read_excel('nba_player_data.xlsx')
    stats_data = stats_df.to_dict('records')
    return render_template('index.html', stats=stats_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)