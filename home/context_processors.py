from initiative.models import Post as InitiativePost
from home.models import SocialMedia
from home.forms import ContactForm
from jalsmruti import settings


def social_media(request):
    """
    Context processor to include social media links, email, address, initiative posts count, and contact form in
    templates.

    Args:
        request: The HTTP request object.

    Returns:
        dict: Context data including social media links, counts of music links, social media links, initiative posts,
        email, address, and contact form.
    """
    social_media_object = SocialMedia.objects.all()

    # Define the social services and filter out 'Email' and 'Address' from the count
    social_services = {'Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Youtube'}
    social_media_links_count = sum(
        1 for link in social_media_object if link.name in social_services and link.url and link.url.strip()
    )

    # Retrieve 'Email' and 'Address' separately
    email = None
    address = None
    for link in social_media_object:
        if link.name == 'Email' and link.url and link.url.strip():
            email = link.url.strip()
        if link.name == 'Address' and link.url and link.url.strip():
            address = link.url.strip()

    posts_count = InitiativePost.objects.count()

    # Instantiate the contact form
    contact_form = ContactForm()

    return {
        'social_media': social_media_object,
        'social_media_links_count': social_media_links_count,
        'postsCount': posts_count,
        'email': email,
        'address': address,
        'contactForm': contact_form,
        'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
    }
