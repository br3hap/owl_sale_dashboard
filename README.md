# Ventas Dashboard / Vista de Tarjetas - Odoo 18

Este módulo añade una **vista tipo tarjetas** con indicadores de ventas en la vista lista del módulo de ventas de Odoo. Ideal para visualizar métricas clave de forma rápida y visual dentro de la interfaz estándar.

## 📊 Características

- Visualización de tarjetas con indicadores personalizados en la vista de lista de **Pedidos de Venta**.
- Integración total con OWL y los estilos del backend de Odoo.
- Configuración por usuario desde la vista de ajustes (`res.users`).
- Módulo ligero y fácil de extender para incluir nuevos KPIs.

## 🧩 Dependencias

Este módulo depende de los siguientes módulos estándar de Odoo:

- `sale_management`
- `sale`
- `base`

## 📦 Instalación

1. Clona o descarga el repositorio en el directorio de addons de tu instancia Odoo.
2. Ve a **Aplicaciones** y actualiza la lista.
3. Busca **Ventas Dashboard / Vista de tarjetas** e instala el módulo.

## 🖼️ Vista previa

> (Opcional) Puedes incluir aquí una imagen tipo screenshot mostrando cómo se ven las tarjetas en la vista lista.

## 🛠 Archivos incluidos

- `views/res_users_views.xml`: configuración por usuario.
- `views/sale_order_views.xml`: herencia y modificación de la vista de lista de ventas.
- Archivos OWL y XML en `static/src` para renderizar las tarjetas.

## 🙋 Autor

Desarrollado por **Breithner Aquituari**

## 📝 Licencia

Licencia: **LGPL-3.0**
