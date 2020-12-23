from modeltranslation.translator import translator, TranslationOptions 
from product.models import Product


class ProductTranslationOptions(TranslationOptions): 
    fields = ('name', ) 
    required_languages = ('en', 'tr')
    
translator.register(Product, ProductTranslationOptions)