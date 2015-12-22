import inspect
import os

from django.template.loader import render_to_string


class Generator(object):
    """
    The Generator class takes a model class and generates one file out of it.
    """

    # The template name used to generate a file.
    template_name = None

    # The file path relative to an app.
    # Examples: 'views.py' or 'tests/test_views.py'
    file_name = None

    def __init__(self, model_class=None, file_name=''):
        self.model_class = model_class
        self.app_label = model_class._meta.app_label

    def generate(self):
        return render_to_string(self.get_template_name(), self.get_context())

    def get_context(self):
        context = {
            'model_name': self.model_class.__name__,
            'field_names': [f.name for f in self.model_class._meta.get_fields()],
            'app_label': self.app_label,
        }
        context.update(self.get_extra_context())
        return context

    def get_extra_context(self):
        """Method for users to override to add more data to the context."""
        return {}

    def get_template_name(self):
        return self.template_name

    def get_file_name(self):
        return self.file_name

    def get_full_path(self):
        model_path = inspect.getfile(self.model_class)
        app_dir = os.path.split(model_path)[0]
        return os.path.join(app_dir, self.get_file_name())

    def generate_file(self):
        try:
            file_content = self.generate()
            file_path = self.get_full_path()
            with open(file_path, 'w') as f:
                f.write(file_content.encode('utf-8'))
            return True
        except KeyError:
            raise CommandError("Invalid configuration.")
