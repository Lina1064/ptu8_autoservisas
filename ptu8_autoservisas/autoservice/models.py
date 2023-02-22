from django.db import models
from django.utils.translation import gettext_lazy as _


class CarModel(models.Model):
    make = models.CharField(_('make'), max_length=100, db_index=True)
    model = models.CharField(_('model'), max_length=100, db_index=True)

    def __str__(self) -> str:
        return f"{self.make} {self.model}"

    class Meta:
        ordering = ['make', 'model']

class Service(models.Model):
    name = models.CharField(_('name'), max_length=255, db_index=True)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name} {self.price}"
    
    class Meta:
        ordering = ['name']

class Car(models.Model):
    vehicle_registration_plate = models.CharField(_('vehicle registration plate'), max_length=10)
    vehicle_identification_number = models.CharField(_('vehicle identification number'), max_length=17)
    client = models.CharField(_('client'), max_length=30)
    model = models.ForeignKey(
        CarModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('model'),
    )

    def __str__(self) -> str:
        return f"{self.vehicle_registration_plate} {self.vehicle_identification_number} {self.client} {self.model}"

    class Meta:
        ordering = ['client', 'vehicle_registration_plate']

class Order(models.Model):
    date = models.DateTimeField(_('order date'), auto_now_add=True)
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('car')
    )
    total_order_price = models.DecimalField(_('total order price'), max_digits=10, decimal_places=2, blank=True)
    
    @property
    def total_order_price(self):
        total = 0
        for line in self.orderlines.all():
            total+=line.total_price
        return total

    ORDER_STATUS = (
        ('o', _('ordered')),
        ('p', _('in process')),
        ('d', _('done')),
        ('c', _('cancelled')),
    )
    
    status = models.CharField(_('status'), max_length=1, choices=ORDER_STATUS, default='o')

    def __str__(self) -> str:
        return f"{self.date} {self.car} {self.status} {self.total_order_price}"

    class Meta:
        ordering = ['date']

class OrderLine(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name='order_lines',
        verbose_name=_('service'),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='order_lines',
        verbose_name=_('orders'),
    )
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    total_price = models.DecimalField(_('total order price'), max_digits=10, decimal_places=2, blank=True)

    @property
    def total_price(self):
        return self.service.price * self.quantity
    
    def __str__(self) -> str:
        return f"{self.service} {self.order} {self.quantity} {self.total_price}"
    