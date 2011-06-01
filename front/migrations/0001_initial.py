# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Phone'
        db.create_table('front_phone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(unique=True, max_length=20)),
            ('blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('front', ['Phone'])

        # Adding model 'PhoneCall'
        db.create_table('front_phonecall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front.Phone'])),
            ('guid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('front', ['PhoneCall'])


    def backwards(self, orm):
        
        # Deleting model 'Phone'
        db.delete_table('front_phone')

        # Deleting model 'PhoneCall'
        db.delete_table('front_phonecall')


    models = {
        'front.phone': {
            'Meta': {'object_name': 'Phone'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'unique': 'True', 'max_length': '20'})
        },
        'front.phonecall': {
            'Meta': {'object_name': 'PhoneCall'},
            'completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['front.Phone']"})
        }
    }

    complete_apps = ['front']
