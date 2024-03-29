from django.test import TestCase

# Create your tests here.





'''
  <title>{% block title %}{{title_status}}{% endblock %}</title>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <link rel="stylesheet" type="text/css" href="/static/admin/css/base.css">
    <link rel="stylesheet" type="text/css" href="/static/admin/css/nav_sidebar.css">
    <link rel="stylesheet" type="text/css" href="/static/admin/css/changelists.css">

    <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles-coin.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles-games.css' %}">
    
<body class="app-task model-cliente change-list" data-admin-utc-offset="-10800">

  <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
    <script src="/static/admin/js/nav_sidebar.js" defer></script>
    <script src="/admin/jsi18n/"></script>

    <script src="{% static 'js/scripts.js' %}"></script>
    <script src="{% static 'js/script-coin.js' %}"></script>

    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
    </script>
'''



'''

  <title>{% block title %}{{title_status}}{% endblock %}</title>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <link rel="stylesheet" type="text/css" href="/static/admin/css/base.css">
    <link rel="stylesheet" type="text/css" href="/static/admin/css/nav_sidebar.css">
    <link rel="stylesheet" type="text/css" href="/static/admin/css/changelists.css">

    <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles-coin.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles-games.css' %}">
    


<body class="app-task model-cliente change-list" data-admin-utc-offset="-10800">

  <!--==========================
    Header
  ============================-->
  <header class="site-header">
    <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
      <div class="container">
        <a class="navbar-brand mr-4" href="/"><i class="fas fa-th"></i></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarToggle">
          <div class="navbar-nav mr-auto">
            {% if title_status == 'Home | xxx' or title_status == 'Upload | xxx' or title_status == 'Login | xxx'%}
              <a class="nav-item nav-link" href="/home_ncr">Home</a>
            {% elif title_status == 'COINS' %}
              <a class="nav-item nav-link" href="/index_coin">Home</a>
            {% elif title_status == 'HangmanGame' %}
              <a class="nav-item nav-link" href="/index_game">Home</a>
            {% else %}
              <a class="nav-item nav-link" href="/">Home</a>
            {% endif %}
          </div>

          <div class="navbar-nav">
            <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
            <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
          </div>
        </div>
      </div>
    </nav>
  </header>

<!--==========================
  INTO SITE
============================-->

  {% block content %}
  
  {% endblock %}

</div>  
</div>  
<footer>
  <div class="foot-foot">
    <div class="footer-aling1">
      <p>Copyright © 2021-2021 A.M.O. All rights reserved.</p>
    </div>
    <div class="footer-aling2">
      Beta-Version 1.0.1
    </div>
  </div>  
</footer>

  <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
    <script src="/static/admin/js/nav_sidebar.js" defer></script>
    <script src="/admin/jsi18n/"></script>

    <script src="{% static 'js/scripts.js' %}"></script>
    <script src="{% static 'js/script-coin.js' %}"></script>

    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
    </script>

</body>
</html>
'''






'''


<div class="breadcrumbs">
  <a href="/">Home</a>
  &rsaquo; <a href="/admin/project_control/">Lista de Documentos</a>
</div>

<div class="main shifted" id="main">

  <button class="sticky toggle-nav-sidebar" id="toggle-nav-sidebar" aria-label="Toggle navigation"></button>

  <!-- NAV-->
  <nav class="sticky" id="nav-sidebar">
    <div class="app-auth module">
      <table>
        <caption>
          <a href="/admin/auth/" class="section" title="Projects Currently in Progress">PROJETOS EM ANDAMENTO</a>
        </caption>

        <tr class="model-group">
          <th scope="row"><a href="{% url 'lista-proj' %}">Lista de Projetos</a></th>
          <td><a href="/admin/auth/group/add/" class="addlink">Add</a></td>
          <td><a href="/admin/auth/group/" class="changelink">Change</a></td>
        </tr>

        <tr class="model-group">
          <th scope="row"><a href="{% url 'lista-model-docs' %}">Modelo de Documentos</a></th>
          <td><a href="/admin/auth/group/add/" class="addlink">Add</a></td>
          <td><a href="/admin/auth/group/" class="changelink">Change</a></td>
        </tr>

        <tr class="model-user">
          <th scope="row"><a href="/admin/auth/user/">Status do Projeto</a></th>
          <td><a href="/admin/auth/user/add/" class="addlink">Add</a></td>
          <td><a href="/admin/auth/user/" class="changelink">Change</a></td>
        </tr>
      </table>
    </div>

    <div class="app-project_control module">
      <table>
        <caption>
          <a href="/admin/project_control/" class="section"
            title="Models in the Project_Control application">CONFIGURAÇÃO DE PROJETOS</a>
        </caption>

        <tr class="model-action">
          <th scope="row"><a href="/admin/project_control/project/">Novo Projeto</a></th>
          <td><a href="/admin/project_control/project/add/" class="addlink">Add</a></td>
          <td><a href="/admin/project_control/project/" class="changelink">Change</a></td>
        </tr>

        <tr class="model-doctype">
          <th scope="row"><a href="/admin/project_control/doctype/">Tipos de Documentos</a></th>
          <td><a href="/admin/project_control/doctype/add/" class="addlink">Add</a></td>
          <td><a href="/admin/project_control/doctype/" class="changelink">Change</a></td>
        </tr>

        <tr class="model-doctype">
          <th scope="row"><a href="/admin/project_control/subject/">Disciplinas</a></th>
          <td><a href="/admin/project_control/subject/add/" class="addlink">Add</a></td>
          <td><a href="/admin/project_control/subject/" class="changelink">Change</a></td>
        </tr>

      </table>
    </div>
  </nav>

'''