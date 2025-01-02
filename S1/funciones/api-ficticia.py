from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/persona/<int:id>', methods=['GET'])
def obtener_persona(id):
    # Datos ficticios
    datos = {
        1: {'nombre': 'Juan', 'edad': 30},
        2: {'nombre': 'Maria', 'edad': 25}
    }
    persona = datos.get(id, None)
    if persona:
        return jsonify(persona)
    else:
        return jsonify({'error': 'Persona no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)