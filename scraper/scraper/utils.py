# -*- coding: utf-8 -*-


def item_to_model(item):
    model_class = getattr(item, 'django_model')
    if not model_class:
        raise TypeError("Item is not a `DjangoItem` or is misconfigured")

    return item.instance


def get_or_create(model):
    model_class = type(model)
    created = False

    # Normally, we would use `get_or_create`. However, `get_or_create` would
    # match all properties of an object (i.e. create a new object
    # anytime it changed) rather than update an existing object.
    #
    # Instead, we do the two steps separately
    try:
        # We have no unique identifier at the moment; use the title and author
        #  for now.
        obj = model_class.objects.get(title=model.title, author=model.author)
    except model_class.DoesNotExist:
        created = True
        obj = model  # DjangoItem created a model for us.

    return obj, created
