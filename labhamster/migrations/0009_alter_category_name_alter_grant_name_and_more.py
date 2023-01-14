# Generated by Django 4.1.5 on 2023-01-14 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import labhamster.customfields.datafields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labhamster', '0008_auto_20180225_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='name of product category', max_length=20, unique=True, verbose_name='Product Category'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='name',
            field=models.CharField(help_text='descriptive name of grant', max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, help_text='Order-related remarks. Please put catalog number and descriptions not here but into the product page.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(help_text='user who created this order', on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL, verbose_name='requested by'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateField(auto_now_add=True, help_text='Date when order was created', verbose_name='requested'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(blank=True, help_text='Date when order was placed', null=True, verbose_name='ordered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_received',
            field=models.DateField(blank=True, help_text='Date when product was received', null=True, verbose_name='received'),
        ),
        migrations.AlterField(
            model_name='order',
            name='grant_category',
            field=models.CharField(choices=[('consumables', 'consumables'), ('equipment', 'equipment')], default='consumables', max_length=20, verbose_name='Grant category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_urgent',
            field=models.BooleanField(default=False, help_text='Mark this order as urgent', verbose_name='Urgent!'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_by',
            field=models.ForeignKey(blank=True, help_text='user who sent this order out', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='ordered by'),
        ),
        migrations.AlterField(
            model_name='order',
            name='po_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='P.O.number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', help_text='cost per unit (!)', max_digits=8, null=True, verbose_name='Unit price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'British Pound'), ('EUR', 'Euro'), ('SAR', 'Saudi Riyal'), ('USD', 'US Dollar')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(help_text='Click the magnifying lens to select from the list of existing products.\nFor a new product, first click the lens, then click "Add Product" and fill out and save the Product form.', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='labhamster.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, help_text='number of units ordered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('pending', 'pending'), ('quote', 'quote requested'), ('ordered', 'ordered'), ('received', 'received'), ('cancelled', 'cancelled')], default='pending', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='unit_size',
            field=models.CharField(blank=True, help_text='e.g. "10 l", "1 kg", "500 tips"', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.CharField(help_text='vendor catalogue number', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labhamster.category', verbose_name='Product Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.TextField(blank=True, verbose_name='comments & description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, help_text='Product web site', verbose_name='Product Link'),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, help_text='location in the lab', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, help_text='original manufacturer if different', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer_product', to='labhamster.vendor', verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer_catalog',
            field=models.CharField(blank=True, help_text='manufacturer catalogue number', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='short descriptive name of this product', max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shelflife',
            field=labhamster.customfields.datafields.DayModelField(blank=True, null=True, unit='months', verbose_name='Shelf Life'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('ok', 'in stock'), ('low', 'running low'), ('out', 'not in stock'), ('expired', 'expired'), ('deprecated', 'deprecated')], default='out', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(help_text='select normal supplier of this product', on_delete=django.db.models.deletion.CASCADE, to='labhamster.vendor', verbose_name='Vendor'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact',
            field=models.CharField(blank=True, max_length=30, verbose_name='Primary contact name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.CharField(blank=True, max_length=30, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='link',
            field=models.URLField(blank=True, help_text='URL Link to Vendor home page'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='login',
            field=models.CharField(blank=True, max_length=50, verbose_name='Account Login'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(help_text='short descriptive name of this supplier', max_length=30, unique=True, verbose_name='Vendor name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='password',
            field=models.CharField(blank=True, max_length=30, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone'),
        ),
    ]
