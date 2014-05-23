from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import serializers
from django.conf.urls import url

from .models import MetaModel

def make_all_document_app(configs):
    ''' use to parse the configuration
        and create the endpoints
            input is the list of configurations
            output is the list of app objects
    '''
    assert configs is not None
    all_apps = []

    for config in configs:
        entity_name = config.get('name', '')
        entity_config = config.get('config')
        app = make_document_app(entity_name, entity_config)
        all_apps.extend([{'name': entity_name,
                         'app': app}])
    return all_apps

def make_document_app(document_name, config=None):
    ''' this function define all parts of our application
        input
            document_name: is the name of the entity
            config: define our document configuration as a dictionary

        output:
            a dictionary containing model, serializer, views and urls
    '''

    if config is None:
        raise ValueError('configuration missing')

    if document_name in ['', None]:
        raise ValueError('document name is mandatory')

    # Model
    model_config = config.pop('model', None)
    if model_config is None:
        raise ValueError('model configuration missing')

    meta_model = get_model(document_name, model_config)

    # Serializer

    class Serializer(serializers.ModelSerializer):

        class Meta:
            model = meta_model

    Serializer.__name__ = '{}Serializer'.format(document_name)

    # Views

    views = config.pop('views', None)
    view_list = {}
    urls = []

    for view_definition in views:
        view_type = view_definition.get('type', '').lower()
        if view_type == 'list':
            parent_class = ListCreateAPIView
            name_type = 'List'
            base_url = r'^{}$'.format(document_name)
        elif view_type == 'detail':
            parent_class = RetrieveUpdateDestroyAPIView
            name_type = 'Detail'
            base_url = r'^{}/(?P<pk>\d+)$'.format(document_name)
        attrs = {'serializer_class': Serializer,
                 'queryset': meta_model.objects.all()}
        view_name = '{}{}View'.format(document_name, name_type)
        view = type(view_name,
                    (parent_class,), attrs)
        view_list[view_name] = view
        urls.append(url(base_url, view.as_view()))

    return {'model': meta_model,
            'views': view_list,
            'urls': urls}


def get_model(document_name, config):
    ''' model is defined out of here and is imported dinamically
        using __import__ function
    '''
    concrete = config.pop('concrete', None)
    if concrete:
        from_file = concrete.get('from')
        model_name = concrete.get('name')
        try:
            module = __import__(from_file, globals(), locals(), [model_name])
            concrete_model = getattr(module, model_name, None)
            return concrete_model
        except ImportError:
            raise ImportError('can not import name {} from {}'\
                .format(model_name, from_file))
