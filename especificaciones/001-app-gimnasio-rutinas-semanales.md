# 001 - App de gimnasio: rutinas semanales (lunes a viernes)

- **Estado**: Borrador
- **Rama**: `spec/001-app-gimnasio-rutinas-semanales`
- **Fecha**: 2026-08-14
- **Arquitectura/tooling**: ver [CONSTITUCION.md](CONSTITUCION.md) (MVC + uv)

## Contexto

El usuario quiere una web app personal donde ir cargando, día a día, las
rutinas de gimnasio que va programando. La carga es progresiva: no se
ingresan todas las rutinas de una sola vez, sino que se van agregando y
editando ejercicio por ejercicio con el tiempo.

## Objetivo

Registrar y consultar la rutina de ejercicios correspondiente a cada día
hábil de entrenamiento (lunes a viernes), sin incluir sábado ni domingo.

## Decisiones ya tomadas

- **Interfaz**: web app (Flask + Jinja2, siguiendo MVC).
- **Persistencia**: rutina única y viva por día — cada día se sobreescribe /
  edita in place, **no** se guarda historial de semanas anteriores.
- **Usuario**: uso personal, un único usuario, sin login/autenticación.

## Alcance

- Días soportados: Lunes, Martes, Miércoles, Jueves, Viernes (fijos, no
  configurables por el usuario).
- Sábado y domingo quedan explícitamente fuera de la aplicación.
- Una única rutina activa por día, compuesta por una lista ordenada de
  ejercicios.

### Fuera de alcance (por ahora)

- Historial de rutinas pasadas / versionado por semana.
- Múltiples usuarios / autenticación / login.
- Seguimiento de progreso en el tiempo (pesos levantados, gráficas).
- Rutinas de sábado o domingo.
- Notificaciones o recordatorios.

## Historias de usuario

1. Como usuario, quiero ver los 5 días de la semana (L-V) para elegir sobre
   cuál trabajar.
2. Como usuario, quiero agregar un ejercicio a la rutina de un día
   específico (nombre, series, repeticiones, peso, descanso, notas).
3. Como usuario, quiero editar un ejercicio ya cargado en la rutina de un
   día.
4. Como usuario, quiero eliminar un ejercicio de la rutina de un día.
5. Como usuario, quiero ver la rutina completa de un día con todos sus
   ejercicios en el orden en que los cargué.
6. Como usuario, quiero que lo que cargo se guarde y esté disponible la
   próxima vez que entre a la app (persistencia).

## Requisitos funcionales

- **RF1**: El sistema debe exponer exactamente 5 días fijos: Lunes, Martes,
  Miércoles, Jueves, Viernes.
- **RF2**: El sistema no debe permitir crear ni mostrar rutinas para sábado
  o domingo.
- **RF3**: Cada día tiene una única rutina activa, compuesta por 0..N
  ejercicios.
- **RF4**: Un ejercicio tiene como mínimo: nombre, series, repeticiones.
  Opcionalmente: peso, tiempo de descanso, notas.
- **RF5**: El usuario puede crear, editar, eliminar y listar ejercicios
  dentro de la rutina de un día.
- **RF6**: Los ejercicios se muestran en el orden en que fueron cargados
  (campo `orden`).
- **RF7**: Los datos persisten entre sesiones (no se pierden al cerrar o
  reiniciar la app).
- **RF8**: Al editar/eliminar un ejercicio de un día, el cambio reemplaza el
  estado anterior de ese día (no se conserva versión previa).

## Entidades de datos (Modelo)

- **Dia**: `{ id, nombre }` — valores fijos: `lunes`, `martes`, `miercoles`,
  `jueves`, `viernes`.
- **Rutina**: `{ id, dia_id }` — relación 1 a 1 con Día.
- **Ejercicio**: `{ id, rutina_id, nombre, series, repeticiones,
  peso (opcional), descanso (opcional), notas (opcional), orden }`

## Criterios de aceptación

- Dado que estoy en la app, cuando selecciono "Martes", entonces veo la
  rutina cargada para Martes (o vacía si no hay nada aún cargado).
- Dado que agrego un ejercicio a "Jueves", cuando vuelvo a entrar a la app,
  entonces el ejercicio sigue apareciendo en Jueves.
- Dado que intento acceder a Sábado o Domingo, entonces la app no ofrece esa
  opción (no existen esos días en la navegación).
- Dado que edito un ejercicio, cuando guardo, entonces el cambio se refleja
  inmediatamente en la lista del día, y no queda rastro del valor anterior.
- Dado que elimino un ejercicio, entonces deja de aparecer en la rutina del
  día correspondiente.

## Preguntas abiertas

- ¿Se necesita algún orden/agrupación de ejercicios por grupo muscular, o
  alcanza con una lista simple por día?
- ¿La app corre solo local (uso personal en la máquina del usuario) o se va
  a desplegar en algún servidor accesible desde el celular?
