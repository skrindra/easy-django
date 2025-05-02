import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


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
''',

    'admin.py': '''from django.contrib import admin
from .models import {name}

@admin.register({name})
class {name}Admin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at", "is_active"]
    search_fields = ["name"]
    list_filter = ["is_active", "created_at"]
''',

    'tests/test_{lower_name}_service.py': '''from django.test import TestCase
from {app_name}.services.{lower_name}_service import {name}Service

class {name}ServiceTest(TestCase):
    def setUp(self):
        self.service = {name}Service()

    def test_create_should_succeed(self):
        data = {{"name": "Test {name}"}}
        instance = self.service.create(data)
        self.assertIsNotNone(instance.id)

    def test_retrieve_should_return_queryset(self):
        results = self.service.retrieve({{}})
        self.assertIsNotNone(results)
'''
}

"""
RUN IN TERMINAL: 'python manage.py generate_module <app_name> <Entity>'

Example: 'python manage.py generate_module users User' will create the below in the project directory
with the boilerplate inherited class names starting with "User"

users/
├── __init__.py
├── admin.py                          # Auto-registers the User model with admin
├── models.py                         # Defines the User model
├── urls.py                           # Exposes the API route
├── repositories/
│   └── user_repository.py            # Encapsulates query logic
├── serializers/
│   └── user_serializer.py            # DRF serializer for the model
├── services/
│   └── user_service.py               # Business logic layer
├── views/
│   └── user_view.py                  # API view using BaseAPIView + decorator
└── tests/
    └── test_user_service.py          # Unit test for UserService

Additionally:
- Registers the app in INSTALLED_APPS if not present
- Automatically generates admin registration and placeholder test case
"""

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

        dirs = ['repositories', 'services', 'serializers', 'views', 'tests']
        for d in dirs:
            os.makedirs(os.path.join(app_name, d), exist_ok=True)

        for filename, content in TEMPLATE.items():
            path = os.path.join(app_name, filename.format(lower_name=lower_name))
            dir_path = os.path.dirname(path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            with open(path, 'w') as f:
                f.write(content.format(app_name=app_name, name=model_name, lower_name=lower_name))

        settings_file = os.path.join(settings.BASE_DIR, settings.SETTINGS_MODULE.replace('.', '/') + '.py')
        with open(settings_file, 'r') as f:
            settings_content = f.read()

        if app_name not in settings_content:
            with open(settings_file, 'a') as f:
                f.write(f"\nINSTALLED_APPS.append('{app_name}')\n")

        self.stdout.write(self.style.SUCCESS(f'Module "{app_name}" with model "{model_name}" scaffolded with admin, test files, and registered in INSTALLED_APPS.'))
