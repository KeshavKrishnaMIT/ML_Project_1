from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load Bollywood movies dataset
movies_df = pd.read_csv("Top 1000 Bollywood Movies and their boxoffice.csv")
movies_df = movies_df[['Movie','Worldwide','Budget','India Net','India Gross','Overseas']]
movies_df = movies_df.dropna()
movies_df.rename(columns={
    'Movie':'movie_name',
    'India Net':'India_Net',
    'India Gross':'India_Gross'
}, inplace=True)

def get_verdict(row):
    try:
        ratio = row['Worldwide'] / row['Budget']
    except:
        ratio = 0
    if ratio < 1:
        return 'Flop'
    elif 1 <= ratio < 1.5:
        return 'Average'
    elif 1.5 <= ratio < 2:
        return 'Hit'
    elif 2 <= ratio < 3:
        return 'Superhit'
    else:
        return 'Blockbuster'

@app.route("/")
def home():
    movies_list = movies_df.to_dict(orient='records')
    return render_template("index.html", movies_list=movies_list)

if __name__ == "__main__":
    app.run(debug=True)

