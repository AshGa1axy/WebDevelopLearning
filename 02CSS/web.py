from flask import Flask,render_template

app=Flask(__name__)

@app.route('/show/info')
def show_info():
    return render_template('info.html')

if __name__=='__main__':
    app.run()