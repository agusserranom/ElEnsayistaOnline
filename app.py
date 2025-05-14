from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cursos')
def cursos():
    return render_template('cursos.html')


@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


@app.route('/profesores')
def profesores():
    return render_template('profesores.html')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        # Crear el mensaje para enviar por correo
        email_message = MIMEMultipart()
        email_message['From'] = correo  # El correo que envió el mensaje
        email_message['To'] = 'elensayistaonline@gmail.com'  # El correo al que se enviará el mensaje
        email_message['Subject'] = 'Nuevo mensaje de contacto'

        body = f"Nombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"
        email_message.attach(MIMEText(body, 'plain'))

        try:
            # Conexión al servidor SMTP (usando Gmail)
            server = smtplib.SMTP('elensayistaonline@gmail.com', 587)
            server.starttls()  # Usar conexión segura
            server.login('elensayistaonline@gmail.com', 'zptn hora ikwq dwux')  # Tu correo y contraseña

            # Enviar el correo
            server.sendmail(correo, 'elensayistaonline@mail.com', email_message.as_string())

            server.quit()

            # Mostrar mensaje de éxito
            return render_template('contacto.html', enviado=True)

        except Exception as e:
            print(f"Error: {e}")
            return render_template('contacto.html', enviado=False)

    return render_template('contacto.html', enviado=False)


if __name__ == '__main__':
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
