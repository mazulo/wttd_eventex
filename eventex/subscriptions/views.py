from django.views.generic import DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from .mixins import EmailCreateView


new = EmailCreateView.as_view(
    model=Subscription, form_class=SubscriptionForm,
    email_subject='Confirmação de inscrição'
)

detail = DetailView.as_view(model=Subscription)
