
from collections import namedtuple

from base_conocimiento_mascotas import PREDICADOS, ENFERMEDADES, HECHOS, REGLAS

Clausula = namedtuple("Clausula", "cabeza cuerpo regla")

Prueba = namedtuple("Prueba", "predicado origen hijos")

PREGUNTAS = {
    "Cachorro": "¿Es un cachorro (todavía muy pequeño, de pocos meses)?",
    "HembraEntera": "¿Es una hembra que no ha sido esterilizada?",
    "CeloUltimosDosMeses": "¿estuvo celo en los últimos 2 meses?",
    "VacunacionIncompleta": "¿Le faltan vacunas o no está vacunado?",
    "ContactoConPerrosEnfermos": "¿Ha convivido con perros enfermos o estado en lugares con muchos perros (guardería, refugio, paseos)?",
    "AccesoARaticida": "¿Pudo haber comido veneno para ratas o una rata envenenada?",
    "ComioBasuraOAlimentoInadecuado": "¿Comió basura, comida en mal estado o algo que no debía?",
    "Letargo": "¿Tiene muy poca energía y duerme más de lo normal?",
    "Anorexia": "¿Ha dejado de comer o come mucho menos de lo normal?",
    "PerdidaPeso": "¿Ha bajado de peso sin que usted lo haya buscado?",
    "Polifagia": "¿Come mucho más de lo normal y aun así parece tener hambre?",
    "PoliuriaPolidipsia": "¿Toma mucha más agua de lo normal y orina más seguido o en mayor cantidad?",
    "Hiperactividad": "¿Tiene más inquietud o nerviosismo de lo normal?",
    "Debilidad": "¿Se le ve débil o le cuesta pararse y caminar?",
    "PalidezMucosas": "¿Tiene las encías casi blancas o muy pálidas? (levante el labio para verlas)",
    "Hemorragia": "¿Tiene sangrado por la nariz, la boca, la orina o las heces?",
    "Hematomas": "¿Le salieron moretones o manchas rojas o moradas en la piel?",
    "Disnea": "¿Le cuesta respirar o respira muy rápido o con la boca abierta?",
    "Vomitos": "¿Ha vomitado?",
    "VomitosIntensos": "¿Los vómitos son muy seguidos o muy fuertes?",
    "Diarrea": "¿Tiene diarrea (heces blandas o líquidas)?",
    "DiarreaProfusa": "¿La diarrea es muy abundante o líquida como agua?",
    "DiarreaConSangre": "¿Hay sangre en la diarrea?",
    "DolorAbdominal": "¿Se queja o se pone tenso cuando le toca la panza?",
    "PosturaRezo": "¿Se agacha con el pecho en el suelo?",
    "AbdomenAbultado": "¿Tiene la panza hinchada o abultada?",
    "Tos": "¿Tiene tos?",
    "TosParoxistica": "¿La tos le da en ataques fuertes, como si quisiera sacar algo de la garganta?",
    "Estornudos": "¿Estornuda con frecuencia?",
    "SecrecionNasal": "¿Le escurre moco o líquido por la nariz?",
    "Convulsiones": "¿Ha tenido convulsiones (se cae y se sacude sin control)?",
    "Temblores": "¿Le tiembla el cuerpo o las patas?",
    "Ataxia": "¿Camina descoordinado, tambaleándose o se cae al caminar?",
    "Mioclonias": "¿Tiene sacudidas bruscas e involuntarias en algún músculo (cara, patas)?",
    "Polaquiuria": "¿Va muchas veces a orinar pero saca muy poca orina cada vez?",
    "Estranguria": "¿Se esfuerza o se queja al orinar?",
    "NoLograOrinar": "¿Intenta orinar pero no le sale nada?",
    "PruritoIntenso": "¿Se rasca, muerde o lame la piel con mucha insistencia?",
    "VenPulgasOHeces": "¿Ha visto pulgas o puntitos negros (sus heces) en el pelo?",
    "LesionesLomoCola": "¿Tiene heridas o irritación en el lomo, la base de la cola o la parte de atrás?",
    "LesionesOrejaCodos": "¿Tiene lesiones en el borde de las orejas o en los codos?",
    "PapulasCostrosas": "¿Tiene granitos con costra en la piel?",
    "CostrasGrisAmarillentas": "¿Tiene costras gruesas de color gris o amarillento?",
    "AlopeciaPorRascado": "¿Tiene zonas sin pelo por rascarse?",
    "PeloSeco": "¿Tiene el pelo seco, opaco o quebradizo?",
    "SacudeCabeza": "¿Sacude la cabeza con frecuencia?",
    "RascaOreja": "¿Se rasca las orejas?",
    "SecrecionOido": "¿Le sale líquido o pus de alguno de los oídos?",
    "MalOlorOido": "¿Le huele mal el oído?",
    "CerumenOscuro": "¿Tiene mucha cera oscura (café o negra) en el oído?",
    "OjoRojo": "¿Tiene algún ojo rojo?",
    "ParpadoHinchado": "¿Tiene algún párpado hinchado?",
    "SecrecionOcular": "¿Le salen lagañas o líquido de los ojos?",
    "PupilaAlterada": "¿Las pupilas (la parte negra del ojo) se ven de distinto tamaño o raras?",
    "Halitosis": "¿Tiene mal aliento?",
    "HalitosisMarcada": "¿El mal aliento es muy fuerte?",
    "EnciaRoja": "¿Tiene las encías rojas?",
    "EnciaInflamada": "¿Tiene las encías hinchadas?",
    "EnciaSangra": "¿Le sangran las encías (por ejemplo, al comer o al tocarlas)?",
    "DientesFlojos": "¿Tiene dientes flojos o que se mueven?",
    "PerdidaDientes": "¿Ha perdido dientes?",
    "RaicesExpuestas": "¿Se le ve la raíz de algún diente (la encía se ha retraído)?",
    "PusEnEncia": "¿Tiene pus o bultos con pus en las encías?",
    "DescargaVaginalPurulenta": "¿Le sale por la vagina un líquido espeso, con pus o mal olor?",


}
# formas mas faciles de llamar a los sintomas
SINTOMAS = {
    "Letargo": "poca energía", "Anorexia": "falta de apetito", "PerdidaPeso": "pérdida de peso",
    "Polifagia": "come en exceso", "PoliuriaPolidipsia": "mucha sed y orina", "Hiperactividad": "inquietud",
    "Debilidad": "debilidad", "PalidezMucosas": "encías pálidas", "Hemorragia": "sangrado",
    "Hematomas": "moretones", "Disnea": "dificultad para respirar", "Vomitos": "vómitos",
    "VomitosIntensos": "vómitos intensos", "Diarrea": "diarrea", "DiarreaProfusa": "diarrea abundante",
    "DiarreaConSangre": "diarrea con sangre", "DolorAbdominal": "dolor abdominal",
    "PosturaRezo": "postura de rezo", "AbdomenAbultado": "panza abultada", "Tos": "tos",
    "TosParoxistica": "tos en ataques", "Estornudos": "estornudos", "SecrecionNasal": "moco nasal",
    "Convulsiones": "convulsiones", "Temblores": "temblores", "Ataxia": "falta de coordinación",
    "Mioclonias": "sacudidas musculares", "Polaquiuria": "orina muchas veces en poca cantidad",
    "Estranguria": "dolor al orinar", "NoLograOrinar": "no logra orinar", "PruritoIntenso": "mucha comezón",
    "VenPulgasOHeces": "pulgas", "LesionesLomoCola": "lesiones en lomo y cola",
    "LesionesOrejaCodos": "lesiones en orejas y codos", "PapulasCostrosas": "granitos con costra",
    "CostrasGrisAmarillentas": "costras gris amarillentas", "AlopeciaPorRascado": "zonas sin pelo",
    "PeloSeco": "pelo seco", "SacudeCabeza": "sacude la cabeza", "RascaOreja": "se rasca las orejas",
    "SecrecionOido": "secreción en el oído", "MalOlorOido": "mal olor en el oído",
    "CerumenOscuro": "cera oscura en el oído", "OjoRojo": "ojo rojo", "ParpadoHinchado": "párpado hinchado",
    "SecrecionOcular": "secreción en el ojo", "PupilaAlterada": "pupila alterada", "Halitosis": "mal aliento",
    "HalitosisMarcada": "mal aliento fuerte", "EnciaRoja": "encías rojas", "EnciaInflamada": "encías hinchadas",
    "EnciaSangra": "encías que sangran", "DientesFlojos": "dientes flojos", "PerdidaDientes": "pérdida de dientes",
    "RaicesExpuestas": "raíces expuestas", "PusEnEncia": "pus en las encías",
    "DescargaVaginalPurulenta": "secreción vaginal con pus",

}


