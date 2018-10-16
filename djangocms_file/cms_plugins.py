# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import File, Folder

ICON_CLASS = {
    '': 'fa fa-file-o',
    'pdf': 'fa fa-file-pdf-o',
    'mp3': 'fa fa-file-audio-o',
    'py': 'fa fa-file-code-o',
    'java': 'fa fa-file-code-o',
    'c': 'fa fa-file-code-o',
    'zip': 'fa fa-file-archive-o',
    'tar.gz': 'fa fa-file-archive-o',
    'xls': 'fa fa-file-excel-o',
    'xlsx': 'fa fa-file-excel-o',
    'xlt': 'fa fa-file-excel-o',
    'txt': 'fa fa-file-text-o',
    'text': 'fa fa-file-text-o',
    'md': 'fa fa-file-text-o',
    'mp4': 'fa fa-file-video-o',
    'avi': 'fa fa-file-video-o',
    'mkv': 'fa fa-file-video-o',
    'svg': 'fa fa-file-image-o',
    'png': 'fa fa-file-image-o',
    'jpeg': 'fa fa-file-image-o',
    'gif': 'fa fa-file-image-o',
    'jpg': 'fa fa-file-image-o',
    'doc': 'fa fa-file-word-o',
    'docx': 'fa fa-file-word-o',
    'odt': 'fa fa-file-word-o',
    'ott': 'fa fa-file-word-o',
    'oth': 'fa fa-file-word-o',
    'odm': 'fa fa-file-word-o',
}

class FilePlugin(CMSPluginBase):
    model = File
    name = _("File")
    render_template = "cms/plugins/file.html"
    module = "Basis plugins"
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'file_src',
                'file_name',
                'show_pdf_preview',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                ('link_target', 'link_title'),
                'show_file_size',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        if instance.file_src and instance.file_src.extension:
            file_extension = instance.file_src.extension
        if ICON_CLASS.has_key(file_extension):
            context['file_extension_class'] = ICON_CLASS[file_extension]
        else:
            context['file_extension_class'] = ICON_CLASS['']

        return 'djangocms_file/{}/file.html'.format(instance.template)


class FolderPlugin(CMSPluginBase):
    model = Folder
    name = _('Folder')
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'folder_src',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                'link_target',
                'show_file_size',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        context['folder_files'] = instance.get_files()
        return super(FolderPlugin, self).render(context, instance, placeholder)

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_file/{}/folder.html'.format(instance.template)


plugin_pool.register_plugin(FilePlugin)
plugin_pool.register_plugin(FolderPlugin)
