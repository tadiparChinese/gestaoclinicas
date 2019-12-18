from django import forms


class ClienteForms(forms.Form):

        nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        cnpj = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))

class FuncionarioForms(forms.Form):

        nome = forms.CharField(max_length=100, widget=forms.TextInput)
        nacionalidade = forms.CharField(max_length=50, widget=forms.TextInput)
        naturalidade_cid = forms.CharField(max_length=20, widget=forms.TextInput)
        naturalidade_estado = forms.CharField(max_length=20, widget=forms.TextInput)
        data_nasc = forms.DateField(widget=forms.DateField)
        sexo = forms.CharField(max_length=8, widget=forms.TextInput)
        estado_civil = forms.CharField(max_length=5, widget=forms.TextInput)
        mae = forms.CharField(max_length=50,widget=forms.TextInput)
        pai = forms.CharField(max_length=50, widget=forms.TextInput)
        cor_raca = forms.CharField(max_length=10, widget=forms.TextInput)
        dependentes = forms.IntegerField(widget=forms.TextInput)


class AtivosForm(forms.Form):
    tipo_ativo = forms.CharField(label='Tipo Ativo', max_length=20)
    descricao_ativo = forms.CharField(label='Descrição Ativo', max_length=20)
    valor_ativo = forms.IntegerField(label='Valor do Ativo')
    data_ativo = forms.DateField(label='Data do Ativo')


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('bulma.css',)
        }
        js = ('animations.js', 'actions.js')