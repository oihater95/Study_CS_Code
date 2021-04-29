from rest_framework import serializers
from .models import Artist, Music

class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist', )


class MusicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=100)

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist', )


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)


class ArtistSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='musics.count')

    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics', 'music_count',)