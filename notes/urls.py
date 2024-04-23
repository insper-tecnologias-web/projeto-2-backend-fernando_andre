from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('tag', views.tag, name='tag'),
    path('tag_espec/<int:id>', views.tag_espec, name='tag_espec'),
    path('simulado', views.simulado, name='simulado'),
    path('curtir/<int:id>', views.curtir, name='curtir'),
    path('voltar', views.voltar, name='voltar'),
    path('tag_espec/voltar', views.voltar, name='tag_espec_voltar'),
    path('deleteFact/<int:id>', views.deleteFact, name='deleteFact'),
    path('deleteTag/<int:id>', views.deleteTag, name='deleteTag'),
    path('tag_espec/tag', views.tag, name='tag'),
    path('provaPI', views.provaPI, name='provaPI'),
    path('produto', views.produto, name='produto'),
    path('api/notes/<int:note_id>/', views.api_note),
    path('api/notes/', views.api_notes),
    path('api/moedas/', views.api_binance),
]   