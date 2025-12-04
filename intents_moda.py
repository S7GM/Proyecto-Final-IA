{
  "intents": [
    {
      "tag": "saludo",
      "patterns": ["hola", "buenas", "qué onda", "hey", "hola bot", "holaa"],
      "responses": [
        "¡Hola! Soy tu asistente de moda. Cuéntame, ¿para qué ocasión necesitas outfit?",
        "¡Qué tal! Estoy aquí para ayudarte a elegir tu outfit. ¿Qué evento tienes?"
      ]
    },
    {
      "tag": "despedida",
      "patterns": ["gracias", "adios", "bye", "nos vemos", "eso es todo"],
      "responses": [
        "¡Con gusto! Si necesitas otra recomendación, aquí estaré 💖",
        "¡Bye! Que tu outfit sea tan icónico como tú ✨"
      ]
    },
    {
      "tag": "recomendacion_outfit",
      "patterns": [
        "qué me pongo para una boda",
        "tengo una boda",
        "tengo entrevista de trabajo",
        "tengo una cita",
        "voy a una fiesta elegante",
        "necesito ropa para la oficina",
        "quiero un outfit casual",
        "qué me pongo para la escuela",
        "quiero verme formal",
        "quiero verme casual"
      ],
      "responses": [
        "Para eso necesito saber: ¿es de día o de noche? ¿Y hace calor o frío?",
        "Perfecto, dime si el evento es formal o casual, y si prefieres pantalón o vestido."
      ]
    },
    {
      "tag": "combinacion_colores",
      "patterns": [
        "qué colores combinan",
        "puedo combinar rosa con rojo",
        "qué color de blusa va con un pantalón negro",
        "qué color de zapatos combina con vestido azul",
        "qué colores se ven elegantes",
        "no sé cómo combinar colores"
      ],
      "responses": [
        "Negro, blanco, beige y gris combinan con casi todo. Un truco: usa una prenda llamativa y las demás en tonos neutros 😉",
        "Puedes usar combinaciones clásicas (negro con blanco, azul marino con beige) o de contraste (azul con naranja, rosa con verde). Lo importante es que al menos un color sea neutro."
      ]
    },
    {
      "tag": "talla_ajuste",
      "patterns": [
        "no sé qué talla soy",
        "me queda muy pegado",
        "no quiero que se vea muy flojo",
        "qué talla debo usar",
        "no quiero que marque la panza",
        "quiero que se vea cómodo"
      ],
      "responses": [
        "Lo ideal es que la prenda no haga arrugas muy marcadas ni se vea muy estirada. Si dudas entre dos tallas, escoge la más cómoda y ajusta con cinturón o accesorios.",
        "Busca que puedas mover brazos y caminar sin que se tense la tela. Si se marca demasiado, vale la pena subir una talla: comodidad = elegancia."
      ]
    },
    {
      "tag": "cuidado_prendas",
      "patterns": [
        "cómo lavo esta prenda",
        "se puede meter a lavadora",
        "cómo cuido la ropa",
        "se puede planchar",
        "cómo hago que dure más mi ropa"
      ],
      "responses": [
        "Revisa siempre la etiqueta: si dice ‘lavado a mano’, evita lavadora. En general, usa agua fría y evita secadora para que dure más.",
        "Las prendas delicadas (lencería, telas muy delgadas, algunas blusas) es mejor lavarlas a mano y secarlas a la sombra."
      ]
    },
    {
      "tag": "desconocido",
      "patterns": [],
      "responses": [
        "No estoy segura de entender eso, pero puedo ayudarte con outfits, tallas, colores y cuidado de la ropa 😊",
        "Todavía estoy aprendiendo. Intenta preguntarme sobre outfits, combinaciones de colores o tallas."
      ]
    }
  ]
}
