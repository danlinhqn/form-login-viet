from flask import Flask, jsonify, render_template_string
import base64

app = Flask(__name__)

def encode_url(url):
    return base64.urlsafe_b64encode(url.encode()).decode()

def decode_url(encoded_url):
    return base64.urlsafe_b64decode(encoded_url.encode()).decode()

@app.route('/iframe-url')
def get_iframe_url():
    iframe_url = "https://docs.google.com/forms/d/e/1FAIpQLSfk-3ozGbTIVk_kqurlcZQgij2HIAswDE2ZU0UgMaAYCkwXiA/formResponse?entry.109584719=Đào+Duy+Phúc&pli=1"
    encoded_url = encode_url(iframe_url)
    return jsonify({'url': encoded_url})

@app.route('/')
def show_form():
    html_content = '''
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/iframe-url')
                .then(response => response.json())
                .then(data => {
                    let encoded_url = data.url;
                    let iframe_url = atob(encoded_url);
                    let iframe = document.createElement('iframe');
                    iframe.src = iframe_url;
                    iframe.width = "100%";
                    iframe.height = "600px";
                    iframe.frameBorder = "0";
                    document.body.appendChild(iframe);
                });
        });
    </script>
    '''
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Google Form</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
