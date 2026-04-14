import asyncio
import re
from playwright.async_api import async_playwright


URL = "https://entradas.roigarena.com/roigarena/select/2801703?sessionPreviewToken=AK6G3EN576M3M2OX&viewCode=V_blockmap_view"


async def obtener_entradas():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print(f"🔗 Abriendo página...")
        await page.goto(URL, wait_until="domcontentloaded", timeout=30000)

        try:
            boton_cookies = await page.wait_for_selector(
                "text=Aceptar todas",
                timeout=8000
            )
            await boton_cookies.click()
            print("✅ Cookies aceptadas")
            await page.wait_for_timeout(1500)
        except Exception:
            print("ℹ️  No apareció el banner de cookies (puede que ya esté aceptado)")

        print("⏳ Esperando contenido dinámico...")
        await page.wait_for_timeout(5000)

        try:
            await page.wait_for_selector(
                "[class*='block'], [class*='sector'], [class*='area'], svg",
                timeout=15000
            )
        except Exception:
            print("⚠️  No se encontró un selector de mapa concreto; continuando con el HTML actual")

        contenido = await page.inner_text("body")

        patron = re.compile(
            r"([^\n\r\t]{2,80}?)\s*[-–—]\s*(\d+)\s+entradas?\s+disponibles?",
            re.IGNORECASE
        )
        resultados = patron.findall(contenido)

        patron_simple = re.compile(
            r"(\d+)\s+entradas?\s+disponibles?",
            re.IGNORECASE
        )
        resultados_simples = patron_simple.findall(contenido)

        print("\n" + "="*50)
        print("       ENTRADAS DISPONIBLES")
        print("="*50)

        if resultados:
            for nombre, numero in resultados:
                nombre = nombre.strip()
                print(f"  🎟️  {nombre} - {numero} entradas disponibles")
        elif resultados_simples:
            print("  (No se encontró nombre de zona, solo cantidades)\n")
            for numero in resultados_simples:
                print(f"  🎟️  {numero} entradas disponibles")
        else:
            print("  ❌ No se encontraron entradas disponibles en el texto de la página.")
            print("\n  📋 Fragmento del contenido recibido (debug):")

            lineas = [l.strip() for l in contenido.splitlines() if l.strip()]
            for linea in lineas[:40]:
                print(f"     {linea}")

        print("="*50)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(obtener_entradas())
