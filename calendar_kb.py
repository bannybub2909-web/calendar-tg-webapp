from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import calendar
from datetime import datetime

def calendar_keyboard(year: int, month: int):
    kb = []

    kb.append([
        InlineKeyboardButton(
            text=f"{calendar.month_name[month]} {year}",
            callback_data="ignore"
        )
    ])

    kb.append([
        InlineKeyboardButton(text=day, callback_data="ignore")
        for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    ])

    month_cal = calendar.monthcalendar(year, month)
    for week in month_cal:
        row = []
        for day in week:
            if day == 0:
                row.append(InlineKeyboardButton(text=" ", callback_data="ignore"))
            else:
                date = f"{year}-{month:02d}-{day:02d}"
                row.append(
                    InlineKeyboardButton(text=str(day), callback_data=f"date:{date}")
                )
        kb.append(row)

    kb.append([
        InlineKeyboardButton(text="⬅️", callback_data="prev"),
        InlineKeyboardButton(text="➡️", callback_data="next"),
    ])

    return InlineKeyboardMarkup(inline_keyboard=kb)
