from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def envoyer_mail_html(destinataires, sujet, contexte, template_html):
    # Récupérer le contenu HTML du modèle
    contenu_html = render_to_string(template_html, contexte)
    
    # Récupérer le contenu texte brut du modèle (optionnel)
    contenu_texte = strip_tags(contenu_html)
    
    # Créer l'objet EmailMultiAlternatives
    email = EmailMultiAlternatives(sujet, contenu_texte, settings.EMAIL_HOST_USER, destinataires)
    
    # Ajouter la version HTML du message
    email.attach_alternative(contenu_html, "text/html")
    
    # Envoyer l'e-mail
    email.send()

def recevoir_mail_html(de, sujet, contexte, template_html):
    # Récupérer le contenu HTML du modèle
    contenu_html = render_to_string(template_html, contexte)
    
    # Récupérer le contenu texte brut du modèle (optionnel)
    contenu_texte = strip_tags(contenu_html)
    
    # Créer l'objet EmailMultiAlternatives
    email = EmailMultiAlternatives(sujet, contenu_texte, de, [settings.EMAIL_HOST_USER])
    
    # Ajouter la version HTML du message
    email.attach_alternative(contenu_html, "text/html")
    
    # Envoyer l'e-mail
    email.send()
