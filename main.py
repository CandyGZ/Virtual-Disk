import os
import struct

# El tamaño de un bloque en bytes
BLOCK_SIZE = 4096

class SimpleBlockStorage:
    def __init__(self, filename, num_blocks):
        self.filename = filename
        self.num_blocks = num_blocks
        self.total_size = num_blocks * BLOCK_SIZE
        
        # Crea el archivo del "disco"
        with open(self.filename, 'wb') as f:
            f.seek(self.total_size - 1)
            f.write(b'\0')
        print(f"Almacenamiento en bloques creado: {self.filename}")

    def write_block(self, block_number, data):
        """Escribe datos en un bloque específico."""
        if block_number >= self.num_blocks:
            raise IndexError("Número de bloque fuera de rango.")
        
        if len(data) > BLOCK_SIZE:
            raise ValueError("Los datos son demasiado grandes para el bloque.")
            
        offset = block_number * BLOCK_SIZE
        
        with open(self.filename, 'r+b') as f:
            f.seek(offset)
            f.write(data)
        print(f"Datos escritos en el bloque {block_number}")

    def read_block(self, block_number):
        """Lee datos de un bloque específico."""
        if block_number >= self.num_blocks:
            raise IndexError("Número de bloque fuera de rango.")
            
        offset = block_number * BLOCK_SIZE
        
        with open(self.filename, 'rb') as f:
            f.seek(offset)
            data = f.read(BLOCK_SIZE)
        return data

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Crea una instancia de almacenamiento con 10 bloques
    storage = SimpleBlockStorage("mi_disco.dat", 10)

    # Datos para escribir en el bloque 0
    message_to_write = b"Hola, este es un mensaje para el bloque 0"
    storage.write_block(0, message_to_write)

    # Lee los datos del bloque 0
    read_data = storage.read_block(0)
    print(f"Datos leídos del bloque 0: {read_data.decode('utf-8')}")

    # Escribe datos en el bloque 5
    message_to_write_2 = b"Este es el bloque 5"
    storage.write_block(5, message_to_write_2)

    # Lee los datos del bloque 5
    read_data_2 = storage.read_block(5)
    print(f"Datos leídos del bloque 5: {read_data_2.decode('utf-8')}")