# nombres completos de enferemedades
ENFERMEDAD_NOMBRE = {
    "parvovirosis": "Parvovirosis canina", "panleucopenia": "Panleucopenia felina",
    "indiscrecion_alimentaria": "Indigestión por comer algo inadecuado", "pancreatitis": "Pancreatitis aguda",
    "parasitosis_intestinal": "Parásitos intestinales", "moquillo": "Moquillo canino",
    "tos_perreras": "Tos de las perreras", "complejo_respiratorio_felino": "Complejo respiratorio felino",
    "flutd": "Problema urinario felino (FLUTD)", "flutd_obstructivo": "Problema urinario felino con obstrucción",
    "enfermedad_renal_cronica": "Enfermedad renal crónica", "diabetes_mellitus": "Diabetes mellitus",
    "hipertiroidismo_felino": "Hipertiroidismo felino", "otitis_externa": "Otitis externa (infección de oído)",
    "dermatitis_pulgas": "Dermatitis alérgica por pulgas", "sarna_sarcoptica": "Sarna sarcóptica",
    "conjuntivitis": "Conjuntivitis", "gingivitis": "Gingivitis (inflamación de encías)",
    "periodontitis": "Periodontitis (enfermedad avanzada de encías y dientes)",
    "intoxicacion_rodenticidas": "Intoxicación por veneno para ratas", "piometra": "Piómetra (infección del útero)",
}
ORDEN_URGENCIA = {"alta": 0, "media": 1, "baja": 2}
INFO = {enfermedad[0]: enfermedad for enfermedad in ENFERMEDADES}
HECHO_DE = {hecho[0]: codigo for codigo, hecho in HECHOS.items()}
HECHO_DE["flutd_obstructivo"] = "H9"

