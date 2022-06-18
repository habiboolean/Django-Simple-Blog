from django.views import generic
from accounts.forms import RegistrationFrom


class SignUpView(generic.CreateView):
    form_class = RegistrationFrom
    success_url = "/"
    template_name = "registration/signup.html"

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs


