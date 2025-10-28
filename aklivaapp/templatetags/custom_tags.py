from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def get_active_class(context, url_name, css_class='active', *args, **kwargs):
    """
    Verilen URL adının mevcut sayfanın URL'i ile eşleşip eşleşmediğini kontrol eder.
    Eşleşirse belirtilen CSS sınıfını (varsayılan: 'active') döndürür.
    
    Kullanım: <a class="nav-link {% get_active_class 'url_adı' %}">...</a>
    """
    
    # 1. Mevcut sayfanın tam URL yolunu alın (örneğin: /projeler/detay-1/)
    # 'request' objesinin context içinde olduğundan emin olun.
    try:
        current_path = context['request'].path
    except KeyError:
        # Eğer 'request' context'te yoksa (nadiren olur)
        return "" 
    
    # 2. URL adından (örneğin 'projeler') tam URL yolunu tersine çevirin (örneğin: /projeler/)
    try:
        url_to_check = reverse(url_name, args=args, kwargs=kwargs)
    except NoReverseMatch:
        # Eğer verilen url_name yanlışsa
        return ""
    
    # URL'nin sonunda '/' yoksa ekleyin (tutarlılık için)
    if not url_to_check.endswith('/'):
        url_to_check += '/'

    # Mevcut URL'nin sonunda '/' yoksa ekleyin
    if not current_path.endswith('/'):
        current_path += '/'


    # --- Karşılaştırma Mantığı ---
    
    # A) Anasayfa için özel durum (tam eşleşme: sadece '/')
    if url_name == 'home' and current_path == url_to_check:
        return css_class

    # B) Kısmi eşleşme (Alt sayfalar için: /projeler/ altındaki her şey)
    # Eğer mevcut yol, kontrol edilen URL yolu ile başlıyorsa (ve anasayfa değilse)
    elif url_to_check != '/' and current_path.startswith(url_to_check):
        return css_class
        
    # C) Tam eşleşme (Diğer sayfalar için)
    elif current_path == url_to_check:
        return css_class
    
    return ""