def separar(condicion): #basicamente toma una condicion y separa sus alternativas
    if isinstance(condicion, str):
        return [[condicion]]
    if condicion[0] == "NO":
        if not isinstance(condicion[1], str):
            raise ValueError("NO solo se aplica a un predicado")
        return [[("NO", condicion[1])]] #si hay un NO lo guarda en una tupla para identificarlo despues
    if condicion[0] == "O":
        alternativas = []
        for subcondicion in condicion[1:]:
            alternativas += separar(subcondicion) #si hay un O, separa cada opcion y la guarda por su lado
        return alternativas
    raise ValueError("Operador desconocido: " + str(condicion[0]))


def combinar(condiciones): #junta las condiciones en grupos, tomando en cuenta las alternativas
    grupo_condiciones = [[]]
    for condicion in condiciones:
        grupo_condiciones = [cuerpo + alternativa for cuerpo in grupo_condiciones for alternativa in separar(condicion)]
    return grupo_condiciones

def a_horn(reglas): #toma los grupos de condiciones y les agrega su conclusion
    clausulas = []
    for numero, (condiciones, conclusion) in enumerate(reglas, start=1):
        for cuerpo in combinar(condiciones):
            clausulas.append(Clausula(conclusion, tuple(cuerpo), numero)) #convierte cada grupo en una clausula mas sencilla
    return clausulas




