# Trabajo Práctico: Funciones en Python

## Descripción
Este proyecto implementa 5 funciones en Python como ejercicio educativo para practicar la definición y uso de funciones con diferentes tipos de parámetros: posicionales, keyword-only, con valores por defecto y parámetros opcionales. Cada función resuelve un problema matemático o de conversión sencillo.

## Tecnologías utilizadas
- **Python 3.x**: lenguaje de programación principal utilizado para implementar las funciones y la lógica del proyecto.

## Características principales
- Suma de dos números recibidos por posición.
- Resta de dos números con parámetros nombrados obligatorios (keyword-only).
- Cálculo de precio final aplicando IVA con valor por defecto del 21%.
- Conversión de metros a centímetros (por defecto) o milímetros.
- Cálculo de área de rectángulo, asumiendo cuadrado si no se indica la altura.

## Arquitectura del proyecto
Proyecto simple de un solo archivo (`funciones.py`) que contiene las 5 funciones definidas. No hay separación en capas (frontend/backend) al ser un ejercicio de consola/educativo.

## Estructura del proyecto
```
trabajoPracticoFunciones/
├── funciones.py   # Contiene las 5 funciones implementadas
└── README.md      # Este archivo de documentación
```

## Requisitos previos
- Python 3.x instalado en el sistema.

## Instalación
1. Clonar o descargar el repositorio.
2. Ingresar a la carpeta del proyecto:
   ```bash
   cd trabajoPracticoFunciones
   ```

## Configuración
No se requiere configuración adicional. No hay variables de entorno, archivos `.env`, bases de datos ni servicios externos.

## Ejecución
Para probar las funciones, ejecutar Python en modo interactivo o crear un script de prueba:

```bash
python -c "from funciones import *; print(suma(3, 5)); print(resta(minuendo=10, sustraendo=3)); print(precio_final(1000)); print(convertir_metros(2)); print(area_rectangulo(5))"
```

O usar un archivo de prueba:
```bash
python test_funciones.py
```

## Funcionamiento general
1. El usuario importa las funciones desde `funciones.py`.
2. Llama a cada función con los argumentos correspondientes.
3. Las funciones procesan los parámetros y devuelven el resultado calculado.

## Funciones o mecanismos importantes

### `suma(a, b)`
Recibe dos números por posición y devuelve su suma.
```python
suma(3, 5)  # 8
```

### `resta(*, minuendo, sustraendo)`
Usa parámetros keyword-only (el `*` obliga a nombrar los argumentos) para evitar confusiones en el orden.
```python
resta(minuendo=10, sustraendo=3)  # 7
```

### `precio_final(precio, iva=21)`
Aplica IVA al precio. El IVA por defecto es 21%.
```python
precio_final(1000)      # 1210.0 (IVA 21%)
precio_final(1000, 10)  # 1100.0 (IVA 10%)
```

### `convertir_metros(metros, unidad="cm")`
Convierte metros a centímetros por defecto, o a milímetros si se especifica `"mm"`.
```python
convertir_metros(2)        # 200 (cm)
convertir_metros(2, "mm")  # 2000 (mm)
```

### `area_rectangulo(base, altura=None)`
Calcula el área. Si no se pasa `altura`, asume que es un cuadrado (`altura = base`).
```python
area_rectangulo(5)     # 25 (cuadrado 5x5)
area_rectangulo(5, 3)  # 15 (rectángulo 5x3)
```

## Pruebas realizadas
| Prueba | Acción | Resultado esperado | Resultado |
|--------|--------|-------------------|-----------|
| 1 | `suma(3, 5)` | 8 | OK |
| 2 | `resta(minuendo=10, sustraendo=3)` | 7 | OK |
| 3 | `precio_final(1000)` | 1210.0 | OK |
| 4 | `precio_final(1000, 10)` | 1100.0 | OK |
| 5 | `convertir_metros(2)` | 200 | OK |
| 6 | `convertir_metros(2, "mm")` | 2000 | OK |
| 7 | `area_rectangulo(5)` | 25 | OK |
| 8 | `area_rectangulo(5, 3)` | 15 | OK |

## Problemas conocidos
- No se validan tipos de entrada (ej. pasar strings en lugar de números causa error).
- No hay tests automatizados formales (pytest/unittest).

## Mejoras futuras
- Agregar validación de tipos y manejo de errores.
- Incluir tests automatizados con `pytest`.
- Añadir docstrings tipo Google/NumPy a cada función.
- Crear una pequeña CLI para probar las funciones interactivamente.

## Autores y responsabilidades
| Integrante | Responsabilidad |
|------------|-----------------|
| Estudiante | Desarrollo de funciones y documentación |

## Repositorio
El código fuente se encuentra en este repositorio local.

## Licencia
Este proyecto fue desarrollado con fines educativos.

## Conclusión
Este trabajo práctico permitió repasar conceptos fundamentales de funciones en Python: parámetros posicionales, keyword-only (`*`), valores por defecto, parámetros opcionales (`None` como sentinel) y retorno de valores. Se aplicó tipado implícito y se verificó el funcionamiento mediante pruebas manuales. Estos conceptos son base para proyectos más complejos y reutilizables.

## GitHub Helpers
- [GitDiagram](https://gitdiagram.com/enzo-salveem/trabajoPracticoFunciones)
- [Gitingest](https://gitingest.com/https://github.com/enzo-salveem/trabajoPracticoFunciones)
- [RepoGrep](https://repogrep.com/enzo-salveem/trabajoPracticoFunciones)
- [DeepWiki](https://deepwiki.com/enzo-salveem/trabajoPracticoFunciones)
- [GitHub1s](https://github1s.com/enzo-salveem/trabajoPracticoFunciones/tree/main)




