import smtplib
from email.message import EmailMessage
 
# --- AYARLAR: burayı kendine göre doldur ---
GONDEREN = "mkucuktas91@gmail.com"
UYGULAMA_SIFRESI = "ufmu bvxl qohb ftcr"   # Gmail hesap şifren DEĞİL, 16 haneli uygulama şifresi
ALICI = "halhizmetleri@karaman.bel.tr"
KONU = "Test maili"
METIN = "Merhaba,\n\nBu mail Python ile otomatik olarak gönderildi."
# -------------------------------------------
 
mesaj = EmailMessage()
mesaj["From"] = GONDEREN
mesaj["To"] = ALICI
mesaj["Subject"] = KONU
mesaj.set_content(METIN)
 
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as sunucu:
    sunucu.login(GONDEREN, UYGULAMA_SIFRESI)
    sunucu.send_message(mesaj)
 
print("Mail gönderildi.")
 