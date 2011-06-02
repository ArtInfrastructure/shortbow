# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Color'
        db.create_table('front_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hex_code', self.gf('django.db.models.fields.CharField')(default='#EEEEEE', max_length=10)),
        ))
        db.send_create_signal('front', ['Color'])


    def backwards(self, orm):
        
        # Deleting model 'Color'
        db.delete_table('front_color')


    models = {
        'front.color': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Color'},
            'hex_code': ('django.db.models.fields.CharField', [], {'default': "'#EEEEEE'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
