import uuid

from django.db import models


class UUIDModel(models.Model):
    """
    An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class DeletedManager(models.Manager):
    def get_queryset(self):
        return super(DeletedManager, self).get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    """
    An abstract base class model to add basic db fields with custom model manager
    """

    show_edit_button = True
    show_delete_button = True
    show_view_button = False

    add_user_fields = True
    if add_user_fields:
        # i_by = models.ForeignKey(get_user_model(), blank=True, null=True, editable=False, help_text="Inserted by")
        # u_by = models.ForeignKey(get_user_model(), blank=True, null=True, editable=False, help_text="Updated by")
        i_by = models.IntegerField(blank=True, null=True, editable=False)
        u_by = models.IntegerField(blank=True, null=True, editable=False)

    status_fields = True
    if status_fields:
        # objects = DeletedManager()
        is_active = models.BooleanField(blank=True, default=True, verbose_name="Status")
        is_deleted = models.BooleanField(blank=True, default=False,
                                         help_text="Instead of delete details from db, update this as False")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
