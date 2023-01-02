from flask import Flask,render_template,request,redirect
from converter import binary_to_decimal,decimal_to_binary,binary_to_hex,decimal_to_hex,hex_to_binary,hex_to_decimal

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1



@app.route("/", methods=['POST','GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        try:
            convert_from = request.form["convert_from"]
            convert_to = request.form["convert_to"]
            number = request.form["number"]
        except:
            convert_from,convert_to,number = '5','7','10'
        try:
            if convert_from == 'binary' and convert_to == 'decimal':
                output= binary_to_decimal(number)
            elif convert_from == 'decimal' and convert_to == 'binary':
                x = int(number)
                output= decimal_to_binary(x)
            elif convert_from == 'binary' and convert_to == 'hex':
                output= binary_to_hex(number)
            elif convert_from == 'decimal' and convert_to == 'hex':
                x = int(number)
                output= decimal_to_hex(x)
            elif convert_from == 'hex' and convert_to == 'binary':
                output= hex_to_binary(number)
            elif convert_from == 'hex' and convert_to == 'decimal':
                output= hex_to_decimal(number)
            elif convert_from == convert_to:
                output = number
            else:
                output = "Не удалось решить"
        except:
            output = "Не правильно ввели"
        return render_template('new.html', output = output )



if __name__ == "__main__":
    app.run(debug=True)
