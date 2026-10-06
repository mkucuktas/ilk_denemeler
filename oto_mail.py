import mimetypes
import smtplib
from email.message import EmailMessage
from pathlib import Path
 
# --- AYARLAR: burayı kendine göre doldur ---
GONDEREN = "mkucuktas91@gmail.com"
UYGULAMA_SIFRESI = "ufmu bvxl qohb ftcr"
ALICI = "halhizmetleri@karaman.bel.tr"
KONU = "Dosyalar ektedir"
METIN = "Haftalık belge ve bilgiler ektedir."
KLASOR = r"C:\Users\Casper\Desktop\AI\ilk_denemeler\gonderilecekler"
# -------------------------------------------
 
mesaj = EmailMessage()
mesaj["From"] = GONDEREN
mesaj["To"] = ALICI
mesaj["Subject"] = KONU
mesaj.set_content(METIN)
 
klasor = Path(KLASOR)
dosyalar = [d for d in klasor.iterdir() if d.is_file()]
 
if not dosyalar:
    print("Klasörde dosya yok, mail gönderilmedi.")
    raise SystemExit
 
for dosya in dosyalar:
    tur, _ = mimetypes.guess_type(dosya)
    ana_tur, alt_tur = (tur or "application/octet-stream").split("/")
    mesaj.add_attachment(
        dosya.read_bytes(),
        maintype=ana_tur,
        subtype=alt_tur,
        filename=dosya.name,
    )
    print("Eklendi:", dosya.name)
 
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as sunucu:
    sunucu.login(GONDEREN, UYGULAMA_SIFRESI)
    sunucu.send_message(mesaj)
 
print("Mail gönderildi.")
 