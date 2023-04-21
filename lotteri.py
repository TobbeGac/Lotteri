import random

class Lotteri:

    def __init__(self):
        
        self.list_vinster = [
            "Solstol",
            "Svettig strumpa",
            "Gethorn",
            "Leksaks Polisbil",
            "Skateboard",
            "Hårspänne",
            "Linjal",
            "2 I 1 Tvål",
            "Mössa",
            "En biltvätt på OK/Q8",
            "En Volvo",
            "En röd Ferrari",
            "2 kilo gädda",
            "Servetter",
            "Penskrin",
            "FickLampa",
            "Munkhuve jacka",
            "Snowboard",
            "Skoter 80k 800",
            "Motorcykel",
            "Sockerkaka"
]



    def get_vinst(self):
        slumptal = random.randint(0, 19)
        return self.list_vinster[slumptal] 
