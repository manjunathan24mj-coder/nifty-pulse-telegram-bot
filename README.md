# NIFTY PULSE Telegram Bot

Bot username: `@NiftyPulse24_bot`

## Files

- `main.py` - main bot code
- `requirements.txt` - Python packages
- `Procfile` - deploy start command
- `runtime.txt` - Python version
- `.env.example` - environment variable sample

## Environment variable

Create this variable in your hosting panel:

```env
BOT_TOKEN=your_bot_token_here
```

Do not paste your bot token directly inside `main.py`.

## Start command

```bash
python main.py
```

If your hosting platform supports Procfile workers, use:

```Procfile
worker: python main.py
```

## Local run

```bash
pip install -r requirements.txt
set BOT_TOKEN=your_bot_token_here
python main.py
```

For PowerShell:

```powershell
$env:BOT_TOKEN="your_bot_token_here"
python main.py
```
