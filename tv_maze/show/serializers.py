from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Show, Comment


class SearchSerializer(serializers.Serializer):
    search_query = serializers.CharField()

class AddCommentSerializer(serializers.Serializer):
    show = serializers.IntegerField()
    comment = serializers.CharField()
    rating = serializers.IntegerField()

    def validate(self, data):
        errors = {}
        show_id = data.get("show")
        show_qs = Show.objects.filter(tvshow_id = show_id)
        
        if not show_qs:
            errors['show'] = f"Show con id{show_id} no registrado"
            
        else:
            data['show'] = show_qs.first()
        
        rating = data.get("rating")
        
        if rating < 0 or rating > 5:
            errors['rating'] = f"Rating debe estar entre 0 y 5"
            
        if errors:
            raise ValidationError(errors)
        return data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment',
                  'rating')
        