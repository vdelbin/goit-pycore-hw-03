from datetime import datetime, date, time

def get_days_from_today(date: str) -> int | None:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference = current_date - target_date
        return difference.days
    
    except (ValueError, TypeError):
        print(f"помилка формата даних {date}")
        return None

print(get_days_from_today("2001-11-09"))
print(get_days_from_today("2077-11-09"))