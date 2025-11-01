# Evaluación de Git - Trabajo en Equipo

## Primera Parte: Configuración, Roles y Contribución Individual

### Asignación de Roles

Deberán asignar los siguientes roles de acuerdo con el tamaño de su equipo, siguiendo las siguientes reglas:

- **Grupos de 4:** Un miembro será el **Líder** (crea las Issues en GitHub), otro el **Aprobador** (revisa, marca el PR como aprobado y hace merge de los cambios), y dos serán **Desarrolladores** (Devs).
- **Grupos de 3:** Un miembro asume el rol de **Líder/Aprobador** (crea las Issues en GitHub, revisa, marca el PR como aprobado y hace merge del PR), y dos serán **Desarrolladores** (Devs).

Una vez definen los roles, deberán realizar lo siguiente de acuerdo con el rol asignado:

### Rol: Líder (o Líder/Aprobador)

1. Crear el repositorio donde trabajará el equipo.
2. Añadir el primer commit con el archivo base `calculadora.py` adjunto a esta evaluación.
3. Crear los siguientes issues en GitHub (dentro del repositorio hay una sección para crearlos):
   - **Issue #1:** Implementar Descuento Fijo del 5%. Asigna al Dev 1.
   - **Issue #2:** Implementar Impuesto de Venta del 15%. Asigna al Dev 2.

### Rol: Desarrollador

1. Clonar el repositorio remoto.
2. Crear una rama respectiva al feature que le corresponde, siguiendo el formato:
   - `feature/[ISSUE-ID]-descripcion-corta`
3. Añadir el código en el sitio correspondiente dentro de la función:
   - **Dev 1:** Añade la lógica para restar el 5% (`precio = precio * 0.95`).
   - **Dev 2:** Añade la lógica para sumar el 15% (`precio = precio * 1.15`).
4. Realizar el commit con un mensaje descriptivo usando el prefijo "feat":
   - Ejemplo: `git commit -m "feat: Descripcion del feature"`
5. Hacer push al repositorio remoto.
6. Crear un Pull Request hacia `main`, nombrando al Aprobador como revisor.

## Segunda Parte: Integración, Conflictos y Resolución

### Rol: Aprobador (o Líder/Aprobador)

1. Revisar el PR del Dev 1, aprobarlo, y fusionar (merge) los cambios a `main`.
   - Este merge pasa limpio y el código de descuento queda en `main`.
2. Revisar el PR del Dev 2, y añadir el comentario en el PR que debe actualizar los últimos cambios de `main`.

### Rol: Desarrollador 2

1. Traer los cambios de `main` a la rama local para iniciar la resolución del conflicto.
2. Abre el archivo `calculadora.py`. Edita el código para eliminar los marcadores de conflicto (`<<<<<<<`, `=======`, `>>>>>>`) e integrar ambas lógicas (primero el descuento del 5% y luego