from django.shortcuts import render, redirect
from .models import Note, Tag, Fact, Produto, Moeda
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import NoteSerializer, MoedaSerializer
import requests

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        titulo = request.POST.get('createTag')
        Lista = Tag.objects.filter(titulo=titulo)
        if len(Lista) == 0:
            Tag(titulo=titulo).save()
            Lista = Tag.objects.filter(titulo=titulo)
        tag_ = Lista[0]
        Note(title=title, content=content, tag=tag_).save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('index')

def update(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        action =  request.POST.get('action')
        if action == 'Salvar':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            note.title = title
            note.content = content
            note.save()
        return redirect('index')
    else:
        return render(request, 'notes/update.html', {'title': note.title, 'content': note.content})
    

def tag(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tag.html', {'tags': all_tags})

def tag_espec(request, id):
    note_tag = Tag.objects.get(id=id)
    notes = Note.objects.filter(tag=note_tag)
    return render(request, 'notes/tag_espec.html', {'notes': notes})
    # return redirect('tag_espec', {'notes': notes})

def simulado(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        Fact(descricao=descricao).save()
        return redirect('simulado')
    all_facts = Fact.objects.all()
    return render(request, 'notes/simulado.html', {'description': all_facts, 'qnt_facts': len(all_facts)})

def curtir(request, id):
    fact = Fact.objects.get(id=id)
    fact.curtidas += 1
    fact.save()
    return redirect('simulado')

def voltar(request):
    return redirect('index')

def deleteFact(request, id):
    fact = Fact.objects.get(id=id)
    fact.delete()
    return redirect('simulado')

def deleteTag(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return redirect('tag')

def provaPI(request):
    return render(request, 'notes/provaPI.html')

def produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        promocao = request.POST.get('promocao', False)
        Produto(nome=nome, preco=preco, estoque=estoque, promocao=promocao).save()
        return redirect('produto')
    all_produtos = Produto.objects.all()
    return render(request, 'notes/produto.html', {'produtos': all_produtos, 'qnt_produtos': len(all_produtos)})


@api_view(['GET', 'POST', 'DELETE'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save() 
    if request.method == 'DELETE':
        note.delete()
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])
def api_notes(request):
    if request.method == 'POST':
        new_note_data = request.data
        Note.objects.create(title=new_note_data['title'], content=new_note_data['content'])
    notes = Note.objects.all()
    serialized_notes = NoteSerializer(notes, many=True)
    return Response(serialized_notes.data)

@api_view(['GET'])
def api_binance(request):
    url = "https://binance43.p.rapidapi.com/ticker/price"
    headers = {
        "X-RapidAPI-Key": "faaef0b15dmshbba959178caf68dp13952ejsnda47a593faad",
        "X-RapidAPI-Host": "binance43.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    return Response(response.json())

@api_view(['GET', 'POST'])
def favoritar(request):

    if request.method == 'POST':
        moeda_fav = request.data.get('symbol')
        obj, created = Moeda.objects.get_or_create(nome=moeda_fav)
        if not created:
            obj.delete()
        return Response({'message': 'Moeda favoritada com sucesso!'})
    
    if request.method == 'GET':
        favs = Moeda.objects.all()
        moedas_fav = [moeda for moeda in api_binance() if moeda['nome'] in favs]
        serialized_favs = MoedaSerializer(moedas_fav, many=True)
        return Response(serialized_favs.data)
    
