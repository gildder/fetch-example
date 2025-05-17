# MCP Fetch Example

[![GitHub](https://img.shields.io/badge/GitHub-gildder-181717?style=flat&logo=github)](https://github.com/gildder)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)

Este proyecto es un ejemplo de cómo usar el cliente MCP (Model Context Protocol) con el servidor mcp-server-fetch para obtener y procesar contenido web.

## Requisitos

- Python 3.11+
- pip
- uvx (recomendado) o Docker

## Configuración

1. Clona el repositorio:
```bash
git clone https://github.com/gildder/mcp-use-tutorial.git
cd mcp-use-tutorial/fetch-example
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configura las variables de entorno:
```bash
cp .env.example .env
```
Edita el archivo `.env` y añade tu API key de OpenAI:
```
OPENAI_API_KEY=tu_api_key_aqui
```

## Uso

Para ejecutar el ejemplo:

```bash
python fetch_example.py
```

## Estructura del Proyecto

```
fetch-example/
├── .env.example         # Template para variables de entorno
├── .env                 # Variables de entorno (no incluido en git)
├── .gitignore          # Archivos ignorados por git
├── fetch_example.py    # Script principal
├── fetch_mcp.json      # Configuración del servidor MCP
└── requirements.txt    # Dependencias del proyecto
```

## Notas de Seguridad

- Nunca subas tu archivo `.env` a GitHub
- Mantén tus API keys seguras y no las compartas
- Revisa regularmente tus credenciales por seguridad

## Contribuir

1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

## Autor

👤 **Gildder**

* GitHub: [@gildder](https://github.com/gildder)

Si te gusta este proyecto, por favor dale una ⭐️!
