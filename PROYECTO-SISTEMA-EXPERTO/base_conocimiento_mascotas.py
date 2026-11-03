# Base de conocimiento: sistema experto de diagnostico preliminar en perros y gatos
# Solo contiene hechos y reglas, no incluye motor de inferencia

# Predicados (signos y contexto observables por el dueño), agrupados por tipo
PREDICADOS = {
    "contexto": (
        "Perro", "Gato", "Cachorro", "HembraEntera", "CeloUltimosDosMeses",
        "VacunacionIncompleta", "ContactoConPerrosEnfermos", "AccesoARaticida",
        "ComioBasuraOAlimentoInadecuado"
    ),
    "general": (
        "Letargo", "Anorexia", "PerdidaPeso", "Polifagia", "PoliuriaPolidipsia",
        "Hiperactividad", "Debilidad", "PalidezMucosas", "Hemorragia",
        "Hematomas", "Disnea"
    ),
    "digestivo": (
        "Vomitos", "VomitosIntensos", "Diarrea", "DiarreaProfusa",
        "DiarreaConSangre", "DolorAbdominal", "PosturaRezo", "AbdomenAbultado"
    ),
    "respiratorio": (
        "Tos", "TosParoxistica", "Estornudos", "SecrecionNasal",
        "SecrecionOculonasal"
    ),
    "neurologico": ("Convulsiones", "Temblores", "Ataxia", "Mioclonias"),
    "urinario": ("Polaquiuria", "Estranguria", "NoLograOrinar"),
    "piel": (
        "PruritoIntenso", "VenPulgasOHeces", "LesionesLomoCola",
        "LesionesOrejaCodos", "PapulasCostrosas", "CostrasGrisAmarillentas",
        "AlopeciaPorRascado", "PeloSeco"
    ),
    "oido": (
        "SacudeCabeza", "RascaOreja", "SecrecionOido", "MalOlorOido",
        "CerumenOscuro"
    ),
    "ojo": ("OjoRojo", "ParpadoHinchado", "SecrecionOcular", "PupilaAlterada"),
    "boca": (
        "Halitosis", "HalitosisMarcada", "EnciaRoja", "EnciaInflamada",
        "EnciaSangra", "DientesFlojos", "PerdidaDientes", "RaicesExpuestas",
        "PusEnEncia"
    ),
    "reproductivo": ("DescargaVaginalPurulenta",)
}


# Enfermedades: (nombre, especie, sistema, causa, urgencia)
ENFERMEDADES = {
    ("parvovirosis", "perro", "digestiva", "viral", "alta"),
    ("panleucopenia", "gato", "digestiva", "viral", "alta"),
    ("indiscrecion_alimentaria", "ambos", "digestiva", "dietetica", "baja"),
    ("pancreatitis", "ambos", "digestiva", "multifactorial", "alta"),
    ("parasitosis_intestinal", "perro", "digestiva", "parasitaria", "media"),
    ("moquillo", "perro", "multisistemica", "viral", "alta"),
    ("tos_perreras", "perro", "respiratoria", "multietiologica", "media"),
    ("complejo_respiratorio_felino", "gato", "respiratoria", "viral", "media"),
    ("flutd", "gato", "urinaria", "multifactorial", "media"),
    ("flutd_obstructivo", "gato", "urinaria", "multifactorial", "alta"),
    ("enfermedad_renal_cronica", "ambos", "urinaria", "multifactorial", "media"),
    ("diabetes_mellitus", "ambos", "endocrina", "deficit_insulina", "media"),
    ("hipertiroidismo_felino", "gato", "endocrina", "alteracion_tiroidea", "media"),
    ("otitis_externa", "ambos", "piel_oido", "multifactorial", "media"),
    ("dermatitis_pulgas", "ambos", "piel_oido", "hipersensibilidad_pulga", "baja"),
    ("sarna_sarcoptica", "perro", "piel_oido", "parasitaria", "media"),
    ("conjuntivitis", "ambos", "oftalmologica", "infecciosa_o_no", "baja"),
    ("gingivitis", "ambos", "bucodental", "placa_bacteriana", "baja"),
    ("periodontitis", "ambos", "bucodental", "placa_bacteriana", "media"),
    ("intoxicacion_rodenticidas", "ambos", "intoxicacion", "toxica", "alta"),
    ("piometra", "perro", "reproductiva", "bacteriana_post_celo", "alta")
}


