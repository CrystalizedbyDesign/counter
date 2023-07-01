from flask import Flask, render_template, session, redirect # Here we added in session and redirect

app= Flask(__name__)

app.secret_key="This is to test session."

@app.route('/')
def index():
    if 'counter'not in session:
        session["counter"] = 0
    else:
        session['counter'] += 1 #you will increment here

    return render_template('index.html')

@app.route('/destroy_session') 
def reset():
    session.clear()  # Here you will clear the session
    
    return redirect('/')  #Here you will be redirected to the beginning of the session.
    
if __name__=='__main__':
    app.run(debug=True)