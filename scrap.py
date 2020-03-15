import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_data():
    url = 'https://raw.githubusercontent.com/dtandev/coronavirus/master/data/CoronavirusPL%20-%20Timeseries.csv'
    df = pd.read_csv(url, error_bad_lines=False)

    # All infections
    total_cases = df.shape[0]

    count = df['City'].value_counts()
    count_dataframe = pd.DataFrame(count)
    return render_template('get_data.html', data=count_dataframe, total_cases=total_cases)


if __name__ == '__main__':
    app.run(debug=True)
