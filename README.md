# Restaurant

Bu loyiha restoran uchun mo‘ljallangan veb-ilova bo‘lib, foydalanuvchilarga menyuni ko‘rish, buyurtma berish va restoran haqida ma'lumot olish imkoniyatini beradi.

## Texnologiyalar
Loyihada quyidagi texnologiyalar ishlatilgan:
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Ma'lumotlar bazasi:** SQLite3

## O'rnatish
Loyihani o‘z kompyuteringizga yuklab olish va ishga tushirish uchun quyidagi bosqichlarni bajaring:

1. **Repodan klonlash:**
   ```bash
   git clone https://github.com/ASILBEKasilbek/Restaurant.git
   cd Restaurant
   ```

2. **Virtual muhit yaratish:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Talab qilinadigan kutubxonalarni o‘rnatish:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ma'lumotlar bazasini sozlash:**
   ```bash
   python manage.py migrate
   ```

5. **Superuser yaratish (ixtiyoriy):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Lokal serverni ishga tushirish:**
   ```bash
   python manage.py runserver
   ```

Ilova endi `http://127.0.0.1:8000/` manzilida ishga tushadi.

## Foydalanish
- **Admin panel:** `http://127.0.0.1:8000/admin/`
- **Menyu sahifasi:** `http://127.0.0.1:8000/menu/`
- **Buyurtmalar:** `http://127.0.0.1:8000/orders/`

## Hissa qo‘shish
Agar loyihaga hissa qo‘shmoqchi bo‘lsangiz:
1. Fork qiling
2. O‘z branch'ingizni yarating (`git checkout -b yangi-branch`)
3. O‘zgarishlar kiriting va commit qiling (`git commit -m 'O‘zgarish tavsifi'`)
4. GitHub'ga push qiling (`git push origin yangi-branch`)
5. Pull request yuboring

## Muallif
- **Ism:** Asilbek
- **GitHub:** [ASILBEKasilbek](https://github.com/ASILBEKasilbek)

## Litsenziya
Ushbu loyiha ochiq manba sifatida taqdim etilgan. Litsenziya shartlariga muvofiq foydalanishingiz mumkin.
