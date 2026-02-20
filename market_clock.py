from datetime import datetime
import pytz

class MarketClock:
    def __init__(self):
        # Official NSE/BSE Full Trading Holidays 2026 (Weekday closures)
        self.holidays_2026 = [
            "2026-01-26", "2026-03-03", "2026-03-26", "2026-03-31",
            "2026-04-03", "2026-04-14", "2026-05-01", "2026-05-28",
            "2026-06-26", "2026-09-14", "2026-10-02", "2026-10-20",
            "2026-11-10", "2026-11-24", "2026-12-25"
        ]
        self.tz = pytz.timezone('Asia/Kolkata')

    def is_market_open(self):
        now = datetime.now(self.tz)
        today_str = now.strftime("%Y-%m-%d")
        
        # 1. Check Weekends
        if now.weekday() >= 5: # 5=Saturday, 6=Sunday
            return False, "Weekend - Market Closed"
        
        # 2. Check Holiday List
        if today_str in self.holidays_2026:
            return False, f"Holiday ({today_str}) - Market Closed"
        
        # 3. Check Trading Hours (09:15 to 15:30)
        start_time = now.replace(hour=9, minute=15, second=0, microsecond=0)
        end_time = now.replace(hour=15, minute=30, second=0, microsecond=0)
        
        if start_time <= now <= end_time:
            return True, "Active Trading Session"
        else:
            return False, "Outside Market Hours"

# --- Execution ---
clock = MarketClock()
is_open, reason = clock.is_market_open()

print(f"--- 🕰️ MARKET CLOCK CHECK ---")
print(f"Status: {'✅ OPEN' if is_open else '💤 CLOSED'}")
print(f"Reason: {reason}")