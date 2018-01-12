from django.urls import path, include
from rest_framework.routers import DefaultRouter
from billing import views as billingviews
from clients import views as clientviews
from projects import views as projectviews
from employees import views as employeeviews
from invoicing import views as invoicingviews
from entries import views as entryviews

router = DefaultRouter()
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
router.register(r'offices', employeeviews.OfficesViewSet, base_name='office')
router.register(r'employees', employeeviews.EmployeesViewSet, base_name='employee')
router.register(r'invoice-statuses', invoicingviews.InvoiceStatusesViewSet, base_name='invoicestatus')
router.register(r'invoices', invoicingviews.InvoicesViewSet, base_name='invoice')
router.register(r'entry-statuses', entryviews.EntryStatusesViewSet, base_name='entrystatus')
router.register(r'entries', entryviews.EntriesViewSet, base_name='entry')

urlpatterns = [
    path('', include(router.urls))
]