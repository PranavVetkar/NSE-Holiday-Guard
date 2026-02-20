# 🕰️ NSE Holiday Guard

**NSE Holiday Guard** is a lightweight Python utility designed to track the Indian stock market (NSE/BSE) status in real-time. It automatically detects if the market is open or closed based on official trading hours, weekends, and the 2026 NSE holiday calendar.

## 🚀 Features

- **2026 Holiday Integration**: Pre-configured with all official NSE/BSE holidays for 2026.
- **Trading Hours Check**: Validates against the standard session (09:15 AM to 03:30 PM IST).
- **Weekend Detection**: Automatically identifies Saturdays and Sundays.
- **Timezone Aware**: Uses `Asia/Kolkata` timezone to ensure accuracy regardless of where the script is hosted.

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/PranavVetkar/NSE-Holiday-Guard.git
cd NSE-Holiday-Guard
```

### 2. Install Dependencies
This project requires `pytz` for timezone management.
```bash
pip install pytz
```

## 💻 Usage

Run the script to check the current market status:

```bash
python market_clock.py
```

## 📊 Example Output

When you run the script, you will see an output similar to this:

```text
--- 🕰️ MARKET CLOCK CHECK ---
Status: 💤 CLOSED
Reason: Outside Market Hours
```

## 📅 Supported Holidays (2026)
The script includes logic for the following major trading holidays:
- Republic Day
- Holi
- Eid-ul-Fitr
- Ambedkar Jayanti
- Maharashtra Day
- Independence Day
- Gandhi Jayanti
- Diwali
- Christmas
- *And more...*

---
Built for Systematic Trading precision. 📈
