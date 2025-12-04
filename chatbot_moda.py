import json
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# ------------------ Cargar intents ------------------

with open("intents_moda.json", "r", encoding="utf-8") as f:
    data = json.load(f)

intents = data["intents"]

# ------------------ Entrenar modelo ------------------

texts = []
labels = []

for intent in intents:
    tag = intent["tag"]
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(tag)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf", LogisticRegression(max_iter=1000))
])

print("Entrenando al chatbot de moda...")
model.fit(texts, labels)
print("Entrenamiento terminado.\n")

# ------------------ Estado para recomendación de outfit ------------------

estado_outfit = {
    "evento": None,      # boda, entrevista, reunión, fiesta, etc.
    "momento": None,     # día / noche
    "clima": None,       # frío / calor
    "formalidad": None,  # formal / casual
    "prenda": None       # vestido / pantalón
}


def predecir_intent(mensaje_usuario: str) -> str:
    return model.predict([mensaje_usuario])[0]


def obtener_respuesta_simple(tag: str) -> str:
    """Respuestas normales cuando NO estamos haciendo lógica especial."""
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    for intent in intents:
        if intent["tag"] == "desconocido":
            return random.choice(intent["responses"])

    return "Aún no sé cómo responder eso, pero estoy aprendiendo 😊"


def actualizar_estado_outfit(mensaje: str):
    """Extrae info del mensaje y la guarda en el estado."""
    txt = mensaje.lower()

    # evento
    if any(p in txt for p in ["boda", "casamiento"]):
        estado_outfit["evento"] = "boda"
    elif any(p in txt for p in ["entrevista", "trabajo"]):
        estado_outfit["evento"] = "entrevista"
    elif any(p in txt for p in ["reunion", "reunión"]):
        estado_outfit["evento"] = "reunión"
    elif any(p in txt for p in ["fiesta", "antro"]):
        estado_outfit["evento"] = "fiesta"

    # momento
    if "noche" in txt:
        estado_outfit["momento"] = "noche"
    if "dia" in txt or "día" in txt:
        estado_outfit["momento"] = "día"

    # clima
    if "frio" in txt or "frío" in txt:
        estado_outfit["clima"] = "frío"
    if "calor" in txt or "caliente" in txt:
        estado_outfit["clima"] = "calor"

    # formalidad
    if "formal" in txt or "elegante" in txt:
        estado_outfit["formalidad"] = "formal"
    if "casual" in txt or "relajado" in txt:
        estado_outfit["formalidad"] = "casual"

    # prenda
    if "vestido" in txt:
        estado_outfit["prenda"] = "vestido"
    if "pantalon" in txt or "pantalón" in txt or "jeans" in txt:
        estado_outfit["prenda"] = "pantalón"


def generar_recomendacion() -> str:
    """Genera el texto final de outfit en base al estado."""
    evento = estado_outfit["evento"]
    momento = estado_outfit["momento"]
    clima = estado_outfit["clima"]
    formalidad = estado_outfit["formalidad"]
    prenda = estado_outfit["prenda"]

    partes = []

    if formalidad == "formal":
        if prenda == "vestido":
            partes.append("un vestido midi o largo en tonos neutros (negro, azul marino o vino)")
        else:
            partes.append("un pantalón de vestir recto con una blusa elegante y blazer")
    else:  # casual
        if prenda == "vestido":
            partes.append("un vestido cómodo en colores claros o pastel")
        else:
            partes.append("jeans o pantalón cómodo con una blusa básica y una chamarra ligera")

    if clima == "frío":
        partes.append("agrega medias, abrigo o suéter y, si puedes, botas cerradas")
    elif clima == "calor":
        partes.append("usa telas frescas (algodón, lino) y calzado abierto o tenis ligeros")

    if evento == "boda":
        partes.append("evita el blanco para no opacar a la novia 😉")
    elif evento == "entrevista":
        partes.append("evita estampados muy llamativos y cuida que la ropa esté bien planchada")
    elif evento == "reunión":
        partes.append("mantén un equilibrio entre cómodo y presentable")
    elif evento == "fiesta":
        partes.append("puedes agregar accesorios brillantes o un labial llamativo para destacar")

    recomendacion = "Te recomiendo " + ", ".join(partes) + "."
    return recomendacion


def manejar_recomendacion_outfit(mensaje_usuario: str) -> str:
    """Logica para ir preguntando y luego dar la recomendación final."""
    # Actualizamos lo que el usuario acaba de decir
    actualizar_estado_outfit(mensaje_usuario)

    # Revisamos qué falta
    faltantes = []
    if estado_outfit["momento"] is None:
        faltantes.append("si es de día o de noche")
    if estado_outfit["clima"] is None:
        faltantes.append("si hace frío o calor")
    if estado_outfit["formalidad"] is None:
        faltantes.append("si el evento es formal o casual")
    if estado_outfit["prenda"] is None:
        faltantes.append("si prefieres vestido o pantalón")

    if faltantes:
        # Todavía falta info → preguntamos solo lo que falta
        texto_faltantes = "; ".join(faltantes)
        return f"Perfecto, voy entendiendo. Solo dime {texto_faltantes}."
    else:
        # Ya tenemos todo → damos recomendación y reseteamos estado
        recomendacion = generar_recomendacion()
        # reset
        for k in estado_outfit:
            estado_outfit[k] = None
        return recomendacion


def generar_respuesta(mensaje_usuario: str) -> str:
    tag = predecir_intent(mensaje_usuario)

    if tag == "recomendacion_outfit":
        return manejar_recomendacion_outfit(mensaje_usuario)
    else:
        return obtener_respuesta_simple(tag)


def chat():
    print("FashionBot: ¡Hola! Soy tu asistente de moda. Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ")

        if user_input.lower() in ["salir", "exit", "adios", "adiós", "bye"]:
            print("FashionBot: ¡Gracias por usarme! Que tengas un súper outfit ✨")
            break

        respuesta = generar_respuesta(user_input)
        print(f"FashionBot: {respuesta}\n")


if __name__ == "__main__":
    chat()
