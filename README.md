El código simula un almacenamiento en bloques. En lugar de crear un sistema de archivos con directorios, maneja directamente los datos en bloques numerados.

SimpleBlockStorage: Esta clase actúa como el controlador del almacenamiento. Su constructor crea un archivo (mi_disco.dat) con un tamaño predefinido, que representa nuestro "disco virtual".

write_block(block_number, data): Este método escribe datos en un bloque específico. Calcula la posición exacta en el archivo (el offset) usando el número de bloque y el tamaño del bloque. Esto es clave: no busca por nombre de archivo, sino por su posición numérica, lo que lo hace muy eficiente.

read_block(block_number): Este método lee los datos de un bloque específico. Se mueve al offset correcto y lee la cantidad de bytes que corresponden al tamaño de un bloque.

Este ejemplo, aunque muy básico, ilustra el concepto principal del almacenamiento en bloques: la manipulación de datos a través de bloques numerados y no de archivos con nombres. Este es el mismo principio que utilizan los volúmenes de Amazon EBS o los discos duros internos de una computadora.
