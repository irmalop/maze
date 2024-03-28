from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .api import TvMazeApi
from .serializers import SearchSerializer


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

            show_list.append(show_dict)

        return Response({'data': show_list}, status=status.HTTP_200_OK)


class ShowByIdView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, show_id):

        tv_mazeapi = TvMazeApi()
        response_api = tv_mazeapi.get_show_by_id(show_id)
        print(response_api)
        
        json_api = response_api.json()

        return Response({'data': json_api}, status=status.HTTP_200_OK)
