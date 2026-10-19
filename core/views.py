from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoriaForm, BairroForm, UsuarioForm
from .models import Categoria, Bairro, Usuario


def inicial(request):
    return render(request, 'index.html')


def categoria_lista(request):
    lista = Categoria.objects.all().order_by('nome')
    return render(request, 'categoria_lista.html', {'lista': lista})


def categoria_cadastro(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoria cadastrada com sucesso.')
        return redirect('categoria_lista')
    return render(request, 'categoria_form.html', {'form': form})


def categoria_editar(request, pk):
    obj = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoria atualizada com sucesso.')
        return redirect('categoria_lista')
    return render(request, 'categoria_form.html', {'form': form, 'editando': True})


def categoria_remover(request, pk):
    obj = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, 'Categoria removida.')
        except ProtectedError:
            messages.error(request, 'Não é possível remover: há denúncias usando esta categoria.')
        return redirect('categoria_lista')
    return render(request, 'categoria_confirmar_remocao.html', {'obj': obj})


def bairro_lista(request):
    lista = Bairro.objects.all().order_by('nome')
    return render(request, 'bairro_lista.html', {'lista': lista})


def bairro_cadastro(request):
    form = BairroForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Bairro cadastrado com sucesso.')
        return redirect('bairro_lista')
    return render(request, 'bairro_form.html', {'form': form})


def bairro_editar(request, pk):
    obj = get_object_or_404(Bairro, pk=pk)
    form = BairroForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Bairro atualizado com sucesso.')
        return redirect('bairro_lista')
    return render(request, 'bairro_form.html', {'form': form, 'editando': True})


def bairro_remover(request, pk):
    obj = get_object_or_404(Bairro, pk=pk)
    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, 'Bairro removido.')
        except ProtectedError:
            messages.error(request, 'Não é possível remover: há denúncias neste bairro.')
        return redirect('bairro_lista')
    return render(request, 'bairro_confirmar_remocao.html', {'obj': obj})


def usuario_lista(request):
    lista = Usuario.objects.all().order_by('nome')
    return render(request, 'usuario_lista.html', {'lista': lista})


def usuario_cadastro(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('usuario_lista')
    return render(request, 'usuario_form.html', {'form': form})


def usuario_editar(request, pk):
    obj = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário atualizado com sucesso.')
        return redirect('usuario_lista')
    return render(request, 'usuario_form.html', {'form': form, 'editando': True})


def usuario_remover(request, pk):
    obj = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, 'Usuário removido.')
        except ProtectedError:
            messages.error(request, 'Não é possível remover: este usuário possui denúncias ou alterações de status.')
        return redirect('usuario_lista')
    return render(request, 'usuario_confirmar_remocao.html', {'obj': obj})