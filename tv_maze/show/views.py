from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .api import TvMazeApi
from .models import Show, Comment
from .serializers import SearchSerializer, AddCommentSerializer, CommentSerializer


class SearchView(APIView):
    permission_classes = (AllowAny, )
    
    def get(self, request):
        serialized = SearchSerializer(data=request.GET)
        serialized.is_valid()
        data = serialized.validated_data

        tv_mazeapi = TvMazeApi()
        response_api = tv_mazeapi.search_shows(data.get('search_query'))
        
        json_api = response_api.json()

        show_list = []
        
        for item in json_api:
            show = item.get('show')
        
            show_dict = {
                'id': show.get('id'),
                'name': show.get('name'),
                'channel': show.get('webChannel').get('name') if show.get('webChannel') != None else show.get('network').get('name'),
                'summary': show.get('summary'),
                'genres': show.get('genres')
            }
            
            show_qs = Show.objects.filter(
                tvshow_id = show.get('id')
            )
            if show_qs:
                show_obj = show_qs.first()
 
                comments_qs = Comment.objects.filter(show = show_obj)
                show_dict['comments'] = CommentSerializer(comments_qs, many = True).data
            

            show_list.append(show_dict)

        return Response(show_list, status=status.HTTP_200_OK)


class ShowByIdView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, show_id):
        show_qs = Show.objects.filter(tvshow_id = show_id)
        if show_qs:
            show = show_qs.first()
            
        else:
            tv_mazeapi = TvMazeApi()
            response_api = tv_mazeapi.get_show_by_id(show_id)
            json_api = response_api.json()
            
            show = Show.objects.create(tvshow_id = show_id,
                    name = json_api.get('name'), 
                    channel = json_api.get('webChannel').get('name') if json_api.get('webChannel') != None else json_api.get('network').get('name'), 
                    summary = json_api.get('summary'), 
                    genres = json_api.get('genres'), 
                    show_object = json_api)
            
        data = show.show_object
        comments_qs = Comment.objects.filter(show = show)
        data['comments'] = CommentSerializer(comments_qs, many = True).data

        return Response(data, status=status.HTTP_200_OK)

class CommentView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):

        serializer = AddCommentSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        data = serializer.validated_data

        Comment.objects.create(
            show = data.get('show'),
            comment = data.get('comment'),
            rating = data.get('rating')
        )

        return Response({}, status=status.HTTP_201_CREATED)
