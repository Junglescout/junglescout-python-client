from enum import Enum


class Marketplace(Enum):
    US = ("us", ["Appliances", "Arts, Crafts & Sewing", "Automotive", "Baby", "Beauty & Personal Care", "Camera & Photo", "Cell Phones & Accessories", "Clothing, Shoes & Jewelry", "Computers & Accessories", "Electronics", "Grocery & Gourmet Food",
          "Health & Household", "Home & Kitchen", "Industrial & Scientific", "Kitchen & Dining", "Musical Instruments", "Office Products", "Patio, Lawn & Garden", "Pet Supplies", "Software", "Sports & Outdoors", "Tools & Home Improvement", "Toys & Games", "Video Games"])
    UK = ("uk", ["Automotive", "Baby Products", "Beauty", "Business, Industry & Science", "Clothing", "Computers & Accessories", "DIY & Tools", "Electronics & Photo", "Garden & Outdoors", "Grocery", "Health & Personal Care",
          "Home & Kitchen", "Jewellery", "Large Appliances", "Lighting", "Luggage", "Musical Instruments & DJ", "PC & Video Games", "Pet Supplies", "Shoes & Bags", "Sports & Outdoors", "Stationery & Office Supplies", "Toys & Games", "Watches"])
    CA = ("ca", ["Automotive", "Baby", "Beauty & Personal Care", "Clothing & Accessories", "Electronics", "Grocery & Gourmet Food", "Health & Personal Care", "Industrial & Scientific", "Jewelry", "Luggage & Bags",
          "Musical Instruments, Stage & Studio", "Office Products", "Patio, Lawn & Garden", "Pet Supplies", "Shoes & Handbags", "Sports & Outdoors", "Tools & Home Improvement", "Toys & Games", "Watches"])
    DE = ("de", ["Auto & Motorrad", "Baby", "Baumarkt", "Beauty", "Bekleidung", "Beleuchtung", "Bücher", "Bürobedarf & Schreibwaren", "Computer & Zubehör", "DVD & Blu-ray", "Drogerie & Körperpflege", "Elektro-Großgeräte", "Elektronik & Foto", "Fremdsprachige Bücher", "Games", "Garten",
          "Gewerbe, Industrie & Wissenschaft", "Haustier", "Kamera & Foto", "Koffer, Rucksäcke & Taschen", "Küche, Haushalt & Wohnen", "Lebensmittel & Getränke", "Musikinstrumente & DJ-Equipment", "Schmuck", "Schuhe & Handtaschen", "Software", "Spielzeug", "Sport & Freizeit", "Uhren"])
    FR = ("fr", ["Animalerie", "Auto & Moto", "Bagages", "Beauté & Parfum", "Bijoux", "Bricolage", "Bébé & Puériculture", "Chaussures & Sacs", "Commerce, Industrie & Science", "Cuisine & Maison", "DVD & Blu-ray", "Epicerie", "Fournitures de bureau", "Gros électroménager",
          "High-tech", "Hygiène & Santé", "Informatique", "Instruments de musique & Sono", "Jardin", "Jeux & Jouets", "Jeux vidéo", "Livres", "Livres anglais & étrangers", "Logiciels", "Luminaires & Eclairage", "Montres", "Sports & Loisirs", "Vêtements"])
    IN = ("in", ["Baby", "Baby Products", "Bags, Wallets & Luggage", "Beauty", "Books", "Car & Motorbike", "Clothing & Accessories", "Electronics", "Gift Cards", "Grocery & Gourmet Foods", "Health & Personal Care", "Home & Kitchen",
          "Industrial & Scientific", "Jewellery", "Movies & TV Shows", "Music", "Musical Instruments", "Office Products", "Pet Supplies", "Shoes & Handbags", "Software", "Sports, Fitness & Outdoors", "Toys & Games", "Video Games", "Watches"])
    IT = ("it", ["Abbigliamento", "Alimentari e cura della casa", "Auto e Moto", "Bellezza", "Buoni regalo", "CD e Vinili", "Casa e cucina", "Commercio, Industria e Scienza", "Elettronica", "Fai da te", "Film e TV", "Giardino e giardinaggio",
          "Giochi e giocattoli", "Gioielli", "Illuminazione", "Informatica", "Kindle Store", "Libri", "Libri in altre lingue", "Orologi", "Prima infanzia", "Salute e cura della persona", "Scarpe e borse", "Software", "Sport e tempo libero", "Valigeria", "Videogiochi"])
    ES = ("es", ["Apps y Juegos", "Bebé", "Belleza", "Bricolaje y herramientas", "Coche y moto", "Deportes y aire libre", "Electrónica", "Equipaje", "Hogar y cocina", "Iluminación", "Industria, empresas y ciencia", "Informática",
          "Instrumentos musicales", "Jardín", "Joyería", "Juguetes y juegos", "Libros", "Oficina y papelería", "Películas y TV", "Relojes", "Ropa", "Salud y cuidado personal", "Software", "Tienda Kindle", "Videojuegos", "Zapatos y complementos"])
    MX = ("mx", ["Bebé", "Deportes y Aire Libre", "Electrónicos", "Herramientas y Mejoras del Hogar", "Hogar y Cocina", "Industria, Empresas y Ciencia", "Instrumentos Musicales",
          "Juguetes y Juegos", "Libros", "Música", "Oficina y papelería", "Ropa, Zapatos y Accesorios", "Salud, Belleza y Cuidado Personal", "Software", "Tienda Kindle", "Videojuegos"])
    JP = ("jp", ["DIY・工具・ガーデン", "おもちゃ", "シューズ&バッグ", "ジュエリー", "スポーツ&アウトドア", "ドラッグストア", "ビューティー", "ベビー&マタニティ", "ペット用品",
          "ホビー", "ホーム&キッチン", "大型家電", "家電&カメラ", "文房具・オフィス用品", "服&ファッション小物", "産業・研究開発用品", "腕時計", "車&バイク", "食品・飲料・お酒"])

    @property
    def country_code(self):
        return self.value[0]

    @property
    def categories(self):
        return self.value[1]
