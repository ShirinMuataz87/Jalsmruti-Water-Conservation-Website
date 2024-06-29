import requests

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.views import APIView

from home.forms import ContactForm
from home.models import HomeSection, Fact, AboutPage
from home.throttling import ContactFormRateThrottleMixin
from initiative.models import Post as InitiativePost
from insight.models import Post as InsightPost
from event.models import Post as EventPost
from django.conf import settings
from utility.base_views import BaseView


class ContactFormView(ContactFormRateThrottleMixin, APIView):
    """
    View to handle contact form submission with rate throttling and reCAPTCHA validation.

    Methods:
        post(request, *args, **kwargs): Handle POST request for the contact form submission.
            - Checks for throttling limits.
            - Validates and saves the contact form data.
            - Sets success or error messages.
            - Redirects to the original page with the footer anchor or to the home page with the footer anchor.

    Attributes inherited from APIView:
        request (HttpRequest): The HTTP request object.
        args (list): Additional positional arguments.
        kwargs (dict): Additional keyword arguments.
    """
    def handle_recaptcha(self, request):
        """
        Handle Google reCAPTCHA validation.

        Args:
            request: The HTTP request object.

        Returns:
            bool: True if reCAPTCHA is valid, False otherwise.
        """
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        return result.get('success', False) and result.get('score', 0) > 0.65

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for the contact form submission.

        Args:
            request (HttpRequest): The HTTP request object.
            *args (list): Additional positional arguments.
            **kwargs (dict): Additional keyword arguments.

        Returns:
            HttpResponse: Redirects to the original page with the footer anchor or to the home page with the footer anchor.
        """
        self.check_throttles(request)

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            if settings.USE_RECAPTCHA:
                if not self.handle_recaptcha(request):
                    messages.error(request, 'Unable to send message. Please try again later.')
                    next_url = request.META.get('HTTP_REFERER', reverse('home:index')) + '#footer'
                    return redirect(next_url)
            contact_form.save()
            messages.success(request, "Message submitted successfully!")
            # Redirect to the original page or home page with the footer anchor
            next_url = request.META.get('HTTP_REFERER', reverse('home:index')) + '#footer'
            return redirect(next_url)
        else:
            messages.error(request, 'Form validation failed. Please correct the errors below.')
            # Redirect back to the form page with the errors
            next_url = request.META.get('HTTP_REFERER', reverse('home:index')) + '#footer'
            return redirect(next_url)


class IndexView(BaseView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the index page.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered index page.
        """
        try:
            home = HomeSection.objects.get(name="Home Section")
        except HomeSection.DoesNotExist:
            home = None
        try:
            facts = Fact.objects.all()
        except Fact.DoesNotExist:
            facts = None

        image_url = home.image.url if home and home.image else settings.DEFAULT_IMAGE_URL
        self.meta = self.get_meta(home.title if home else "JalSmruti",
                                  home.description if home else "",
                                  home.keywords if home else "",
                                  '/', image_url)

        initiatives = InitiativePost.objects.all().order_by('-created_on')
        main_initiative = initiatives.first() if initiatives else None
        initiatives_post = initiatives[1:3] if initiatives.count() > 1 else None

        insights_post = InsightPost.objects.all().order_by('-created_on')[:4]
        events_post = EventPost.objects.all().order_by('-created_on')[:3]

        contact_form = ContactForm()
        data = {
            'home': home,
            'facts': facts,
            'initiatives_post': initiatives_post,
            'main_initiative': main_initiative,
            'insights_post': insights_post,
            'events_post': events_post,
            'meta': self.meta,
            'style': "transparent-header white water path-node page-node-type-program-center",
            'contactForm': contact_form,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)


class AboutView(BaseView):
    template_name = 'home/about.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the about page.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered about page.
        """
        try:
            about_page = AboutPage.objects.get(name="About Page Editor")
        except AboutPage.DoesNotExist:
            about_page = None

        image_url = about_page.image.url if about_page and about_page.image else settings.DEFAULT_IMAGE_URL
        self.meta = self.get_meta(f"{about_page.title} | Jalsmruti" if about_page else "About Us | Jalsmruti",
                                  about_page.description if about_page else "",
                                  about_page.keywords if about_page else "",
                                  '/about/', image_url)

        data = {
            'about_page': about_page,
            'meta': self.meta,
            'style': "about-us path-node page-node-type-simple-page",
        }
        self.knowledge.update(data)
        return render(request, self.template_name, self.knowledge)