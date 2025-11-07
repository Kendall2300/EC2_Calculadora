# calculadora.py

def aplicar_reglas_compra(precio):
    """
    Aplica todas las reglas de negocio al precio de compra.
    """
    
    # Ambos desarrolladores DEBEN MODIFICAR la línea inmediatamente debajo de este comentario.
    precio = precio * 1.15
    
    return precio

# Inicia la ejecución de prueba
if __name__ == '__main__':
    precio_inicial = 100
    precio_final = aplicar_reglas_compra(precio_inicial)
    print(f"Precio inicial: {precio_inicial}. Precio final: {precio_final}")