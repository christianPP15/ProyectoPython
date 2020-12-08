def pago(coste):
    print(f"El precio a pagar es de: {coste}")
    dinero=float(input("Introduce la cantidad a pagar: "))
    while dinero<coste:
        print("Error con su pago, intentelo de nuevo")
        dinero=float(input("Introduce la cantidad a pagar: "))
    print(f"Gracias por el pago, el cambio es de : {dinero-coste}")
