from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
#stuff
# adding this method
@app.route("/")
def show_counter():
    print(request.form)
    if 'secret_key' in session:
        print('key exists!')
        session['session_num']+=1
    else:
        print("key 'secret_key' does NOT exist")
        session['session_num'] = 1
    return render_template("index.html", session_num = session['session_num'])

@app.route('/process', methods=['POST'])
def nsession():
    print("Got Post Info")
    print(request.form)

    return redirect("/stuff")	# changed this line!

@app.route('/stuff')
def destroy_session():
    session.clear()		# clears all keys
    session.pop('secret_key')		# clears a specific key
    return redirect("/")	# changed this line!

if __name__ == "__main__":
    app.run(debug=True)
