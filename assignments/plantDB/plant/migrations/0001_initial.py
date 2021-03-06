# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Plant'
        db.create_table('plant_plant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('genus', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('species', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zone', self.gf('django.db.models.fields.IntegerField')()),
            ('featureColor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nativeRegion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('plantDescription', self.gf('django.db.models.fields.TextField')()),
            ('plantType', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bloom_time', self.gf('django.db.models.fields.CharField')(default='Spring', max_length=15)),
            ('sun_needs', self.gf('django.db.models.fields.CharField')(default='Full Sun', max_length=15)),
        ))
        db.send_create_signal('plant', ['Plant'])


    def backwards(self, orm):
        # Deleting model 'Plant'
        db.delete_table('plant_plant')


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
            'zone': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['plant']