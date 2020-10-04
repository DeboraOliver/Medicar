<h1 align="center">
  <img alt="Fastfeet" title="Medicar" src="pics/logo.png" width="300px" />
</h1>

<h3 align="center">
  Desafio: Medicar
</h3>

<p align="center">Sistema para gestão de consultas em uma clínica médica</p>

<p align="center">
  <a href="#cadastrar-especialidades">Cadastrar Especialidade</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#cadastrar-médicos">Cadastrar Médicos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#criar-agenda-para-médico">Criar Agenda para Médicos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#listar-agendas-disponíveis">Listar agendas disponíveis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#listar-consultas-marcadas">Listar consultas marcadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#desmarcar-consulta">Desmarcar consulta</a>&nbsp;&nbsp;&nbsp;
</p>

## Backend

Instale a versão 3.x do Python e o Virtualenv:

<ol>
<li> Clone este repositório : git clone https://github.com/DeboraOliver/Medicar.git
<li> Vá para o repositório : cd medicar
<li> Crie um ambiente de desenvolvimento : virtualenv --python $( which python3 ) py3;
<li> Instale as dependências : pip install -r requirements.txt;
<li> Crie a base de dados : python manage.py migrate
<li> Suba o servidor : python manage.py runserver
<li> Acesse o programa em 127.0.0.1:8000
</ol>

Os endpoints gerados:

<h2 align="center">
  <img alt="Fastfeet" title="endpoints" src="pics/endpoints.png" width="300px" />
</h2>

## Cadastrar especialidades

No models.py:

```
class Especialidade(models.Model):
    especialidade = models.CharField(max_length=50, default='Demartologia')

    def __str__(self):
        return self.especialidade

    class Meta:
        ordering = ['especialidade'] 
```
O resultado na tela administrativa:

<h2 align="center">
  <img alt="Fastfeet" title="especialidadecadastro" src="pics/cadastrar_especialidade.png" width="300px" />
</h2>

### Listar especialidades médicas

Ao acessar a http://127.0.0.1:8000/especialidade/ é possível visualizar ambas as especialidades cadastradas:

<h2 align="center">
  <img alt="Fastfeet" title="especialidadelista" src="pics/lista_especialidades.png" width="300px" />
</h2>

## Cadastrar médicos

O cadastro de médicos e os campor nome, crm, email, telefone conforme o requisito.

```
class Medico(models.Model):
    nome = models.CharField ("Nome", max_length=200, null = False, blank = False)
    crm = models.CharField ("CRM", max_length=11,  null = False, blank = False)
    email = models.EmailField ()
    telefone = models.CharField ("Telefone", max_length=11)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
```

Resulta na seguinte tela:

<h2 align="center">
  <img alt="Fastfeet" title="medicoslista" src="pics/cadastrar_medicos.png" width="300px" />
</h2>


### Listar médicos

Na localhost http://127.0.0.1:8000/medico/:

<h2 align="center">
  <img alt="Fastfeet" title="medicoscadastro" src="pics/lista_medicos.png" width="300px" />
</h2>


## Criar agenda para médico 

Para o cadastro das agendas médicas, respeitando a regra de negócio de não criar agendas paras datas passadas, vamos usar um validador. E para evitar a criação de repetidas agendas para um mesmo médico em um dado dia, vamos usar a função clean(). Por fim, respeitando a regra de manter a agenda ordenada pelo dia mais próximo, vamos adicionar uma classe organizadora.

```
hours = [(i, dt.time(i).strftime('%H:%M')) for i in range(7,21)]

#validator
def data_passada(value):
    hoje = date.today()
    if value < hoje:
        raise ValidationError("Não é possível agendar horários em datas passadas.")

class Agenda(models.Model):
    medico = models.ForeignKey (Medico, on_delete=models.CASCADE)
    dia = models.DateField (validators=[data_passada],  null = False, blank = False)
    horario = MultiSelectField(choices=hours,
                                 max_choices=5,
                                 max_length=200)

    def clean(self):
        if self.dia and Agenda.objects.filter (medico=self.medico).exists ():
            raise ValidationError ("Já existe agenda para o dia {} com dr(a) {}. Escolha outro dia, ou outro médico.".format(self.dia, self.medico))

    def __str__(self):
        return '{} - {}'.format (self.medico, self.dia)

    class Meta:
        ordering = ['dia']
```

Na tela administrativa, o código acima aparece como:

<h2 align="center">
  <img alt="Fastfeet" title="cadastroagendas" src="pics/cadastro_agendas.png" width="300px" />
</h2>

### Listar agendas disponíveis

A lista de agendas pode ser visto na localhost como:

<h2 align="center">
  <img alt="Fastfeet" title="listaagendas" src="pics/lista_agendas.png" width="300px" />
</h2>

### Listar consultas marcadas

As consultas podem ser cadastradas devido ao código:

```
class Consulta(models.Model):

    usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    
    medico = ChainedForeignKey(
        Medico,
        chained_field="especialidade",
        chained_model_field="especialidade",
        show_all=False,
        auto_choose=True,
        sort=True)

    dia = ChainedForeignKey(
        Agenda,
        chained_field="medico",
        chained_model_field="medico",
        show_all=False,
        auto_choose=True,
        sort=True)

    horario = models.TimeField()

    data_agendamento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} - {}'.format (self.medico, self.dia, self.horario)

    #Ordenar consulta por dia e horário
    class Meta:
        ordering = ['dia','horario']

        #checar se já existe esta consulta
    def hora_marcada(self):
        #agenda_hours = Agenda.objects.filter(medico=self.medico, dia = self.dia)
        #if self.dia and self.horario and Consulta.objects.filter(owner=self.owner).exists ():
        if self.dia and Consulta.objects.filter (horario=self.horario).exists():
            raise ValidationError ("Você já possui uma consulta marcada para {} - {}.".format(self.dia, self.horario))
```
Este código aparece na localhost como:

<h2 align="center">
  <img alt="Fastfeet" title="listaconsultas" src="pics/cadastrar_consultas.png" width="300px" />
</h2>

A lista de consultas (parte):

<h2 align="center">
  <img alt="Fastfeet" title="listaconsultas" src="pics/lista_consultas.png" width="300px" />
</h2>

Como se pode verificar algumas regras de negócios não entraram e alguns ajustes talvez precisassem ser feitos.

### Desmarcar consulta

Também é possível desmarcar consulta se for necessário:

<h2 align="center">
  <img alt="Fastfeet" title="desmarcar" src="pics/desmarcar.png" width="300px" />
</h2>

## O que pode melhorar

Algumas regras de negócio ficaram pendentes:
<ul>
<li> Garantir que, além da data não poder ser anterior ao dia de hoje, a hora também esteja de acordo e não possamos agendar consultas para horários mais cedos do que o atual;</li>
<li> O horário das consultas na agenda poderia ter intervalo de 15 minutos ao invés de uma hora;</li>

## Fontes

<ul>
<li><a href="https://pypi.org/project/django-multiselectfield/">Django-multiselectfield 0.1.12</a></li>
<li><a href="https://django-smart-selects.readthedocs.io/en/latest/index.html">Django smart_selects</a></li>