# Hechos: codigo -> (enfermedad, contenido, fuente)
# MC2015 = Muñoz Rascon et al. (2015), ER2014 = Esquivel y Reyes (2014)
HECHOS = {
    "H1": ("parvovirosis",
           "Se transmite por via fecal-oral. En jovenes o inmunodeprimidos inicia con anorexia, letargo y fiebre, y en 1-2 dias evoluciona a vomitos, diarrea hemorragica y deshidratacion.",
           "MC2015, cap. 8, pp. 62-63"),
    "H2": ("panleucopenia",
           "Hay letargo, fiebre y anorexia con sed aparente pero rechazo de la bebida. Luego vomitos y diarrea profusa con deshidratacion intensa. Mas frecuente en gatos jovenes sin vacunar y en refugios.",
           "MC2015, cap. 8, p. 71"),
    "H3": ("indiscrecion_alimentaria",
           "Figura entre las causas de vomito agudo y de diarrea aguda. El vomito es un mecanismo defensivo no especifico, por lo que otros signos obligan a descartar otras causas.",
           "MC2015, cap. 10, pp. 97 y 100"),
    "H4": ("pancreatitis",
           "Vomitos intensos, dolor abdominal con postura de rezo, anorexia que empeora al comer, depresion, fiebre y deshidratacion. La obesidad y la hiperlipidemia predisponen.",
           "MC2015, cap. 10, p. 107"),
    "H5": ("parasitosis_intestinal",
           "Toxocara canis causa abdomen abultado y enteritis en cachorros. Ancylostoma caninum causa anemia con palidez de mucosas, debilidad y diarrea liquida con sangre.",
           "MC2015, cap. 9, p. 85"),
    "H6": ("moquillo",
           "Enfermedad virica que afecta los sistemas digestivo, respiratorio y nervioso. Se disemina por aerosoles. Letargo, anorexia, secrecion oculonasal, tos, vomitos y diarrea. Signos neurologicos 1-3 semanas despues; las mioclonias son muy indicativas. Se sospecha en animal joven con vacunacion deficiente.",
           "MC2015, cap. 8, pp. 64-65"),
    "H7": ("tos_perreras",
           "Multietiologica y comun en colectividades. Causa tos paroxistica, a veces descarga nasal, y en general no hay fiebre ni anorexia.",
           "MC2015, cap. 8, p. 67"),
    "H8": ("complejo_respiratorio_felino",
           "Causado por herpesvirus felino y calicivirus. Estornudos, secrecion nasal y conjuntivitis; el calicivirus ademas causa ulceras bucales. Muy contagioso en grupos de gatos.",
           "MC2015, cap. 8, p. 70"),
    "H9": ("flutd",
           "Hematuria, polaquiuria, estranguria, orinar fuera del arenero y lamido genital. Con obstruccion hay vejiga distendida y dolorosa, decaimiento y signos de insuficiencia renal aguda.",
           "MC2015, cap. 13, pp. 142-143"),
    "H10": ("enfermedad_renal_cronica",
            "Poliuria-polidipsia, anorexia, vomitos, perdida de peso, palidez de mucosas, ulceras bucales, halitosis y debilidad.",
            "MC2015, cap. 13, p. 136"),
    "H11": ("diabetes_mellitus",
            "Poliuria-polidipsia, polifagia y perdida de peso. En fase avanzada hay letargia y cataratas. En gatos son factores de riesgo la obesidad y ser macho castrado.",
            "MC2015, cap. 16, p. 184"),
    "H12": ("hipertiroidismo_felino",
            "Perdida de peso con polifagia, hiperactividad, pelo seco y alopecia en parches.",
            "MC2015, cap. 16, p. 182"),
    "H13": ("otitis_externa",
            "Es multifactorial. Exudado amarillo sugiere bacterias, marron chocolate levaduras y cerumen seco marron oscuro Otodectes. Orejas caidas y conductos estrechos predisponen.",
            "MC2015, cap. 18, pp. 242-243"),
    "H14": ("dermatitis_pulgas",
            "En perros causa prurito en grupa, flancos, cola y perine, con pulgas o sus heces. En gatos la distribucion es variable, rara vez hay prurito y son tipicas las papulas costrosas y la alopecia autoinducida.",
            "MC2015, cap. 18, p. 226"),
    "H15": ("sarna_sarcoptica",
            "Muy contagiosa. Prurito intenso que no remite en borde de la oreja, codos, esternon y abdomen, con costras y alopecia autoinducida. Son frecuentes las lesiones zoonosicas.",
            "MC2015, cap. 18, p. 226; cap. 9, p. 91"),
    "H16": ("conjuntivitis",
            "Hiperemia, edema, secrecion y prurito, sin alteracion pupilar ni de la presion ocular.",
            "MC2015, cap. 19, p. 256"),
    "H17": ("gingivitis",
            "La halitosis suele ser el primer signo de enfermedad periodontal, pero tambien puede venir de causas fuera de la boca. Encia enrojecida, edema y sangrado, reversibles con higiene oral.",
            "ER2014, cap. VI y sec. 6.4, p. 53"),
    "H18": ("periodontitis",
            "Raices expuestas, perdida de piezas, halitosis marcada, abscesos y fistulas. Casi siempre es irreversible.",
            "ER2014, secs. 6.6 y 6.6.2, pp. 60-62"),
    "H19": ("intoxicacion_rodenticidas",
            "Los anticoagulantes tienen latencia de 2-5 dias y causan hemorragia, hematomas, letargo, disnea y mucosas palidas. Otros rodenticidas causan convulsiones, temblores y ataxia.",
            "MC2015, cap. 28, p. 419"),
    "H20": ("piometra",
            "Aparece tras el celo. La abierta da descarga vaginal mucopurulenta y la cerrada no. Letargo, anorexia, vomitos y poliuria-polidipsia. Hembras enteras con celo en los ultimos 2 meses.",
            "MC2015, cap. 15, p. 168; cap. 13, p. 133")
}


