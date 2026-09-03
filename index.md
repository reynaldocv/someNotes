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
<ul>
{% for main in unique_mains %}
  <li>
    <div class="contenedor-imagen">
      <img src="{{site.baseurl}}/assets/images/{{ main | capitalize }}.png">
      <div class="texto-centrado">{{ main | capitalize }}</div>
    </div>
    <strong>{{ main | capitalize }}</strong>
    
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
        <li>  <a href="{{site.baseurl}}/category/{{sub | slugify}}"> {{sub | slugify}}</a></li>
        
      {% endfor %}
      </ul>
    {% endif %}
  </li>
{% endfor %}
</ul>


{% comment %} 1. Collect all unique directory paths from posts {% endcomment %}
{% assign all_dirs = site.posts | map: "path" %}
{% assign post_folders = "" | split: "," %}

{% for path in all_dirs %}
  {% if path contains "/" %}
    {% assign parts = path | split: "/" %}
    {% comment %} Typically: _posts/folder/filename.md -> folder is at index 1 {% endcomment %}
    {% assign folder_name = parts[1] %}
    {% unless post_folders contains folder_name %}
      {% if folder_name contains ".md" or folder_name contains ".html" %}{% continue %}{% endif %}
      {% assign post_folders = post_folders | push: folder_name %}
    {% endunless %}
  {% endif %}
{% endfor %}

 <div class="w3-row w3-grayscale">
{% comment %} 2. Iterate through each folder and show 3 items {% endcomment %}
{% for folder in post_folders %}
<div class="w3-col l4 s6">
        <div class="w3-container w3-whitesmoke">
        <a href="{{ site.baseurl }}/category/{{folder | slugify}}">
          <div class="contenedor-imagen">
            <img src="{{site.baseurl}}/assets/images/{{folder}}.png">
            <div class="texto-centrado">{{ folder }}</div>
          </div>
        </a>        
  <ul>
    {% assign count = 0 %}
    {% for post in site.posts %}
      {% if post.path contains folder and count < 3 %}
        <li>  <a href="{{site.baseurl}}{{post.url}}"> {{ post.title }}</a></li>
        {% assign count = count | plus: 1 %}
      {% endif %}
    {% endfor %}
  </ul>
  </div>    
       </div>
{% endfor %}
</div>    
