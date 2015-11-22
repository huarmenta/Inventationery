#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-21 17:47:20
from django import forms
from .models import VendorModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


# Class: Form for VendorModel
# ----------------------------------------------------------------------------
class VendorForm(forms.ModelForm):

    class Meta:
        model = VendorModel
        fields = ('AccountNum',
                  'AccountType',
                  'OneTimeVendor',
                  'VendGroup',
                  'CreditLimit',
                  'CurrencyCode',
                  'VATNum',
                  'Notes',
                  'Party')

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['AccountNum'].widget.attrs['readonly'] = True
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['AccountType'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.AccountNum + instance.AccountType
        else:
            return self.cleaned_data['AccountNum']
            + self.cleaned_data['AccountType']


# Class: Form for DirPartyModel
# ----------------------------------------------------------------------------
class PartyForm(forms.ModelForm):

    class Meta:
        model = DirPartyModel
        fields = ('Name',
                  'NameAlias',
                  'LanguageCode',
                  'SecondName',
                  'FirstLastName',
                  'SecondLastName',
                  'Gender')

    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)


# Class: Form for LogisticsPostalAddressModel
# ----------------------------------------------------------------------------
class LogisticsPostalForm(forms.ModelForm):

    class Meta:
        model = LogisticsPostalAddressModel
        fields = ('Description',
                  'Purpose',
                  'CountryRegionId',
                  'ZipCode',
                  'Street',
                  'StreetNumber',
                  'BuildingCompliment',
                  'City',
                  'State',
                  'IsPrimary',)


# Class: Form for LogisticsElectronicAddressModel
# ----------------------------------------------------------------------------
class LogisticsElectronicForm(forms.ModelForm):

    class Meta:
        model = LogisticsElectronicAddressModel
        fields = ('Description',
                  'Type',
                  'Contact',
                  'IsPrimary',)