# todas las reglas a clausulas
CLAUSULAS = a_horn(REGLAS)


class Motor:
    def __init__(self, preguntar=None):
        self.clausulas = CLAUSULAS
        self.preguntar = preguntar
        self.hechos = {}
        self.preguntadas = []
        self.indice_meta = 0
        self.faltan_exacto = None
        self.por_cabeza = {} # junta las clausulas que llegan a la misma conclusion
        for clausula in self.clausulas:
            self.por_cabeza.setdefault(clausula.cabeza, []).append(clausula)
        self.generales = {} # guarda las relaciones entre predicados relacionados
        for clausula in self.clausulas:
            if len(clausula.cuerpo) == 1 and isinstance(clausula.cuerpo[0], str):
                self.generales.setdefault(clausula.cuerpo[0], []).append(clausula.cabeza)
        todos = {predicado for grupo in PREDICADOS.values() for predicado in grupo}
        compuestos = {cabeza for cabeza, clausulas_de_cabeza in self.por_cabeza.items()
                      if all(len(clausula.cuerpo) > 1 for clausula in clausulas_de_cabeza)}
        self.preguntables = todos - compuestos # deja solo los predicados que se pueden preguntar
        self.contexto = set(PREDICADOS["contexto"])
        self.metas = [] # aqui se guarda la lista de enfermedades que se van a revisar
        for clausula in self.clausulas:
            if clausula.cabeza in INFO and clausula.cabeza not in self.metas:
                self.metas.append(clausula.cabeza)

    def guardar_hecho(self, predicado, valor=True): # guarda un dato que ya conocemos, como si es perro o gato
        self.hechos[predicado] = valor

    def estado(self, predicado): # revisa si un dato ya se sabe como verdadero o falso, namas se usa en afinar
        if predicado in self.hechos:
            return self.hechos[predicado]
        for predicado_general in self.generales.get(predicado, ()):
            if self.estado(predicado_general) is False:
                return False
        return None

    def obtener_dato(self, predicado): # busca el dato y, si hace falta, se lo pregunta al usuario
        if predicado in self.hechos:
            return self.hechos[predicado]
        if predicado not in self.preguntables:
            return False
        for predicado_general in self.generales.get(predicado, ()):
            if predicado_general in self.preguntables and not self.obtener_dato(predicado_general):
                self.hechos[predicado] = False
                return False
        if self.preguntar:
            faltan = self.faltan_exacto
            if faltan is None:
                faltan = self.estimar_faltantes()
            self.hechos[predicado] = self.preguntar(predicado, len(self.preguntadas) + 1, faltan)
            self.preguntadas.append(predicado)
        else:
            self.hechos[predicado] = False
        return self.hechos[predicado]

    def demostrar(self, meta, pila=()): # intenta comprobar si se cumple una conclusion o enfermedad
        if meta in pila:
            return
        if meta in self.preguntables and self.obtener_dato(meta):
            yield Prueba(meta, "hecho", ())
        for clausula in self.por_cabeza.get(meta, ()):
            for hijos in self.revisa_condicion(clausula.cuerpo, pila + (meta,)):
                yield Prueba(meta, f"R{clausula.regla}", tuple(hijos))

    def revisa_condicion(self, literales, pila): # revisa una por una las condiciones de una clausula
        if not literales:
            yield []
            return
        primero, resto = literales[0], literales[1:]
        if isinstance(primero, tuple):
            predicado = primero[1]
            if next(self.demostrar(predicado, pila), None) is None:
                for pruebas_resto in self.revisa_condicion(resto, pila):
                    yield [Prueba("NO " + predicado, "NAF", ())] + pruebas_resto
        else:
            prueba = next(self.demostrar(primero, pila), None)
            if prueba is not None:
                for pruebas_resto in self.revisa_condicion(resto, pila):
                    yield [prueba] + pruebas_resto

    def diagnosticar(self): # intenta encontrar cuales enfermedades se cumplen con los datos actuales
        resultados = []
        for posicion, enfermedad in enumerate(self.metas):
            self.indice_meta = posicion
            prueba = next(self.demostrar(enfermedad), None)
            if prueba:
                resultados.append((enfermedad, prueba))
        self.indice_meta = len(self.metas)
        return resultados


    def buscar_condicion(self, predicado): # busca todos sintomas o condiciones de una enfermedad
        if predicado in self.preguntables:
            return {predicado}
        hojas = set()
        for clausula in self.por_cabeza.get(predicado, ()):
            for literal in clausula.cuerpo:
                hojas |= self.buscar_condicion(literal[1] if isinstance(literal, tuple) else literal)
        return hojas

    def estimar_faltantes(self): # hace una prueba para calcular aproximadamente cuantas preguntas faltan
        simulacion = Motor(preguntar=lambda predicado, numero, faltan: False)
        simulacion.faltan_exacto = 0
        simulacion.hechos = dict(self.hechos)
        for meta in self.metas[self.indice_meta:]:
            next(simulacion.demostrar(meta), None)
        return max(0, len(simulacion.preguntadas) - 1)


    def perfil(self, enfermedad): # obtiene la lista de sintomas relacionados con una enfermedad y los guarda
        signos = []
        for clausula in self.por_cabeza[enfermedad]:
            for literal in clausula.cuerpo:
                if isinstance(literal, tuple):
                    continue
                for hoja in sorted(self.buscar_condicion(literal)): #aqui busca los sintomas de la enfermedad
                    if hoja not in self.contexto and hoja not in signos:
                        signos.append(hoja)
        return signos

    def pendientes_afinar(self, resultados): # junta los sintomas que todavia no se han preguntado
        pendientes = []
        for enfermedad, _ in resultados:
            for sintoma in self.perfil(enfermedad): #busca el perfil de la enfermedad para conocer todos sus sintomas
                if self.estado(sintoma) is None and sintoma not in pendientes:
                    pendientes.append(sintoma)
        return pendientes

    def afinar(self, pendientes): # pregunta los sintomas pendientes para revisar mejor los resultados
        for posicion, sintoma in enumerate(pendientes):
            self.faltan_exacto = len(pendientes) - posicion - 1
            self.obtener_dato(sintoma)
        self.faltan_exacto = None

    def tiene(self, sintoma): # revisa si el sintoma se confirmo directamente o por uno relacionado
        if self.hechos.get(sintoma):
            return True
        return any(self.hechos.get(especifico) for especifico, generales in self.generales.items()
                   if sintoma in generales)

    def evaluar(self, enfermedad, prueba): # compara los sintomas reportados con los de la enfermedad
        perfil = self.perfil(enfermedad)
        presentes = [sintoma for sintoma in perfil if self.tiene(sintoma)]
        ausentes = [sintoma for sintoma in perfil if sintoma not in presentes]
        reportados = {predicado for predicado, valor in self.hechos.items()
                      if valor and predicado in self.preguntables and predicado not in self.contexto}
        for sintoma in list(reportados):
            for predicado_general in self.generales.get(sintoma, ()):
                reportados.discard(predicado_general)
        perfil_amplio = set(perfil)
        for sintoma in perfil:
            perfil_amplio |= set(self.generales.get(sintoma, ()))
        coincidencia = len(presentes) / len(perfil) if perfil else 0
        explicacion = len(reportados & perfil_amplio) / len(reportados) if reportados else 0
        suma = coincidencia + explicacion
        seguridad = 2 * coincidencia * explicacion / suma if suma else 0
        return {"enfermedad": enfermedad, "regla": prueba.origen, "urgencia": INFO[enfermedad][4],
                "presentes": presentes, "ausentes": ausentes, "coincidencia": coincidencia,
                "seguridad": seguridad}



