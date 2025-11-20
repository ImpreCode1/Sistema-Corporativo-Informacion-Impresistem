# Sistema Corporativo de Información

Este repositorio contiene la arquitectura completa del Sistema Corporativo de Información basado en microservicios. El proyecto está diseñado para centralizar la información de empleados, clientes y procesos administrativos de la organización.

## 🏗️ Arquitectura

La plataforma está compuesta por:

- **API Gateway (Nginx)**  
  Maneja el enrutamiento hacia los microservicios internos.

- **svc-empleados**  
  Microservicio encargado de la gestión de empleados, directorio, exportaciones CSV y evaluaciones.

- **svc-clientes**  
  Servicio encargado de la gestión de clientes y entidades externas asociadas.

- **ui-empleados**  
  Interfaz de usuario para administración y consulta de empleados.

## 🚀 Despliegue

Para levantar todo el entorno:

```bash
docker compose up -d --build
