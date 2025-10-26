# 🌌 NASA Astronomy Picture of the Day (Django App)

A simple Django web app that fetches NASA’s **Astronomy Picture of the Day (APOD)** using NASA’s official public API.  
It displays the image or video of the day, along with key details like the title, date, media type, and a short explanation.

---

## 🚀 Features

- Fetches data from [NASA's APOD API](https://api.nasa.gov/)
- Displays:
  - Picture Title  
  - Date  
  - Explanation (first 200 characters)  
  - Image or Video URL  
  - Media Type  
- Handles API errors and missing data gracefully  
- Optionally fetches APOD for a specific date (`?date=YYYY-MM-DD`)

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Django 4+**
- **Requests** (for NASA API calls)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/davidfarankin/django-nasa-apod.git
cd django-nasa-apod

