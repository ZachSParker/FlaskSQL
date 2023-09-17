from flask import Flask, session, render_template, redirect ,request
app=Flask(__name__)
app.secret_key = "i3nu2o1j"
@app.route('/')
def root_route():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


