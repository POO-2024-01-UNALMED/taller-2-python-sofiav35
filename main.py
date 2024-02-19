class Asiento:
    def__init__(self,color,registro,precio):
        self.color= color
        self.registro=registro
        self.precio=precio

    def cambiarColor(self, color):
        permitidos=["amarillo","verde","blanco","negro","rojo"]
        if color in permitidos:
            self.color= color

class Motor:
    def__init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self, regisronuevo):
        self.registro=registronuevo

    def asignarTipo(self, tipo):
        if tipo=="gasolina" or tipo=="electrico":
            self.tipo=tipo

class Auto:
    cantidadCreados=0
    def__init__(self, modelo, precio, marca, motor,registro):
        self.modelo=modelo 
        self.precio=precio 
        self.asientos=asientos
        self.marca=marca
        self.motor=motor 
        self.registro=registro
    
    def cantidadAsientos(asientos)
        cantidad=0
        for i in asientos:
            if i != None:
                cantidad +=1
        return cantidad

    def verificarIntegridad()
        if self.registro==self.motor.registro:
            for asiento in self.asientos:
                if asiento is not None and asiento.registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

        
