import os
from django.core.management.base import BaseCommand, CommandError

"""
RUN IN TERMINAL: 'python manage.py generate_module <app_name> <Entity>'

Example: 'python manage.py generate_module users User' will create the below in the project directory
with the boilerplate inherited class names starting with "User"

users/
├── models.py
├── repositories/user_repository.py
├── services/user_service.py
├── serializers/user_serializer.py
├── views/user_view.py
└── urls.py

"""

TEMPLATE = {
    'models.py': '''from shared.models.base_model import BaseModel
from django.db import models

class {name}(BaseModel):
    """
    Replace this with actual fields for your model.
    """
    name = models.CharField(max_length=255)
''',

    'repositories/{lower_name}_repository.py': '''from shared.repositories.base_repository import BaseRepository
from {app_name}.models import {name}

class {name}Repository(BaseRepository):
    def __init__(self):
        super().__init__({name})
''',

    'services/{lower_name}_service.py': '''from shared.services.base_service import BaseService
from {app_name}.repositories.{lower_name}_repository import {name}Repository

class {name}Service(BaseService):
    def __init__(self):
        super().__init__({name}Repository())
''',

    'serializers/{lower_name}_serializer.py': '''from shared.serializers.base_serializer import BaseSerializer
from {app_name}.models import {name}

class {name}Serializer(BaseSerializer):
    class Meta:
        model = {name}
        fields = "__all__"
''',

    'views/{lower_name}_view.py': '''from shared.views.base_view import BaseAPIView
from shared.decorators.validate_request import validate_request
from {app_name}.serializers.{lower_name}_serializer import {name}Serializer
from {app_name}.services.{lower_name}_service import {name}Service

@validate_request({name}Serializer)
class {name}View(BaseAPIView):
    service_class = {name}Service
''',

    'urls.py': '''from django.urls import path
from .views.{lower_name}_view import {name}View

urlpatterns = [
    path("", {name}View.as_view(), name="{lower_name}_api"),
]
'''
}


class Command(BaseCommand):
    help = 'Generates a modular app structure for the Django boilerplate'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)
        parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        app_name = options['app_name']
        model_name = options['model_name']
        lower_name = model_name.lower()

        if not os.path.exists(app_name):
            os.makedirs(app_name)

        dirs = ['repositories', 'services', 'serializers', 'views']
        for d in dirs:
            os.makedirs(os.path.join(app_name, d), exist_ok=True)

        for filename, content in TEMPLATE.items():
            path = os.path.join(app_name, filename.format(lower_name=lower_name))
            dir_path = os.path.dirname(path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            with open(path, 'w') as f:
                f.write(content.format(app_name=app_name, name=model_name, lower_name=lower_name))

        self.stdout.write(self.style.SUCCESS(f'Module "{app_name}" with model "{model_name}" created.'))


