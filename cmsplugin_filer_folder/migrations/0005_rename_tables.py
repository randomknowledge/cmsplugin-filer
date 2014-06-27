# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from cmsplugin_filer_utils.migration import rename_tables_new_to_old, rename_tables_old_to_new


class Migration(SchemaMigration):
    cms_plugin_table_mapping = (
        # (old_name, new_name),
        ('cmsplugin_filerfolder', 'cmsplugin_filer_folder_filerfolder'),
    )

    def forwards(self, orm):
        rename_tables_old_to_new(db, self.cms_plugin_table_mapping)

    def backwards(self, orm):
        rename_tables_new_to_old(db, self.cms_plugin_table_mapping)

    complete_apps = ['cmsplugin_filer_folder']
