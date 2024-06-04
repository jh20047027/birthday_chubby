from flask import Flask, request

app = Flask(__name__)

@app.route('/1.html', methods=['POST'])
def process_form():
    account = request.form.get('account')
    password = request.form.get('pwd')
    print("Received account:", account)
    print("Received password:", password)
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
