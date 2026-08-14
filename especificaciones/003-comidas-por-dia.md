# 003 - Apartado de comidas por día

- **Estado**: Borrador
- **Rama**: `spec/003-comidas-por-dia`
- **Fecha**: 2026-08-14
- **Arquitectura/tooling**: ver [CONSTITUCION.md](CONSTITUCION.md) (MVC + uv)

## Contexto

La app de gimnasio ([spec 001](001-app-gimnasio-rutinas-semanales.md)) ya
permite cargar la rutina de ejercicios de cada día hábil. El usuario quiere
sumar, junto a la rutina de cada día, un registro de las comidas planeadas
para ese mismo día, para tener en un solo lugar entrenamiento y alimentación.

## Objetivo

Registrar y consultar las comidas correspondientes a cada día hábil de
entrenamiento (lunes a viernes), asociadas a la rutina de ese día.

## Decisiones ya tomadas

- **Alcance de días**: los mismos 5 días hábiles que las rutinas (lunes a
  viernes); no se agregan sábado ni domingo.
- **Relación de datos**: las comidas cuelgan de la misma `Rutina` del día
  (no es una entidad totalmente independiente).
- **Campos mínimos**: nombre del alimento/plato y tipo de comida (desayuno,
  almuerzo, cena, snack).
- **Persistencia**: mismo criterio que los ejercicios — estado único y vivo
  por día, se sobreescribe/edita in place, sin historial de semanas
  anteriores.
- **Usuario**: uso personal, un único usuario, sin login/autenticación.

## Alcance

- Cada día hábil (L-V) tiene, además de su rutina de ejercicios, una lista
  ordenada de comidas.
- Una comida tiene como mínimo: nombre y tipo (desayuno, almuerzo, cena,
  snack).
- El usuario puede crear, editar, eliminar y listar comidas dentro del día.

### Fuera de alcance (por ahora)

- Conteo de calorías, macros (proteínas, carbohidratos, grasas) u otra
  información nutricional.
- Historial de comidas pasadas / versionado por semana.
- Comidas de sábado o domingo.
- Planificación de compras o recetas.
- Múltiples usuarios / autenticación / login.

## Historias de usuario

1. Como usuario, quiero ver las comidas planeadas para un día específico
   junto con su rutina de ejercicios.
2. Como usuario, quiero agregar una comida a un día (nombre y tipo:
   desayuno/almuerzo/cena/snack).
3. Como usuario, quiero editar una comida ya cargada en un día.
4. Como usuario, quiero eliminar una comida de un día.
5. Como usuario, quiero que las comidas cargadas se guarden y estén
   disponibles la próxima vez que entre a la app (persistencia).

## Requisitos funcionales

- **RF1**: El sistema debe permitir asociar 0..N comidas a la rutina de cada
  uno de los 5 días hábiles existentes.
- **RF2**: El sistema no debe permitir crear ni mostrar comidas para sábado
  o domingo.
- **RF3**: Una comida tiene como mínimo: nombre y tipo (uno de: desayuno,
  almuerzo, cena, snack).
- **RF4**: El usuario puede crear, editar, eliminar y listar comidas dentro
  del día.
- **RF5**: Las comidas se muestran en el orden en que fueron cargadas (campo
  `orden`), agrupadas o identificables por tipo.
- **RF6**: Los datos de comidas persisten entre sesiones (no se pierden al
  cerrar o reiniciar la app).
- **RF7**: Al editar/eliminar una comida de un día, el cambio reemplaza el
  estado anterior de ese día (no se conserva versión previa).

## Entidades de datos (Modelo)

- **Comida**: `{ id, rutina_id, nombre, tipo, orden }` — `tipo` ∈
  `{desayuno, almuerzo, cena, snack}`; relación N a 1 con `Rutina` (la misma
  entidad `Rutina` de la spec 001, 1 por día).

## Criterios de aceptación

- Dado que estoy en la página de "Martes", cuando la app carga, entonces
  veo tanto la rutina de ejercicios como las comidas planeadas para ese día.
- Dado que agrego una comida a "Jueves", cuando vuelvo a entrar a la app,
  entonces la comida sigue apareciendo en Jueves.
- Dado que intento acceder a comidas de Sábado o Domingo, entonces la app no
  ofrece esa opción.
- Dado que edito una comida, cuando guardo, entonces el cambio se refleja
  inmediatamente en la lista del día, y no queda rastro del valor anterior.
- Dado que elimino una comida, entonces deja de aparecer en el día
  correspondiente.

## Preguntas abiertas

- ¿Se necesita limitar a una comida por tipo por día (por ejemplo, un solo
  "desayuno"), o se permiten varias comidas del mismo tipo en un día?
- ¿La vista de comidas va en la misma página del día (junto a la rutina) o
  en una sección/pestaña separada dentro de esa página?
