from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import update_note, get_note_detail, delete_note, get_notes_list, create_note


# Create your views here.

@api_view(['GET'])
def get_routes(request):
    
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET', 'POST'])
def get_notes(request):
    if request.method == 'GET':
        return get_notes_list(request)

    if request.method == 'POST':
        return create_note(request)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def get_note(request, pk):

    if request.method == 'GET':
        return get_note_detail(request, pk)

    if request.method == 'PUT':
        return update_note(request, pk)

    if request.method == 'DELETE':
       return delete_note(request, pk)
