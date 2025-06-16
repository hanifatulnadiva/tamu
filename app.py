from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
app.config['SECRET_FLAG'] = os.environ.get("SECRET_FLAG", "TI404{SSTI_flag_for_testing}")

@app.route("/", methods=["GET", "POST"])
def buku_tamu():
    nama = ""
    pesan = ""

    if request.method == "POST":
        nama = request.form.get("nama", "")
        pesan = request.form.get("pesan", "")

    try:
        hasil_render = render_template_string(pesan)
    except Exception as e:
        hasil_render = f"<i>Error saat render: {e}</i>"

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Buku Tamu Digital</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                margin: 50px auto;
                max-width: 700px;
                background: #f9f9f9;
                padding: 20px;
            }}
            h1 {{ color: #2c3e50; }}
            input, textarea {{
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            button {{
                margin-top: 15px;
                padding: 10px 20px;
                background-color: #3498db;
                border: none;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }}
            .entry {{
                margin-top: 30px;
                padding: 15px;
                background: #ecf0f1;
                border-left: 5px solid #2980b9;
            }}
        </style>
    </head>
    <body>
        <h1>📖 Buku Tamu Digital</h1>
        <p>Silakan isi buku tamu kami dan tinggalkan pesan untuk admin atau pengunjung lain!</p>
        <form method="POST">
            <input type="text" name="nama" placeholder="Nama Anda (opsional)">
            <textarea name="pesan" placeholder="Pesan Anda..."></textarea>
            <button type="submit">Kirim</button>
        </form>

        {"<div class='entry'><strong>" + (nama or "Anonim") + " menulis:</strong><br><br><p>" + hasil_render + "</p></div>" if pesan else ""}
    </body>
    </html>
    """
    return html_template

if __name__ == "__main__":
    app.run(debug=True)
