import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Cargar variables de entorno
    load_dotenv()

    # Crear MCPClient desde el archivo de configuración
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "fetch_mcp.json")
    )

    # Crear LLM (asegúrate de tener configurada la API key de OpenAI en .env)
    llm = ChatOpenAI(model="gpt-4")

    # Crear agente con el cliente
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        # Ejecutar una consulta de ejemplo
        result = await agent.run(
            "Fetch the content from http://www.gildder.com and summarize the main features of Python",
            max_steps=30,
        )
        print(f"\nResultado: {result}")
    finally:
        # Asegurar que cerramos todas las sesiones
        if client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
