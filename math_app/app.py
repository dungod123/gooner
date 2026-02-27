from flask import Flask, render_template, request, jsonify
from latex2sympy2 import latex2sympy
import sympy as sp

app = Flask(__name__)

# Route này mở trang web lên (Frontend)
@app.route('/')
def home():
    return render_template('index.html')

# Route này nhận công thức toán từ web gửi về, giải rồi trả lại kết quả
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        latex_str = data.get('equation', '') # Lấy chuỗi LaTeX người dùng nhập

        # Biến LaTeX thành Toán của SymPy
        expr = latex2sympy(latex_str)

        # Giải/Rút gọn toán
        result = sp.simplify(expr)

        return jsonify({'result': str(result)})
    except Exception as e:
        return jsonify({'error': 'Biểu thức phức tạp quá hoặc nhập sai cú pháp rùi: ' + str(e)})

if __name__ == '__main__':
    # Chạy server ở cổng 5000
    app.run(debug=True, port=5000)
