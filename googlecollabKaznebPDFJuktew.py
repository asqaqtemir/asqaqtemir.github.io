# Қажетті кітапханаларды орнату
!pip install requests pillow fpdf

import os
import requests
from PIL import Image
from io import BytesIO
from fpdf import FPDF
import shutil
from google.colab import files  # Google Colab-тан файл жүктеу үшін кітапхана

# Суреттер мен PDF сақтау үшін папка
DOWNLOAD_FOLDER = "/content/downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def get_image_links(book_url):
    """Кітаптың URL-сынан суреттердің сілтемелерін алады."""
    try:
        # URL-ды өңдеу
        match = book_url.split("/view/")
        if len(match) < 2:
            print("URL дұрыс емес.")
            return []

        book_id = match[1].split("?")[0]
        script_url = f"https://kazneb.kz/kk/bookView/view?brId={book_id}&simple=true"

        # CORS мәселелерін айналып өту үшін прокси қолдану
        proxy_url = "https://api.allorigins.win/get?url=" + requests.utils.quote(script_url)
        response = requests.get(proxy_url)
        if response.status_code != 200:
            print("Кітап деректерін алу кезінде қате.")
            return []

        data = response.json().get("contents", "")
        if not data:
            print("Серверден бос жауап.")
            return []

        # Суреттердің сілтемелерін шығару
        links = []
        for line in data.splitlines():
            if "pages.push" in line:
                link = line.split('"')[1]
                links.append("https://kazneb.kz" + link.replace("&amp;", "&"))

        return links
    except Exception as e:
        print(f"Қате: {e}")
        return []

def download_and_create_pdf(image_links):
    """Суреттерді жүктеп, PDF құжатын жасайды."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for idx, url in enumerate(image_links):
        try:
            # Суретті жүктеу
            img_data = requests.get(url).content
            img = Image.open(BytesIO(img_data))

            # Суретті сақтау
            img_path = os.path.join(DOWNLOAD_FOLDER, f"page_{idx + 1}.png")
            img.save(img_path)

            # Суретті PDF-ке қосу
            pdf.add_page()
            pdf.image(img_path, x=10, y=10, w=180)
            print(f"{idx + 1} - бет сәтті өңделді.")
        except Exception as e:
            print(f" {idx + 1} - бет өңдеу кезінде қате шықты: {e}")

    # PDF сақтау
    pdf_path = os.path.join(DOWNLOAD_FOLDER, "document.pdf")
    pdf.output(pdf_path)
    print(f"PDF сәтті жасалды: {pdf_path}")

    return pdf_path  # PDF файлының жолын қайтару

def main():
    book_url = input("Kazneb кітаптың сілтемесін енгізіңіз: ").strip()
    print("Суреттердің сілтемелерін алу...")
    image_links = get_image_links(book_url)

    if not image_links:
        print("Суреттер табылмады. Жұмыс аяқталды.")
        return

    print(f"Барлығы {len(image_links)} сурет табылды. PDF жасау...")
    pdf_path = download_and_create_pdf(image_links)

    # PDF файлын автоматты түрде жүктеу
    print("PDF файлы дайын, жүктелуде...")
    files.download(pdf_path)  # Файлды автоматты түрде жүктеу

if __name__ == "__main__":
    main()
