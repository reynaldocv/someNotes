---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

{% comment %} 1. Extraer los nombres de las carpetas principales y subcarpetas {% endcomment %}
{% assign main_folders = "" | split: "," %}
{% assign all_paths = site.posts | map: "path" %}

{% for path in all_paths %}
  {% assign parts = path | split: "/" %}
  {% comment %} parts[0] suele ser '_posts' {% endcomment %}
  {% if parts[1] %}
    {% assign main_folders = main_folders | push: parts[1] %}
  {% endif %}
{% endfor %}

{% comment %} 2. Filtrar para tener solo carpetas principales únicas {% endcomment %}
{% assign unique_mains = main_folders | uniq | sort %}

{% comment %} 3. Construir la lista jerárquica {% endcomment %}
<div class="w3-row w3-grayscale">
  

  {% for main in unique_mains %}    
  <div class="w3-col l4 s6">
      <div class="w3-container w3-whitesmoke">
        <div class="contenedor-imagen">
          <img src="{{site.baseurl}}/assets/images/{{ main | capitalize }}.png">
          <div class="texto-centrado">{{ main | capitalize }}</div>
        </div>                        
        {% comment %} Buscar subcarpetas correspondientes a esta carpeta principal {% endcomment %}
        {% assign sub_folders = "" | split: "," %}      
        {% for path in all_paths %}
          {% assign parts = path | split: "/" %}
          {% if parts[1] == main and parts[2] and parts[3] %}
            {% comment %} parts[2] es la subcarpeta (ej. '_posts/carpeta/subcarpeta/archivo.md') {% endcomment %}
            {% assign sub_folders = sub_folders | push: parts[2] %}
          {% endif %}
        {% endfor %}      
        {% assign unique_subs = sub_folders | uniq | sort %}      
        {% comment %} Si existen subcarpetas, imprimirlas como una lista anidada {% endcomment %}
        {% if unique_subs.size > 0 %}
          <ul>
          {% for sub in unique_subs %}
            <li>  <a href="{{site.baseurl}}/category/{{sub}}"> {{sub | slugify}}</a></li>          
          {% endfor %}
          </ul>
        {% endif %}     
      </div>
  </div>
  {% endfor %}
</div>