# Reglas: (condiciones, conclusion), en el orden R1 a R30
# Una condicion es un predicado, ("NO", predicado) o ("O", predicado1, predicado2, ...)
# Todas las condiciones de la tupla se unen con Y
REGLAS = (
    # R1
    (("Perro", "Vomitos", "DiarreaConSangre", "Letargo", "Anorexia",
      ("O", "Cachorro", "VacunacionIncompleta")), "parvovirosis"),
    # R2
    (("Gato", "Letargo", "Anorexia", "Vomitos", "DiarreaProfusa",
      ("O", "Cachorro", "VacunacionIncompleta")), "panleucopenia"),
    # R3
    ((("O", "Vomitos", "Diarrea"), "ComioBasuraOAlimentoInadecuado",
      ("NO", "DiarreaConSangre"), ("NO", "Letargo")),
     "indiscrecion_alimentaria"),
    # R4
    (("VomitosIntensos", ("O", "PosturaRezo", "DolorAbdominal"),
      "Anorexia", "Letargo"), "pancreatitis"),
    # R5
    (("Perro", "Cachorro", "AbdomenAbultado", "Diarrea"),
     "parasitosis_intestinal"),
    # R6
    (("Perro", "DiarreaConSangre", "PalidezMucosas", "Debilidad",
      "PerdidaPeso"), "parasitosis_intestinal"),
    # R7
    (("Perro", "SecrecionOculonasal", "Tos", ("O", "Vomitos", "Diarrea"),
      "VacunacionIncompleta"), "moquillo"),
    # R8
    (("Perro", ("O", "Mioclonias", "Convulsiones", "Ataxia"),
      ("O", "SecrecionOculonasal", "Tos"), "VacunacionIncompleta"),
     "moquillo"),
    # R9
    (("Perro", "TosParoxistica", "ContactoConPerrosEnfermos",
      ("NO", "Anorexia")), "tos_perreras"),
    # R10
    (("Gato", "Estornudos", "SecrecionNasal",
      ("O", "SecrecionOcular", "OjoRojo")), "complejo_respiratorio_felino"),
    # R11
    (("Gato", "Polaquiuria", "Estranguria"), "flutd"),
    # R12
    (("Gato", "Estranguria", "NoLograOrinar", ("O", "Letargo", "Vomitos")),
     "flutd_obstructivo"),
    # R13
    (("PoliuriaPolidipsia", "PerdidaPeso", "Anorexia",
      ("O", "Vomitos", "PalidezMucosas")), "enfermedad_renal_cronica"),
    # R14
    (("PoliuriaPolidipsia", "PerdidaPeso", "Polifagia"), "diabetes_mellitus"),
    # R15
    (("Gato", "PerdidaPeso", "Polifagia",
      ("O", "Hiperactividad", "PeloSeco")), "hipertiroidismo_felino"),
    # R16
    ((("O", "SacudeCabeza", "RascaOreja"),
      ("O", "SecrecionOido", "MalOlorOido", "CerumenOscuro")),
     "otitis_externa"),
    # R17
    (("Perro", "PruritoIntenso", "LesionesLomoCola", "VenPulgasOHeces"),
     "dermatitis_pulgas"),
    # R18
    (("Gato", "PapulasCostrosas", "AlopeciaPorRascado", "VenPulgasOHeces"),
     "dermatitis_pulgas"),
    # R19
    (("Perro", "PruritoIntenso", "LesionesOrejaCodos",
      ("O", "CostrasGrisAmarillentas", "AlopeciaPorRascado")),
     "sarna_sarcoptica"),
    # R20
    ((("O", "OjoRojo", "ParpadoHinchado"), "SecrecionOcular",
      ("NO", "PupilaAlterada")), "conjuntivitis"),
    # R21
    (("Halitosis", ("O", "EnciaRoja", "EnciaInflamada", "EnciaSangra"),
      ("NO", "DientesFlojos"), ("NO", "PerdidaDientes"),
      ("NO", "RaicesExpuestas"), ("NO", "PusEnEncia")), "gingivitis"),
    # R22
    (("HalitosisMarcada", ("O", "DientesFlojos", "PerdidaDientes",
      "RaicesExpuestas", "PusEnEncia")), "periodontitis"),
    # R23
    (("AccesoARaticida", ("O", "Hemorragia", "Hematomas"),
      ("O", "Letargo", "Disnea", "PalidezMucosas")),
     "intoxicacion_rodenticidas"),
    # R24
    (("AccesoARaticida", ("O", "Convulsiones", "Temblores", "Ataxia")),
     "intoxicacion_rodenticidas"),
    # R25
    (("Perro", "HembraEntera", "CeloUltimosDosMeses", "Letargo", "Anorexia",
      ("O", "DescargaVaginalPurulenta", "Vomitos", "PoliuriaPolidipsia")),
     "piometra"),
    # R26
    (("VomitosIntensos",), "Vomitos"),
    # R27
    ((("O", "DiarreaProfusa", "DiarreaConSangre"),), "Diarrea"),
    # R28
    (("TosParoxistica",), "Tos"),
    # R29
    (("SecrecionNasal", "SecrecionOcular"), "SecrecionOculonasal"),
    # R30
    (("HalitosisMarcada",), "Halitosis")
)