def etiqueta_seguridad(valor): # convierte el numero de seguridad en alta, media o baja
    if valor >= 0.8:
        return "alta"
    if valor >= 0.6:
        return "media"
    return "baja"


def lista(sintomas): # cambia los nombres internos por nombres mas faciles de leer
    return ", ".join(SINTOMAS.get(sintoma, sintoma) for sintoma in sintomas) if sintomas else "ninguno"


def mostrar_resultado(evaluaciones): # muestra las enfermedades encontradas y sus sintomas
    print("\nRESULTADO")
    if not evaluaciones:
        print("Con estos datos no se identificó ninguna de las enfermedades del sistema.")
        print("Esto no descarta un problema: si algo le preocupa, consulte a un veterinario.")
    evaluaciones.sort(key=lambda evaluacion: (ORDEN_URGENCIA[evaluacion["urgencia"]], -evaluacion["seguridad"]))
    for numero, evaluacion in enumerate(evaluaciones, start=1):
        total = len(evaluacion["presentes"]) + len(evaluacion["ausentes"])
        print(f"\n{numero}. {ENFERMEDAD_NOMBRE[evaluacion['enfermedad']]} (urgencia {evaluacion['urgencia'].upper()})")
        print(f"   Coincide con {len(evaluacion['presentes'])} de {total} síntomas de la enfermedad ({evaluacion['coincidencia']:.0%})")
        print(f"   Seguridad del resultado: {evaluacion['seguridad']:.0%} ({etiqueta_seguridad(evaluacion['seguridad'])})")
        print(f"   Síntomas que presenta: {lista(evaluacion['presentes'])}")
        print(f"   Síntomas de la enfermedad que no presenta: {lista(evaluacion['ausentes'])}")
        codigo = HECHO_DE.get(evaluacion["enfermedad"])
        if codigo:
            fuente = HECHOS[codigo][2].replace("MC2015", "Muñoz et al. (2015)").replace("ER2014", "Esquivel y Reyes (2014)")
            print(f"   Regla aplicada: {evaluacion['regla']} | Fuente: {fuente} ({codigo})")
        if evaluacion["urgencia"] != "baja":
            print("   Se recomienda acudir con un veterinario.")
    if evaluaciones:
        print("\nLa seguridad compara los síntomas de la enfermedad con los que usted reportó; no es una probabilidad médica.")
    print("Aviso: este resultado es orientativo y no sustituye la evaluación de un veterinario.")



