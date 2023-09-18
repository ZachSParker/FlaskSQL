from flask import Flask, session, render_template, redirect

app=Flask(__name__)

app.secret_key = "i3nu2o1j"
#root route decorator/func def
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] +=1
    return render_template('index.html')
# end index function
#NINJA BONUS:add a way for the user to increment by 2 instead of one

@app.route('/refreshHarder')
def refresh_route2():# adds 2 to the session variable counter then redirects to root
    session['counter'] +=1
    return redirect('/')

# ATTEMPT at sensei bonus
# @app.route('/refreshHardest')
# def refresh_route3():
#     session['counter'] += request.form["num"]
#     return redirect('/')

@app.route('/reset')
def reset_session():#pops the counter variable from the session and redirects to root
    session.pop('counter')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


