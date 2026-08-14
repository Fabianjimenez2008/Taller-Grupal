# 002 - Fondo oscuro para la app de gimnasio

- **Estado**: Borrador
- **Rama**: `spec/002-fondo-oscuro`
- **Fecha**: 2026-08-14
- **Arquitectura/tooling**: ver [CONSTITUCION.md](CONSTITUCION.md) (MVC + uv)
- **Depende de**: [001 - App de gimnasio: rutinas semanales](001-app-gimnasio-rutinas-semanales.md)

## Contexto

Hoy la app (`src/views/templates/base.html`) declara
`color-scheme: light dark` pero no fija un fondo: el navegador elige claro u
oscuro según la preferencia del sistema operativo, y por defecto suele verse
con fondo claro. El usuario quiere que la app se vea siempre con **fondo
oscuro**.

## Objetivo

Que toda la interfaz (fondo, texto, navegación, tablas, formularios y
botones) se muestre en un tema oscuro consistente y legible, en las tres
vistas existentes (`index`, `dia`, `editar`) y en cualquier vista futura que
herede de `base.html`.

## Decisiones asumidas (a confirmar)

- El fondo oscuro es **fijo**: no depende de `prefers-color-scheme` del
  sistema operativo del usuario.
- **No** se agrega en esta iteración un selector/toggle claro-oscuro; eso
  queda como posible especificación futura.
- Se reutiliza la paleta de acento ya existente (indigo `#4f46e5` en enlaces
  activos/botones) sobre una base de grises oscuros, salvo que se indique
  otra paleta.

## Alcance

- Aplica a nivel de layout compartido (`base.html`), de forma que las
  vistas hijas (`index.html`, `dia.html`, `editar.html`) hereden el tema sin
  duplicar CSS.
- Cubre: fondo de página, texto, enlaces de navegación (incluido el estado
  "activo" del día seleccionado), tabla de ejercicios, formularios de alta y
  edición, y botones (agregar, editar, eliminar).

### Fuera de alcance

- Selector de tema para el usuario (claro/oscuro/automático).
- Seguir la preferencia del sistema operativo (`prefers-color-scheme`).
- Rediseño visual más allá de pasar a fondo oscuro (tipografía, layout,
  iconografía se mantienen).

## Requisitos funcionales

- **RF1**: El fondo principal (`body`) de todas las páginas debe ser oscuro
  (no blanco), de forma fija.
- **RF2**: El texto debe tener contraste suficiente sobre el fondo oscuro
  (texto claro, legible).
- **RF3**: La navegación por día debe verse correctamente en fondo oscuro,
  conservando visible el estado "activo" del día seleccionado.
- **RF4**: La tabla de ejercicios (día) debe mostrarse con fondo oscuro,
  con bordes/separadores de fila visibles.
- **RF5**: Los formularios (inputs, textarea) y botones (agregar, editar,
  eliminar) deben ser legibles y usables sobre fondo oscuro, incluido el
  estado de foco de los campos.
- **RF6**: El tema oscuro se aplica siempre, independientemente de la
  preferencia de sistema del dispositivo (no sigue `prefers-color-scheme`).
- **RF7**: No se implementa en esta especificación ningún control para que
  el usuario cambie de tema.

## Criterios de aceptación

- Dado que abro cualquier página de la app (`/`, `/dia/<dia>`,
  `/dia/<dia>/ejercicio/<id>/editar`), entonces el fondo se ve oscuro.
- Dado que cambio la preferencia de tema del sistema operativo a "claro" y
  recargo la app, entonces la app se sigue viendo oscura (RF6).
- Dado que estoy parado en "Martes" en la navegación, entonces el día
  activo se distingue claramente del resto sobre el fondo oscuro.
- Dado que abro el formulario de agregar/editar ejercicio, entonces puedo
  leer las etiquetas/placeholders y el texto que escribo sin problemas de
  contraste.

## Preguntas abiertas

- ¿Se quiere en el futuro un toggle claro/oscuro, o el fondo oscuro fijo es
  definitivo?
