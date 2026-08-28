---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

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
