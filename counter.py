from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# adding this method
@app.route("/")
def show_counter():
    if not "session_num" in session:
        print("key 'session_num' does NOT exist")
        session['session_num'] = 0
    session['session_num']+=1
    inputTwo = request.button['addTwo']
    print(inputTwo)


    return render_template("index.html", session_num = session["session_num"])

@app.route('/destroysession')
def destroy_session():
    session.clear()		# clears all keys

    return redirect("/")	# changed this line!

if __name__ == "__main__":
    app.run(debug=True)
