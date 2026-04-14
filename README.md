# Workshop de Automatización con Bots 🤖

Herramienta de web scraping con integración de Telegram Bot para automatizar la recopilación y distribución de datos.

---

## 📋 Requisitos

### Instalación de Python

- Descarga: https://www.python.org/downloads/
- Para usuarios de Mac: `brew install python`

### Dependencias

```bash
pip install playwright
playwright install chromium
pip3 install python-telegram-bot
pip3 install python-dotenv
```

---

## 🚀 Inicio Rápido

### Probar Scraper Localmente

```bash
python3 scrapper.py
```

### Probar Scraper con Bot

```bash
python3 scrapper_with_bot.py
```

---

## 🤖 Configuración del Bot de Telegram

### Paso 1: Obtener Token del Bot

Crea un nuevo bot con BotFather en Telegram y copia el token.

Formato de ejemplo:

```
TELEGRAM_TOKEN=63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c
```

### Paso 2: Obtener ID de Chat

1. Rellena tu token en esta URL (reemplaza `TU_TOKEN` con tu token real):

    ```
    https://api.telegram.org/botTU_TOKEN/getUpdates
    ```

2. Abre la URL en tu navegador

3. Envía un mensaje a tu bot y actualiza la página

4. La respuesta mostrará un objeto JSON con tu ID de chat

Ejemplo:

```
TELEGRAM_CHAT_ID=8795277551
```

### Paso 3: Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con:

```
TELEGRAM_TOKEN=tu_token_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui
```

---

## 📁 Estructura del Proyecto

- `scrapper.py` - Scraper web básico
- `scrapper_with_bot.py` - Scraper web con integración de bot Telegram
- `.env` - Variables de entorno (crea este archivo)

---

## 📝 Notas Importantes

- Nunca hagas commit del archivo `.env` al control de versiones
- Siempre mantén privado tu token del bot
- Usa un archivo `.gitignore` para excluir `.env`

---

---

---

# Bot Automation Workshop 🤖

Web scraping tool with Telegram Bot integration to automate data collection and distribution.

---

## 📋 Prerequisites

### Python Installation

- Download: https://www.python.org/downloads/
- For Mac users: `brew install python`

### Dependencies

```bash
pip install playwright
playwright install chromium
pip3 install python-telegram-bot
pip3 install python-dotenv
```

---

## 🚀 Quick Start

### Test Scraper Locally

```bash
python3 scrapper.py
```

### Test Scraper with Bot

```bash
python3 scrapper_with_bot.py
```

---

## 🤖 Telegram Bot Configuration

### Step 1: Get Your Bot Token

Create a new bot with BotFather on Telegram and copy the token.

Example format:

```
TELEGRAM_TOKEN=63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c
```

### Step 2: Get Your Chat ID

1. Fill in your token in this URL (replace `YOUR_TOKEN` with your actual token):

    ```
    https://api.telegram.org/botYOUR_TOKEN/getUpdates
    ```

2. Open the URL in your browser

3. Send a message to your bot and refresh the page

4. The response will show a JSON object with your chat ID

Example:

```
TELEGRAM_CHAT_ID=8795277551
```

### Step 3: Environment Variables

Create a `.env` file in the project root with:

```
TELEGRAM_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## 📁 Project Structure

- `scrapper.py` - Basic web scraper
- `scrapper_with_bot.py` - Web scraper with Telegram bot integration
- `.env` - Environment variables (create this file)

---

## 📝 Important Notes

- Never commit your `.env` file to version control
- Always keep your bot token private
- Use a `.gitignore` file to exclude `.env`

# Bot Automation Workshop

ES - Herramienta de web scraping con integración de Telegram Bot para automatizar la recopilación y distribución de datos.

EN - Web scraping tool with Telegram Bot integration to automate data collection and distribution

---

## 📋 Prerequisites / Requisitos

### Python Installation / Instalación de Python

- Download from: https://www.python.org/downloads/
- For Mac users: `brew install python`

### Dependencies / Dependencias

```bash
pip install playwright
playwright install chromium
pip3 install python-telegram-bot
pip3 install python-dotenv
```

---

## 🚀 Quick Start / Inicio Rápido

### Test Scraper Locally / Probar Scraper Localmente

```bash
python3 scrapper.py
```

### Test Scraper with Bot / Probar Scraper con Bot

```bash
python3 scrapper_with_bot.py
```

---

## 🤖 Telegram Bot Configuration / Configuración del Bot de Telegram

### Step 1: Get Your Bot Token / Paso 1: Obtener Token del Bot

Create a new bot with BotFather on Telegram and copy the token.

Example format / Formato de ejemplo:

```
TELEGRAM_TOKEN=63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c
```

### Step 2: Get Your Chat ID / Paso 2: Obtener ID de Chat

1. Fill in your token in this URL (replace `YOUR_TOKEN` with your actual token):

    Rellena tu token en esta URL (reemplaza `YOUR_TOKEN` con tu token real):

    ```
    https://api.telegram.org/botYOUR_TOKEN/getUpdates
    ```

2. Open the URL in your browser / Abre la URL en tu navegador

3. Send a message to your bot and refresh / Envía un mensaje a tu bot y actualiza

4. The response will show a JSON object with your chat ID / La respuesta mostrará un objeto JSON con tu ID de chat

Example / Ejemplo:

```
TELEGRAM_CHAT_ID=8795277551
```

### Step 3: Environment Variables / Paso 3: Variables de Entorno

Create a `.env` file in the project root with:

Crea un archivo `.env` en la raíz del proyecto con:

```
TELEGRAM_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## 📁 Project Structure / Estructura del Proyecto

- `scrapper.py` - Basic web scraper / Scraper web básico
- `scrapper_with_bot.py` - Web scraper with Telegram bot integration / Scraper web con integración de bot Telegram
- `.env` - Environment variables (create this file) / Variables de entorno (crea este archivo)

---

## 📝 Notes / Notas

- Never commit your `.env` file to version control
- Nunca hagas commit del archivo `.env` al control de versiones
- Always keep your bot token private
- Siempre mantén privado tu token del bot
