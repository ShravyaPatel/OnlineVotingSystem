from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define candidates and initialize results as a dictionary
candidates = {
    'candidate1': 'Candidate One',
    'candidate2': 'Candidate Two',
    'candidate3': 'Candidate Three',
    'candidate4': 'Candidate Four',
    'candidate5': 'Candidate Five'
}

# Initialize results as a dictionary with candidate names as keys and vote counts as values
results = {
    'candidate1': 0,
    'candidate2': 0,
    'candidate3': 0,
    'candidate4': 0,
    'candidate5': 0
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_candidate = request.form['candidate']
        # Increment the vote count for the selected candidate
        if selected_candidate in results:  # Ensure selected_candidate is a valid key
            results[selected_candidate] += 1
        return redirect(url_for('results'))
    return render_template('vote.html', candidates=candidates)

@app.route('/results')
def results():
    total_votes = sum(results.values())
    return render_template('results.html', results=results, total_votes=total_votes, candidates=candidates)

if __name__ == '__main__':
    app.run(debug=True)
