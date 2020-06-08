from flask import Flask, render_template #render_template nos va a permitir renderizar archivos html

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('contact_book.html')

if __name__ == '__main__':
    app.run()