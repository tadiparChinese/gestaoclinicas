from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Clientes, Gestor, Funcionario, Ativos, Passivos
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import AtivosForm
import pandas as pd
from django.views import View



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AtivosForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/dashboard/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AtivosForm()

    return render(request, "ativos_form.html", {'form': form})

# Login


@login_required
def dashboard(request, id_ativo=2):
    return render(request, 'dashboard.html')


# Listar Dados

class ListClientes(ListView):
    model = Clientes
    template_name = "clientes_list.html"
    queryset = Clientes.objects.all()


class ClienteDetail(DetailView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# Criar Dados


class ClienteCreate(CreateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email', 'foto']
    success_url = reverse_lazy('list')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['id_func', 'nome', 'nacionalidade', 'naturalidade_cid',
              'naturalidade_estado', 'data_nasc', 'sexo', 'estado_civil', 'mae',
              'pai', 'cor_raca', 'dependentes']
#    success_url = reverse_lazy('funcionario')
#return render(request, 'fucionario.html')

class ClienteUpdate(UpdateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email']
#    success_url = reverse_lazy("list")


class ClienteDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AtivoCreate(CreateView):
    model = Ativos
    fields = ['id_ativo', 'tipo_ativo',
              'descricao_ativo', 'valor_ativo', 'data_ativo']
    success_url = reverse_lazy("dashboard")


class PassivoCreate(CreateView):
    model = Passivos
    fields = ['id_passivo', 'tipo_passivo',
              'descricao_passivo', 'valor_passivo', 'data_passivo']
    success_url = reverse_lazy("dashboard")


class GestorCreate(CreateView):
    model = Gestor
    fields = ['gestor_id', 'nome', 'email', 'celular', 'especialidade']
    success_url = reverse_lazy('list')

# Gráficos


class AtivosView(DetailView):
    model = Ativos
    template_name = 'dashboard.html'
    query_pk_and_slug = 'id_ativo=1'
