from rest_framework.serializers import ModelSerializer
from api.models.employee_models import Employee, Office


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'url',
            'first_name',
            'last_name',
            'middle_initial',
            'email',
            'cell_phone',
            'office_phone',
            'office_ext',
            'manager',
            'office',
            'current_week_start',
            'default_bill_rate',
        )


class OfficeSerializer(ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'id',
            'url',
            'description'
            'address',
            'city',
            'state',
            'zip_code',
            'phone',
        )