def preguntar_usuario(predicado, numero, faltan): # hace la pregunta y revisa que la respuesta sea valida
    texto = PREGUNTAS.get(predicado, f"¿Presenta {predicado}?")
    avance = f"faltan aprox. {faltan}" if faltan > 0 else "casi terminamos"
    while True:
        respuesta = input(f"\n[Pregunta {numero} · {avance}]\n{texto} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Responde s (sí) o n (no).")


def consulta(): # lleva el proceso completo de una consulta
    motor = Motor(preguntar=preguntar_usuario)
    print("\nResponda s (sí) o n (no). El número de preguntas que faltan es aproximado.")
    while True:
        especie = input("\n¿Su mascota es un perro (p) o un gato (g)? ").strip().lower()
        if especie in ("p", "g"):
            break
    motor.guardar_hecho("Perro", especie == "p")
    motor.guardar_hecho("Gato", especie == "g")
    resultados = motor.diagnosticar() # revisa las enfermedades con las respuestas que ya tenemos
    pendientes = motor.pendientes_afinar(resultados) #mira si hay pendientes
    if pendientes: #si los encuentra
        print(f"\nPara afinar el resultado hacen falta {len(pendientes)} preguntas más.")
        motor.afinar(pendientes) #los pregunta
    mostrar_resultado([motor.evaluar(enfermedad, prueba) for enfermedad, prueba in resultados])
    print(f"\nPreguntas respondidas: {len(motor.preguntadas)}")
    input("\nPresiona ENTER para continuar...")


def menu(): 
    while True:
        print("\n===================================")
        print(" MOTOR DE INFERENCIA DE MASCOTAS")
        print("===================================")
        print("1. Nueva consulta")
        print("0. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            consulta()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
