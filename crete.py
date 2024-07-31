import os

dirs = [
    "employee_management_system/app/models",
    "employee_management_system/app/dto",
    "employee_management_system/app/dao",
    "employee_management_system/app/services",
    "employee_management_system/app/controllers",
    "employee_management_system/app/views",
    "employee_management_system/tests"
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)

init_files = [
    "employee_management_system/app/__init__.py",
    "employee_management_system/app/models/__init__.py",
    "employee_management_system/app/dto/__init__.py",
    "employee_management_system/app/dao/__init__.py",
    "employee_management_system/app/services/__init__.py",
    "employee_management_system/app/controllers/__init__.py",
    "employee_management_system/app/views/__init__.py",
    "employee_management_system/tests/__init__.py",
    "employee_management_system/app/models/user.py",
    "employee_management_system/app/dto/user_dto.py",
    "employee_management_system/app/dao/user_dao.py",
    "employee_management_system/app/services/auth_service.py",
    "employee_management_system/app/controllers/auth_controller.py",
    "employee_management_system/tests/test_auth.py",
    "employee_management_system/config.py",
    "employee_management_system/requirements.txt",
    "employee_management_system/main.py"
]

for file in init_files:
    with open(file, 'w') as f:
        pass


