from pyformlang.finite_automaton import Symbol, State, DeterministicFiniteAutomaton

class Automata:
    def __init__(self, name):
        self.estados = {
            State("q0"), State("q1"), State("q2"), State("q3"), State("q4"),
            State("q5"), State("q6"), State("q7"), State("q8"), State("q9"),
            State("q10"), State("q11"), State("q12"), State("q13"), State("q14"),
            State("q15"), State("q16"), State("q17"), State("q18"), State("q19")
        }
        self.lenguaje = {
            Symbol("a"), Symbol("b"), Symbol("c")
        }
        self.simbolos = list(self.lenguaje)
        self.estado_inicial = State("q0")
        self.estado_aceptacion = {
            State("q3"), State("q6"), State("q8"), State("q9"),State("q11"),State("q12"),State("q14"), State("q18"),State("19")
        }
        
        self.transiciones = {
            (State("q0"), Symbol("a")): State("q1"), (State("q0"), Symbol("b")): State("q10"),
            (State("q0"), Symbol("c")): State("q13"),

            (State("q1"), Symbol("a")): State("q2"), (State("q1"), Symbol("b")): State("q3"),
            (State("q2"), Symbol("a")): State("q4"), (State("q2"), Symbol("b")): State("q5"),
            (State("q4"), Symbol("a")): State("q8"), (State("q4"), Symbol("b")): State("q9"),
            (State("q5"), Symbol("a")): State("q6"), (State("q5"), Symbol("b")): State("q7"),
            (State("q7"), Symbol("a")): State("q8"), (State("q7"), Symbol("b")): State("q9"),

            (State("q10"), Symbol("a")): State("q11"), (State("q10"), Symbol("b")): State("q12"),

            (State("q13"), Symbol("a")): State("q15"), (State("q13"), Symbol("b")): State("q14"),
            (State("q15"), Symbol("a")): State("q16"), (State("q15"), Symbol("b")): State("q17"),
            (State("q16"), Symbol("a")): State("q17"), (State("q16"), Symbol("b")): State("q18"),
            (State("q17"), Symbol("a")): State("q3"), (State("q17"), Symbol("b")): State("q19")
        }

        self.estado_texto = {
            State("q0"): f"{name} se despierta en su cómoda cama, el reloj marca las 3:00 a.m., y todo está en silencio \nSiente que algo extraño está ocurriendo en su casa \n ¿Qué debería hacer?",
            State("q1"): f"Con valentía, {name} se levanta de la cama y enciende una linterna \n Los pasos resonan en la oscuridad mientras se aventura por la casa \n Llega a la sala de estar y escucha un murmullo proveniente de la cocina \n¿Qué debería hacer?",
            State("q2"): f"{name} se acerca sigilosamente a la cocina, la linterna ilumina las sombras mientras avanza \nCuando llega a la cocina, descubre que el ruido proviene de una ventana entreabierta que el viento golpea ocasionalmente \n Respira aliviado al descubrir que no hay nada sobrenatural en la casa \nSin embargo, al regresar a su habitación, {name} se encuentra con una figura oscura de pie al final del pasillo \n ¿Qué debería hacer?",
            State("q3"): f"{name} sale corriendo de la casa en busca de ayuda \n Corre a la casa de su vecino más cercano, golpeando frenéticamente la puerta \n Su vecino, asustado por la expresión de {name} y su agitación,le pregunta qué está pasando \n{name} explica la situación y el vecino llama a la policía \nCuando la policía llega, investigan la casa de {name} y no encuentran nada fuera de lo común \nLes dicen que probablemente fue solo su imaginación \n",
            State("q4"): f"Con valentía, {name} se acerca aún más a la figura oscura en el pasillo \nLa linterna tiembla en su mano mientras se prepara para enfrentar a esta entidad desconocida \nLa figura murmura palabras incomprensibles y extiende una mano hacia {name} \nCuando {name} está a punto de tocar la mano de la figura, esta se aparta bruscamente y emite un grito escalofriante \nEn ese momento, la figura desaparece en una nube de sombras oscuras que se disipan en el aire \n{name} queda desconcertado y aterrorizado por la experiencia \n La casa queda en silencio, y los murmullos han desaparecido \n ¿Qué debería hacer ahora?",
            State("q5"):f"Lentamente, {name} retrocede, manteniendo la vista fija en la figura oscura al final del pasillo \n La linterna tiembla en su mano mientras da un paso tras otro hacia su habitación \n Finalmente, llega a la puerta de su habitación y la cierra con llave \nEl corazón de {name} late con fuerza mientras observa la puerta cerrada \n La figura oscura no se mueve, pero su presencia es inquietante \n ¿Qué debería hacer ahora?",
            State("q6"): f"{name} toma su teléfono con manos temblorosas y llama al 911 \n Explica la situación y le dicen que enviarán a un oficial de policía lo antes posible \n Mientras espera, la figura oscura sigue inmóvil al final del pasillo \nEl oficial llega poco después y, junto con {name} , se aventuran a investigar la figura \n Descubren que no es más que una sombra proyectada por una lámpara defectuosa \n El alivio se apodera de {name} mientras la figura desaparece \nCon la explicación lógica en su lugar, {name} se siente avergonzado pero aliviado \n El oficial le sugiere que descanse y le da su número en caso de que necesite ayuda en el futuro \n",
            State("q7"): f"Con valentía, {name} decide acercarse a la figura oscura y preguntarle quién es y qué está haciendo en su casa \n Con la linterna en una mano, se acerca a la figura lentamente \nCuando llega lo suficientemente cerca, la figura se desvanece en la nada, dejando solo una sensación helada en el aire \n {name} queda desconcertado pero aliviado de que la figura haya desaparecido \n¿Qué debería hacer ahora?",
            State("q8"): f"Después de que la figura oscura se desvanece en la nada, {name} decide regresar a su habitación y tratar de dormir, asumiendo que todo ha vuelto a la normalidad \n Se siente agotado por la experiencia y espera que haya sido simplemente un evento aislado \nSin embargo, esa noche, mientras {name} yace en su cama, comienza a escuchar susurros inquietantes y siente una presencia en la habitación \n La figura oscura reaparece en la penumbra de su cuarto, esta vez más cerca que nunca \n Los ojos oscuros de la figura se clavan en {name} con una intensidad aterradora \nAterrorizado, {name} intenta encender la luz de su habitación, pero la electricidad falla \n La figura encapuchada se acerca más, y su aliento helado roza el cuello de {name} \nEl terror se apodera de {name} mientras comprende que la figura oscura nunca se fue y que esta vez, no hay escapatoria \n",
            State("q9"): f"Aunque {name} queda desconcertado por la repentina desaparición de la figura oscura, decide investigar en línea sobre actividades paranormales en su área para obtener más información \nPasando varias noches investigando en foros y sitios web, {name} descubre que su casa está construida sobre un terreno que alguna vez fue un cementerio indígena antiguo \n Los informes de actividades paranormales en la zona son numerosos, y la figura encapuchada que vio se menciona en varias historias locales como una entidad misteriosa que vaga por la zona \nIntrigado y decidido a entender mejor lo que ha ocurrido, {name} busca la ayuda de un experto en lo paranormal \n Juntos, investigan su casa y realizan rituales para comunicarse con cualquier entidad presente \n Descubren que la figura encapuchada era el espíritu de un antiguo chamán que necesitaba ayuda para cruzar al otro lado \n",
            State("q10"): f"{name} cierra los ojos con fuerza, tratando de ignorar la extraña sensación que lo rodea \n Sin embargo, el murmullo persiste y se hace más fuerte \n Siente como si algo estuviera acercándose a su cama \n ¿Qué debería hacer?",
            State("q11"): f"{name} se sienta en la cama y observa atentamente la habitación \n El murmullo se acerca cada vez más, y {name} puede ver una figura oscura moviéndose en la penumbra \n Antes de que pueda reaccionar, la figura se lanza hacia él \nLa historia toma un giro oscuro y {name} nunca se despierta \n",
            State("q12"): f"{name} se esconde bajo las sábanas, temblando de miedo mientras el murmullo se hace cada vez más fuerte \n Siente una presencia junto a su cama y, de repente, las sábanas son arrancadas violentamente \nLa historia toma un giro aterrador y {name} nunca se despierta \n",
            State("q13"): f"{name} llama a su amigo, quien rápidamente acepta venir a pasar la noche \n Mientras espera a su amigo, {name} escucha ruidos extraños que parecen provenir del sótano \n ¿Qué debería hacer?",
            State("q14"): f"{name} se sienta en la sala de estar, nervioso y esperando a su amigo \n Los ruidos extraños continúan, y {name} se siente cada vez más inquieto \n Finalmente, su amigo llega y {name} le cuenta todo lo que ha estado experimentando \nSu amigo, incrédulo, sugiere que {name} debería irse de la casa por esa noche y regresar por la mañana con más personas para investigar \n",
            State("q15"): f"{name} baja las escaleras hacia el sótano, la linterna tiembla en su mano \n A medida que desciende más profundamente, el murmullo se vuelve más intenso \n Cuando llega al sótano, encuentra una puerta entreabierta que conduce a una habitación oscura \n {name} decide entrar en la habitación oscura \n En el rincón más alejado, ve una figura encapuchada que murmura palabras incomprensibles \n ¿Qué debería hacer?",
            State("q16"): f"{name}  se acerca a la figura encapuchada en la habitación oscura \n La linterna tiembla en su mano mientras se acerca \n A medida que se aproxima,la figura encapuchada murmura palabras incomprensibles en un idioma desconocido \nLa figura de repente se detiene de murmurar y se da la vuelta lentamente para mirar a {name} directamente a los ojos \n Sus ojos son oscuros y sin vida, y su boca se curva en una sonrisa siniestra \n Entonces, comienza a pronunciar tu nombre y te llama con un tono escalofriante \n ¿Qué debería hacer ahora?",
            State("q17"): f"Con cuidado, {name} retrocede lentamente, manteniendo la vista fija en la figura oscura al final del pasillo \n La linterna tiembla en su mano mientras da un paso tras otro hacaia atrás, alejándose de la figura \nFinalmente, llega a la parte superior de las escaleras y sale del sótano \n Cierra la puerta detrás de él y se apresura a alejarse de la casa \n La presencia inquietante de la figura oscura queda atrás mientras {name} corre hacia la seguridad del exterior \n¿Qué debería hacer ahora?",
            State("q18"): f"Con valentía, {name}  decide enfrentar la figura oscura en el sótano oscuro. \nCon una mano temblorosa, se acerca más a la figura encapuchada y le pregunta quién es y qué quiere.\n Cuando {name}  le pregunta quién es y qué quiere, la figura se inclina hacia adelante y susurra en su oído palabras incomprensibles y aterradoras.\nDe repente, la figura se desvanece en la oscuridad, dejando solo un eco escalofriante en el sótano. {name}  queda solo en la penumbra, asustado y confundido. \nLos ruidos extraños cesan, pero la experiencia deja una profunda inquietud en {name} .\nA partir de ese día, {name}  vive con la constante sensación de que algo oscuro y sobrenatural lo acecha en las sombras.\nLa figura encapuchada sigue siendo un misterio sin resolver, y {name} nunca logra encontrar respuestas claras a las preguntas que le hizo esa noche.",
            State("q19"): f"La policía llega a su casa poco después de la llamada de {name} y realiza una búsqueda exhaustiva de la propiedad \n Aunque no encuentran ninguna evidencia física de la figura encapuchada, toman su reporte en serio \nEl oficial a cargo le asegura a {name} que patrullarán la zona con mayor frecuencia en las noches siguientes y sugiere que instale cámaras de seguridad en su hogar \n También le proporciona un número de contacto directo por si vuelve a enfrentarse a situaciones similares \nCon la presencia de la policía y el apoyo de las autoridades, {name} comienza a sentirse más seguro en su casa \n Aunque el misterio de la figura encapuchada nunca se resuelve por completo, {name} puede volver a su vida cotidiana con una sensación de protección adicional \n",
        }

        # Diccionario que relaciona cada símbolo con su texto correspondiente
        self.texto_transiciones = {
            (State("q0"), Symbol("a")): f"{name} decide levantarse de la cama y explorar la casa en busca de ruidos extraños.",
            (State("q0"), Symbol("b")): f"{name} se queda inmóvil en la cama, tratando de ignorar la sensación de malestar y volver a dormir.",
            (State("q0"), Symbol("c")): f"{name} agarra su teléfono y llama a su amigo para que venga a pasar la noche con él en caso de que algo ande mal.",

            (State("q1"), Symbol("a")): f"{name} decide acercarse sigilosamente a la cocina y tratar de averiguar de dónde viene el sonido.",
            (State("q1"), Symbol("b")): f"{name} decide salir corriendo de la casa en busca de ayuda.",

            (State("q2"), Symbol("a")): f"{name} decide confrontar a la figura y averiguar quién o qué es.",
            (State("q2"), Symbol("b")): f"{name} decide retroceder lentamente hacia su habitación y cerrar la puerta con llave.",

            (State("q4"), Symbol("a")): f"{name} decide regresar a su habitación y tratar de dormir, asumiendo que todo ha vuelto a la normalidad.", 
            (State("q4"), Symbol("b")): f"{name} decide buscar en línea sobre actividades paranormales en su área para obtener más información.",

            (State("q5"), Symbol("a")): f"{name} decide llamar a la policía para pedir ayuda.",
            (State("q5"), Symbol("b")): f"{name} decide enfrentar la figura oscura y preguntarle quién es y qué quiere.",

            (State("q7"), Symbol("a")): f"{name} decide regresar a su habitación y tratar de dormir, asumiendo que todo ha vuelto a la normalidad.",
            (State("q7"), Symbol("b")): f"{name} decide buscar en línea sobre actividades paranormales en su área para obtener más información.",

            (State("q10"), Symbol("a")): f"{name} decide enfrentar lo que sea que esté ocurriendo y se sienta en la cama para buscar la fuente del ruido.", 
            (State("q10"), Symbol("b")): f"{name} decide esconderse bajo las sábanas y esperar a que todo pase.",

            (State("q13"), Symbol("a")): f"{name} decide investigar el sótano antes de que llegue su amigo.",
            (State("q13"), Symbol("b")): f"{name} decide esperar a su amigo en la sala de estar.",

            (State("q15"), Symbol("a")): f"{name} decide acercarse a la figura encapuchada y tratar de comunicarse con ella.",
            (State("q15"), Symbol("b")): f"{name} decide retroceder lentamente y huir del sótano.",

            (State("q16"), Symbol("a")): f"{name} decide retroceder lentamente y huir del sótano.", 
            (State("q16"), Symbol("b")): f"{name} decide enfrentar la figura oscura y preguntarle quién es y qué quiere.",
            
            (State("q17"), Symbol("a")): f"{name} decide salir corriendo de la casa en busca de ayuda.",
            (State("q17"), Symbol("b")): f"{name} decide llamar a la policía desde su teléfono móvil y reportar lo que ha visto en el sótano.",
        }
        
        self.estado_image = {
            State("q0"): "assets/images/states/0.png",
            State("q1"): "assets/images/states/1.png",
            State("q2"): "assets/images/states/2.png",
            State("q3"): "assets/images/states/3.png",
            State("q4"): "assets/images/states/4.png",
            State("q5"):"assets/images/states/5.png",
            State("q6"): "assets/images/states/6.png",
            State("q7"):"assets/images/states/7.png",
            State("q8"):"assets/images/states/8.png",
            State("q9"): "assets/images/states/9.png",
            State("q10"): "assets/images/states/10.png",
            State("q11"): "assets/images/states/11.png",
            State("q12"): "assets/images/states/12.png",
            State("q13"): "assets/images/states/13.png",
            State("q14"):"assets/images/states/14.png",
            State("q15"):"assets/images/states/15.png",
            State("q16"): "assets/images/states/16.png",
            State("q17"): "assets/images/states/17.png",
            State("q18"):"assets/images/states/18.png",
            State("q19"): "assets/images/states/19.png"
        }

        # Crea el autómata y agrega las transiciones
        self.automaton = DeterministicFiniteAutomaton()
        for (estado_actual, simbolo), estado_destino in self.transiciones.items():
            self.automaton.add_transition(estado_actual, simbolo, estado_destino)
