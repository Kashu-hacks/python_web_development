from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username  # Store username in session
        return redirect(url_for('profile'))
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Enter username">
            <button type="submit">Login</button>
        </form>
    '''

# Route to access session data
@app.route('/profile')
def profile():
    if 'username' in session:  # Check if session data exists
        return f"Welcome, {session['username']}!"
    return redirect(url_for('login'))

# Route to log out and clear session
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return "You have been logged out."

if __name__ == "__main__":
    app.run(debug=True)
