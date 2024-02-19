class Asiento:
    def __init__(self,color,registro,precio):
        self.color= color
        self.registro=registro
        self.precio=precio

    def cambiarColor(self, color):
        permitidos=["amarillo","verde","blanco","negro","rojo"]
        if color in permitidos:
            self.color= color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
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
    def __init__(self, modelo, precio, marca, motor,asientos,registro):
        self.modelo=modelo 
        self.precio=precio 
        self.asientos=asientos
        self.marca=marca
        self.motor=motor 
        self.registro=registro
    
    def cantidadAsientos(self):
        cantidad=0
        for asiento in self.asientos:
            if asiento is not None:
                cantidad +=1
        return cantidad

    def verificarIntegridad(self):
        if self.registro==self.motor.registro:
            for asiento in self.asientos:
                if asiento is not None and asiento.registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

        
