from rest_framework import serializers
from .models import Music_library

class music_librarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_library
        fields = ['title','artist', 'album','release_date','genre']
        
