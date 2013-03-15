# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Plant.thingy'
        db.add_column('plant_plant', 'thingy',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank='True'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Plant.thingy'
        db.delete_column('plant_plant', 'thingy')


    models = {
        'plant.plant': {
            'Meta': {'object_name': 'Plant'},
            'bloom_time': ('django.db.models.fields.CharField', [], {'default': "'Spring'", 'max_length': '15'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'featureColor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'genus': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nativeRegion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'plantDescription': ('django.db.models.fields.TextField', [], {}),
            'plantType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sun_needs': ('django.db.models.fields.CharField', [], {'default': "'Full Sun'", 'max_length': '15'}),
            'thingy': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': "'True'"}),
            'zone': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['plant']