from app import app
from models import db, Kategori, Merk, Tipe, User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()

    # Insert kategori jika belum ada
    kategori_data = [
        ("Laptop", "LTP"),
        ("Printer", "PTR"),
        ("Monitor", "MNTR"),
        ("Mouse", "MOU"),
        ("Keyboard", "KBR"),
        ("Smartphone", "HP")
    ]
    for nama, prefix in kategori_data:
        if not Kategori.query.filter_by(nama=nama).first():
            db.session.add(Kategori(nama=nama, prefix=prefix))
    db.session.commit()

    # Ambil objek kategori
    laptop = Kategori.query.filter_by(nama="Laptop").first()
    printer = Kategori.query.filter_by(nama="Printer").first()
    monitor = Kategori.query.filter_by(nama="Monitor").first()
    mouse = Kategori.query.filter_by(nama="Mouse").first()
    keyboard = Kategori.query.filter_by(nama="Keyboard").first()
    smartphone = Kategori.query.filter_by(nama="Smartphone").first()

    # Insert Merk jika belum ada
    if not Merk.query.first():
        merk_data = [
            # Laptop merk
            ("Apple", laptop.id),
            ("Acer", laptop.id),
            ("Asus", laptop.id),
            ("Lenovo", laptop.id),
            ("Hewlett Packard", laptop.id),

            # Printer merk
            ("Epson", printer.id),
            ("Hewlett Packard", printer.id),

            # Monitor merk
            ("Samsung", monitor.id),
            ("Xiaomi", monitor.id),
            ("LG", monitor.id),
            ("Lenovo", monitor.id),

            # Mouse merk
            ("Apple", mouse.id),
            ("Logitech", mouse.id),

            # Keyboard merk
            ("Logitech", keyboard.id),

            # Smartphone merk
            ("Xiaomi", smartphone.id),
            ("Apple", smartphone.id),
            ("Samsung", smartphone.id),
        ]
        for nama, kat_id in merk_data:
            if not Merk.query.filter_by(nama=nama, kategori_id=kat_id).first():
                db.session.add(Merk(nama=nama, kategori_id=kat_id))
        db.session.commit()

    # Insert Tipe jika belum ada
    if not Tipe.query.first():
        # Ambil merk untuk tiap kategori
        apple_laptop = Merk.query.filter_by(nama="Apple", kategori_id=laptop.id).first()
        asus_laptop = Merk.query.filter_by(nama="Asus", kategori_id=laptop.id).first()
        acer_laptop = Merk.query.filter_by(nama="Acer", kategori_id=laptop.id).first()
        hp_laptop = Merk.query.filter_by(nama="Hewlett Packard", kategori_id=laptop.id).first()
        lenovo_laptop = Merk.query.filter_by(nama="Lenovo", kategori_id=laptop.id).first()

        hp_printer = Merk.query.filter_by(nama="Hewlett Packard", kategori_id=printer.id).first()
        epson_printer = Merk.query.filter_by(nama="Epson", kategori_id=printer.id).first()

        apple_mouse = Merk.query.filter_by(nama="Apple", kategori_id=mouse.id).first()
        logitech_mouse = Merk.query.filter_by(nama="Logitech", kategori_id=mouse.id).first()

        logitech_keyboard = Merk.query.filter_by(nama="Logitech", kategori_id=keyboard.id).first()

        samsung_monitor = Merk.query.filter_by(nama="Samsung", kategori_id=monitor.id).first()
        xiaomi_monitor = Merk.query.filter_by(nama="Xiaomi", kategori_id=monitor.id).first()
        lenovo_monitor = Merk.query.filter_by(nama="Lenovo", kategori_id=monitor.id).first()

        apple_phone = Merk.query.filter_by(nama="Apple", kategori_id=smartphone.id).first()
        xiaomi_phone = Merk.query.filter_by(nama="Xiaomi", kategori_id=smartphone.id).first()
        samsung_phone = Merk.query.filter_by(nama="Samsung", kategori_id=smartphone.id).first()

        # Laptop tipe
        tipe_data = [
            # Apple Laptop
            ("MacBook Air M1", apple_laptop.id),
            ("MacBook Air M2", apple_laptop.id),
            ("MacBook Pro M2", apple_laptop.id),
            ("MacBook Pro M4", apple_laptop.id),

            # Asus Laptop
            ("ROG", asus_laptop.id),
            ("A1404V", asus_laptop.id),

            # Acer Laptop
            ("Nitro 5", acer_laptop.id),
            ("Predator", acer_laptop.id),
            ("Aspire 5", acer_laptop.id),
            ("Aspire Lite", acer_laptop.id),
            ("Aspire 14", acer_laptop.id),

            # Hewlett Packard Laptop
            ("Victus", hp_laptop.id),
            ("Pavilion", hp_laptop.id),
            ("15-FD0888TX", hp_laptop.id),

            # Lenovo Laptop
            ("V14", lenovo_laptop.id),
            ("LOQ", lenovo_laptop.id),
            ("T47Q", lenovo_laptop.id),
            ("Ideapad", lenovo_laptop.id),
            ("Thinkpad L14", lenovo_laptop.id),

            # Printer tipe
            ("HP DeskJet GT 5810", hp_printer.id),
            ("L5290", epson_printer.id),

            # Mouse tipe
            ("Magic Mouse", apple_mouse.id),
            ("MK220", logitech_mouse.id),

            # Keyboard tipe
            ("M220", logitech_keyboard.id),

            # Monitor tipe
            ("24 Inch", samsung_monitor.id),
            ("MI TV", xiaomi_monitor.id),
            ("MI LED", xiaomi_monitor.id),
            ("Think Vision", lenovo_monitor.id),

            # Smartphone tipe
            ("iPhone 6", apple_phone.id),
            ("iPhone 7+", apple_phone.id),
            ("iPhone 8+", apple_phone.id),
            ("iPhone 11", apple_phone.id),
            ("iPhone 13", apple_phone.id),
            ("iPhone 15", apple_phone.id),
            ("iPhone 12", apple_phone.id),

            ("Redmi Note 12", xiaomi_phone.id),
            ("9C", xiaomi_phone.id),

            ("A04", samsung_phone.id),
            ("A05", samsung_phone.id),
            ("A04S", samsung_phone.id),
        ]

        for nama, merk_id in tipe_data:
            if not Tipe.query.filter_by(nama=nama, merk_id=merk_id).first():
                db.session.add(Tipe(nama=nama, merk_id=merk_id))

        db.session.commit()

    # Insert user master jika belum ada
    if not User.query.filter_by(username="master").first():
        db.session.add(User(
            username="master",
            password=generate_password_hash("master123"),
            level="master"
        ))

    db.session.commit()
    print("Database seeded!")
