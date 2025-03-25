from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return open('templates/index.html').read()  # Ensure the file exists

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'Guest')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Thank You</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="/static/styles.css">
        <style>
            body {{
                background-color: black;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
                margin: 0;
            }}
            .thankyou-container {{
                background-color: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 10px;
                width: 50%;
                min-width: 350px;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }}
            h1 {{
                font-size: 2rem;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 1.2rem;
                margin-bottom: 10px;
            }}
            .btn-custom {{
                background-color: #a7a21d;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                margin-top: 20px;
                display: inline-block;
                font-size: 1.2rem;
            }}
            .btn-custom:hover {{
                background-color: #8c8a16;
            }}
        </style>
    </head>
    <body>
        <div class="thankyou-container">
            <h1>Thank You, {name}!</h1>
            <p>Your message has been successfully sent.</p>
            <p>I will get back to you soon.</p>
            <a href="/" class="btn btn-custom">Back to Home</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
