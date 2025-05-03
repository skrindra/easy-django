# Django Boilerplate → `easy-django` 📦

A modular, scalable, and DRY backend boilerplate built on Django. Designed to provide production-ready patterns (service, repository, serializer, view) and a CLI command to scaffold new modules with zero friction.

---

## 🚀 Features
- Modular directory structure (Django-onion architecture)
- Base classes for `Model`, `Repository`, `Service`, `Serializer`, `APIView`
- Unified decorator for query & body validation
- Command to scaffold CRUD-ready Django apps
- Auto admin registration
- Auto test stub generation
- Pagination and soft-delete support

---

## 📦 Installation
```bash
pip install easy-django
```

Or for local development:
```bash
pip install -e .
```

---

## 🧱 Generate a Module
```bash
python manage.py generate_module <app_name> <Entity>
```

### Example
```bash
python manage.py generate_module users User
```
Creates:
```
users/
├── __init__.py
├── admin.py
├── models.py
├── urls.py
├── repositories/
│   └── user_repository.py
├── serializers/
│   └── user_serializer.py
├── services/
│   └── user_service.py
├── views/
│   └── user_view.py
└── tests/
    └── test_user_service.py
```

- Registers `User` in `admin.py`
- Adds app to `INSTALLED_APPS`
- Includes unit test stub for service

---

## 📚 Structure Summary
### 🔹 BaseModel
- Common fields: `created_at`, `updated_at`, `is_active`
- Methods: `soft_delete()`, `restore()`

### 🔹 BaseService
- CRUD methods: `create`, `retrieve`, `update`, `delete`
- Supports pagination out of the box

### 🔹 BaseRepository
- ORM encapsulation: `get_by_id`, `filter`, `exists`, etc.

### 🔹 BaseAPIView
- Handles all HTTP verbs via service layer
- Unified error handling using custom exceptions

### 🔹 Decorator: `@validate_request`
- Combines `request.data` and `request.query_params`
- Injects validated data into `request.validated_data`

---

## 🧪 Testing
Each generated module includes test stubs inside:
```bash
<app_name>/tests/test_<entity>_service.py
```
Use Django's `TestCase` or plug in pytest if preferred.

---

## 🧰 Advanced
- Add signals, permissions, or mixins by extending `shared/`
- Create custom decorators for logging, audit, auth, etc.

---

## ✅ License
[MIT](LICENSE)

---

## 👨‍💻 Maintainer
Created by [Your Name] • Contributions welcome!
