from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view

from api.routers import ExtendedDefaultRouter

from billing import views as billingviews
from clients import views as clientviews
from projects import views as projectviews
from employees import views as employeeviews
from invoicing import views as invoicingviews
from entries import views as entryviews
from tasks import views as taskviews

router = ExtendedDefaultRouter()
router.register(r'bill-rates', billingviews.BillRatesViewSet, base_name='billrate')
router.register(r'billable-items', billingviews.BillableItemsViewSet, base_name='billableitem')
router.register(r'bill-types', billingviews.BillTypesViewSet, base_name='billtype')
router.register(r'departments', billingviews.DepartmentViewSet, base_name='department')
router.register(r'contacts', clientviews.ContactsViewSet, base_name='contact')
router.register(r'clients', clientviews.ClientsViewSet, base_name='client')
router.register(r'project-types', projectviews.ProjectTypesViewSet, base_name='projecttype')
router.register(r'project-statuses', projectviews.ProjectStatusesViewSet, base_name='projectstatus')
router.register(r'projects', projectviews.ProjectsViewSet, base_name='project')
router.register(r'project-subsets', projectviews.ProjectSubsetsViewSet, base_name='projectsubset')
router.register(r'offices', employeeviews.OfficesViewSet, base_name='office') \
    .register(r'employees', employeeviews.EmployeesViewSet,
              base_name='offices-employee', parents_query_lookups=['office'])
employees_routes = router.register(r'employees', employeeviews.EmployeesViewSet, base_name='employee')
employees_routes.register(r'projects', projectviews.ProjectsViewSet,
                          base_name='projects-employee', parents_query_lookups=['lead_employee'])
employees_routes.register(r'clients', clientviews.ClientsViewSet,
                          base_name='clients-employee', parents_query_lookups=['lead_employee'])
router.register(r'invoice-statuses', invoicingviews.InvoiceStatusesViewSet, base_name='invoicestatus')
router.register(r'invoices', invoicingviews.InvoicesViewSet, base_name='invoice')
router.register(r'task-statuses', taskviews.TasksStatusesViewSet, base_name='taskstatus')
router.register(r'default-tasks', taskviews.DefaultTasksViewSet, base_name='defaulttask')
router.register(r'tasks', taskviews.TaskViewSet, base_name='task')
router.register(r'task-estimates', taskviews.TaskEstimateViewSet, base_name='taskestimate')
router.register(r'entry-statuses', entryviews.EntryStatusesViewSet, base_name='entrystatus')
router.register(r'entries', entryviews.EntriesViewSet, base_name='entry')

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('schema/', schema_view),
]
