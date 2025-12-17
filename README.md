# Sistema de Inventario 2025

Proyecto integrador para aprender Git y Python mediante el desarrollo modular de un sistema de inventario.

## 🎯 Objetivo

Desarrollar un sistema de inventario modular donde cada estudiante trabaja en una rama específica.

# 📋 Asignación de Ramas y Responsabilidades

## Estudiantes y sus Ramas

| Rama                    | Estudiante  | Carpeta                         | Archivos a Crear               | Descripción                                                                    |
| ----------------------- | ----------- | ------------------------------- | ------------------------------ | ------------------------------------------------------------------------------ |
| `Lizarzaburu/models`    | Lizarzaburu | `src/mi_proyecto/models/`       | `__init__.py`, `producto.py`   | Crear clase Producto con atributos: codigo, nombre, precio, stock              |
| `Pascacio/repositories` | Pascacio    | `src/mi_proyecto/repositories/` | `__init__.py`, `inventario.py` | Crear clase para gestionar el inventario (agregar, eliminar, buscar productos) |
| `Escobedo/services`     | Escobedo    | `src/mi_proyecto/services/`     | `__init__.py`, `reportes.py`   | Crear clase para generar reportes del inventario                               |
| `Mallma/utils`          | Mallma      | `src/mi_proyecto/utils/`        | `__init__.py`                  | Crear funciones auxiliares (validaciones, formateo, etc.)                      |
| `Tantavilca/tests`      | Tantavilca  | `src/mi_proyecto/tests/`        | `main.py`, `main1.py`          | Crear programas de prueba que integren todos los módulos                       |

## 📝 Instrucciones para lider Grupo

### 1. Crear el Repositorio

### 2. Clonar el Repositorio en su equipo

```bash
git clone [Nombre_repositorio]
cd sistema-inventario-2025
```

### 3. Estructura del proyecto

```
SISTEMA_INVENTARIO/
├── src/
│ └── mi_proyecto/
│ │ ├── models/ → Clases del dominio
│ │ ├── repositories/ → Acceso a datos
│ │ ├── services/ → Lógica de negocio
│ │ ├── utils/ → Funciones auxiliares
│ └── tests/ → Pruebas del sistema
│ └──README.md

solo Crear en Rama main esta estrucutura
SISTEMA_INVENTARIO/
├── src/
│ └──README.md

```

### 4. Crear ramas del proyecto

#### 4.1 Ramas del proyecto

- `main` - Rama principal (estructura proyecto) - Integración de todas las ramas
- `Lizarzaburu/models` - Implementación de modelos
- `Pascacio/repositories` - Implementación de repositorios
- `Escobedo/services` - Implementación de servicios
- `Mallma/utils` - Implementación de utilidades
- `Tantavilca/tests` - Implementación de pruebas

#### 4.2 Crear ramas del proyecto

```bash
    git branch Lizarzaburu/models
    git branch Pascacio/repositories
    git branch Escobedo/services
    git branch Mallma/utils
    git branch Tantavilca/tests
```

#### 4.3 Cambiarte a la rama

```bash
    #sintaxis
    git checkout [Nombre_repositorio]
     #Ejemplo
    git checkout Lizarzaburu/models
    git checkout Pascacio/repositories
    git checkout Mallma/utils
    git checkout Tantavilca/tests
    git checkout Escobedo/services
    git checkout main  # Volver a main
```

#### 4.4 Subir ramas al Github

```bash
    #Ejemplo
     git add .
     git commit -m "Subiendo -u rama Lizarzaburu"
     git push -u origin Lizarzaburu/models

```

### 5. Agregar colaboradores en GitHub

```bash
    •   Ve a tu repo en GitHub
    •   Settings → Collaborators → Add people
    •   Busca por usuario o email: pascacio@email.com
    •   Ellos aceptan la invitación

```

### 6. Realizar Merge

```bash
# al final cuando todos temrines de subir su parte del proyecto se hace el merge
# el merge se hace en la rama main
    git merge lizarzaburu/models
    git merge Pascacio/repositories
    git merge Mallma/utils
    git merge checkout Tantavilca/tests
    git merge checkout Escobedo/services

    # Subir main actualizado
    git push origin main
```

## 📝 Instrucciones para Estudiantes

### 1. Clonar el Repositorio en su equipo

```bash
git clone [Nombre_repositorio]
cd sistema-inventario-2025
```

### 2. Cambiar a tu Rama Asignada

```bash
# Ejemplo para Lizarzaburu:
git checkout Lizarzaburu/models
```

### 3. Crear tu Carpeta y Archivos

Según la tabla de arriba, crea SOLO los archivos de tu responsabilidad.

### 4. Desarrollar tu Código

Escribe el código Python correspondiente a tu módulo.

### 5. Hacer Commits

```bash
git add .
git commit -m "Descripción de lo que hiciste"
```

### 6. Subir Cambios

```bash
git push origin [NOMBRE-DE-TU-RAMA]
```

## ✅ Comandos de apoyo

### ver info

```bash
git status
```

### ver ramas

```bash
    # Locales
    git branch

    # Locales y remotas
    git branch -a
```

### Eliminar ramas ramas

```bash
    #En local:

    git branch -d nombre-rama

    # En GitHub:
    git push origin --delete nombre-rama

    # Forzar eliminación local (si tiene cambios sin mergear):
    git branch -D nombre-rama

```

### Limpiar consola

```bash
   clear
```

## 🎯 Fecha de Entrega

**[17/12/2025]**

## ✅ Criterios de Evaluación

```
- Código funcional
- Buenas prácticas de Python
- Commits con mensajes claros
- Documentación en el código (comentarios)
```
