from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import serializers
from django.db import models


def make_document_app(document_name, config=None):
    ''' this function define all parts of our application
        input
            document_name: is the name of the document
            config: define our document configuration as a dictionary

        output:
            a dictionary containing model, serializer and view
    '''

    if config is None:
        raise ValueError('configuration missing')

    if document_name in ['', None]:
        raise ValueError('document name is mandatory')

    # Model
    model_config = config.pop('model', None)
    if model_config is None:
        raise ValueError('model configuration missing')

    model = get_model(document_name, model_config)

    # Serializer

    class Serializer(serializers.ModelSerializer):

        class Meta:
            model = model

    Serializer.__name__ = '{}Serializer'.format(document_name)

    views = config.pop('views', None)
    view_list = {}

    for view_definition in views:
        view_type = view_definition.get('type', '').lower()
        if view_type == 'list':
            parent_class = ListCreateAPIView
            name_type = 'List'
        elif view_type == 'detail':
            parent_class = RetrieveUpdateDestroyAPIView
            name_type = 'Detail'
        attrs = {'serialzer_class': Serializer,
                 'queryset': model.objects.all()}
        view_name = '{}{}View'.format(document_name, name_type)
        view = type(view_name,
                    parent_class, attrs)
        view_list[view_name] = view

    return {'model': model,
            'views': view_list}



def get_model(document_name, config):
    ''' model configuration contain a simple field list
        dictionary
    '''
    field_definition = config.pop('fields', None)
    fields_attr = {}
    for fld_def in field_definition:
        fld_name = fld_def.get('name', None)
        # type must be described as a model field
        # but with metaclass must be created dinamically
        # as the model
        fld_type = fld_def.get('type', None)
        fields_attr[fld_name] = fld_type

    model = type('{}_doc'.format(document_name),
                  (models.Model,),
                  {'base_fields': fields_attr})
    return model
