# django-file-upload
Demo of file upload

forms.py
```
from django import forms
class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')
```

models.py
```
from django.db import models
class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')
```

views.py
```
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect, HttpResponse
from app.forms import ProfileImageForm
from app.models import ProfileImage
from django.core.urlresolvers import reverse
class ProfileImageView(FormView):
    template_name = 'profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponse('File Uploaded')
```
profile_image_form.html
```
{% block content %}
<form action="{% url "profile_image_upload" %}" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="submit" />
</form>
{% endblock %}
```
