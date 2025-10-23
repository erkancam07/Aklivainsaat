from django.shortcuts import render

from urllib.parse import urlparse, parse_qs

from django.core.serializers import serialize
import json

def parse_youtube_link(raw_url):
    parsed = urlparse(raw_url)
    query = parse_qs(parsed.query)
    video_id = query.get("v", [""])[0]
    embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1&rel=0&playsinline=1"
    return {
        "video_id": video_id,
        "video_url": embed_url
    }


def index(request):
    slides = [
        {
            "title": "Revapark Konakları",
            "subtitle": "Lansman Satışları Başladı",
            "button": "Projeyi İncele",
            "video_url": "https://www.youtube.com/embed/BF9hVS55sIM?autoplay=1&mute=1&rel=0&playsinline=1"
        },
        {
            "title": "Revapark Premium",
            "subtitle": "Yeni Etap Satışları Başladı",
            "button": "Detayları Gör",
            "video_url": "https://www.youtube.com/embed/DXzDS2IO6aA?autoplay=1&mute=1&rel=0&playsinline=1"
        }
    ]
    kurumsal_slider_images = [
        'img/kurumsal_slider.png',
        'img/slider1.jpg',
        'img/slider2.jpg',
        'img/slider3.jpg',
    ]
    
    """  
    Bursı veritabanı için
    video_data = parse_youtube_link("https://www.youtube.com/watch?v=FbYyDF3EPuA")
        medya_videolar = [
        {
            "baslik": "Tanıtım Videosu",
            "video_id": video_data["video_id"],
            "video_url": video_data["video_url"],
            "ikon": "takvim-ikonu.png",
            "metin": "Açıklama"
        }, """

    medya_videolar = [
    {
        "baslik": "II Armağan Sitesi",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=DXzDS2IO6aA&t=6s")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=DXzDS2IO6aA&t=6s")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": " Yükleme Tarihi  "
    },
    {
        "baslik": "Şehri Sultan Sarayları",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=u2Ow1p3zjj4&t=31s")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=u2Ow1p3zjj4&t=31s")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Şehri Sultan Sarayları"
    },
    {
        "baslik": "Akliva İnşaat",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=BF9hVS55sIM")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=BF9hVS55sIM")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Adliye Konakları"
    },
     {
        "baslik": "Avrasya Şehircilik",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=WWfWR-8vml4")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=WWfWR-8vml4")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Adliye Konakları"
    },
     {
        "baslik": "Armağan Siteleri",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Akliva İnşaat"
    },
    {
        "baslik": "Armağan Siteleri",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Akliva İnşaat"
    },
    {
        "baslik": "Armağan Siteleri",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Akliva İnşaat"
    },
    {
        "baslik": "Armağan Siteleri",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Akliva İnşaat"
    },
    {
        "baslik": "Armağan Siteleri",
        "video_id": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_id"],
        "video_url": parse_youtube_link("https://www.youtube.com/watch?v=jVWw-x7GC3Q")["video_url"],
        "ikon": "takvim-ikonu.png",
        "metin": "Akliva İnşaat"
    },
]
    haberler = [
        {
            "resim": "haber_gorsel1.png",
            "konum": "Karatay, Konya",
            "baslik": "Revapark Projesi Konya Karatay'da Tamamlanıyor!",
            "icerik": "Akliva Yapı, Konya’nın gelişen bölgelerinden Karatay’da hayata geçirdiği Revapark Konut Projesinde sona yaklaşıyor....",
        },
        {
            "resim": "haber_gorseli2.png",
            "konum": "Karatay, Konya",
            "baslik": "Beyza Sitesi Projesi Konya Selçuklu'da Tamamlanıyor!",
            "icerik": "Akliva Yapı, Konya’nın gelişen bölgelerinden Karatay’da hayata geçirdiği Revapark Konut Projesinde sona yaklaşıyor....",
        },
         {
            "resim": "haber_gorsel1.png",
            "konum": "Karatay, Konya",
            "baslik": "Revapark Projesi Konya Karatay'da Tamamlanıyor!",
            "icerik": "Akliva Yapı, Konya’nın gelişen bölgelerinden Karatay’da hayata geçirdiği Revapark Konut Projesinde sona yaklaşıyor....",
        },
        {
            "resim": "haber_gorseli2.png",
            "konum": "Karatay, Konya",
            "baslik": "Beyza Sitesi Projesi Konya Selçuklu'da Tamamlanıyor!",
            "icerik": "Akliva Yapı, Konya’nın gelişen bölgelerinden Karatay’da hayata geçirdiği Revapark Konut Projesinde sona yaklaşıyor....",
        },
    ]
    gorusler = [
    {
        "ad": "Ali Yılmaz",
        "meslek": "Mimar",
        "sehir": "Konya",
        "mesaj": "Akliva’dan aldığımız daire hem konumu hem de kalitesiyle tam aradığımız gibiydi. Teslim süreci sorunsuz ilerledi, her şey söz verdikleri gibi oldu.",
        "tarih": "Ekim 2025",
        "yildiz_sayisi": 4
    },
    {
        "ad": "Ayşe Demir",
        "meslek": "İnşaat Mühendisi",
        "sehir": "Antalya",
        "mesaj": "Proje kalitesi ve teslim süreci beklentimizin çok üzerindeydi. Akliva ekibine teşekkür ederiz.",
        "tarih": "Eylül 2025",
        "yildiz_sayisi": 4
    },
    {
        "ad": "Mehmet Kaya",
        "meslek": "Avukat",
        "sehir": "İstanbul",
        "mesaj": "İnşaat kalitesi ve müşteri iletişimi çok başarılıydı. Her aşamada bilgilendirildik.",
        "tarih": "Ağustos 2025",
        "yildiz_sayisi": 4
    },
    {
        "ad": "Ali Yılmaz",
        "meslek": "Mimar",
        "sehir": "Konya",
        "mesaj": "Akliva’dan aldığımız daire hem konumu hem de kalitesiyle tam aradığımız gibiydi. Teslim süreci sorunsuz ilerledi, her şey söz verdikleri gibi oldu.",
        "tarih": "Ekim 2025",
        "yildiz_sayisi": 4
    },
    {
        "ad": "Ayşe Demir",
        "meslek": "İnşaat Mühendisi",
        "sehir": "Antalya",
        "mesaj": "Proje kalitesi ve teslim süreci beklentimizin çok üzerindeydi. Akliva ekibine teşekkür ederiz.",
        "tarih": "Eylül 2025",
        "yildiz_sayisi": 4
    },
    {
        "ad": "Mehmet Kaya",
        "meslek": "Avukat",
        "sehir": "İstanbul",
        "mesaj": "İnşaat kalitesi ve müşteri iletişimi çok başarılıydı. Her aşamada bilgilendirildik.",
        "tarih": "Ağustos 2025",
        "yildiz_sayisi": 4
    },
]
    ortaklar = [
        {"ad": "Firma A", "logo_url": "/static/img/is_ortaklari_card.svg"},
        {"ad": "Firma B", "logo_url": "/static/img/is_ortaklari_card.svg"},
        {"ad": "Firma C", "logo_url": "/static/img/is_ortaklari_card.svg"},
         {"ad": "Firma A", "logo_url": "/static/img/is_ortaklari_card.svg"},
        {"ad": "Firma B", "logo_url": "/static/img/is_ortaklari_card.svg"},
        {"ad": "Firma C", "logo_url": "/static/img/is_ortaklari_card.svg"},
    ]
    sertifikalar = [
        {"ad": "ISO 9001", "img_url": "/static/img/sertifikalar_card.svg"},
        {"ad": "CE Belgesi", "img_url": "/static/img/sertifikalar_card.svg"},
        {"ad": "ISO 9001", "img_url": "/static/img/sertifikalar_card.svg"},
        {"ad": "CE Belgesi", "img_url": "/static/img/sertifikalar_card.svg"},
        {"ad": "ISO 9001", "img_url": "/static/img/sertifikalar_card.svg"},
        {"ad": "CE Belgesi", "img_url": "/static/img/sertifikalar_card.svg"},
    ]
    

   
    
    context = {
        'slider_ids': range(1, 7),
        'slides': slides,
        'slider_images': kurumsal_slider_images,
        'medya_videolar': medya_videolar,
        "haberler":haberler,
        # "gorusler": gorusler,
        "gorusler": gorusler,
        "gorusler_json": json.dumps(gorusler),
        "range5": range(5),
        "ortaklar": ortaklar,
        "sertifikalar": sertifikalar,
    }

    return render(request, "index.html", context)


def kurumsal(request):
    return render(request, "kurumsal.html")

def projeler(request):
    return render(request, "projeler.html")

def haberler(request):
    return render(request, "haberler.html")

def yatirim(request):
    return render(request, "yatirim.html")

def iletisim(request):
    return render(request, "iletisim.html")
