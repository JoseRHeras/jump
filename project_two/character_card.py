from custom_api.characters_api import get_character_stats

css_style = """
  <style>
      /* Define the CSS styles for the character card */
      .card {
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        padding: 20px;
        width: 400px;
      }

      .name {
        font-size: 24px;
        font-weight: bold;
        margin: 0 0 10px;
      }

      .image {
        border: 1px solid #ccc;
        border-radius: 5px;
        height: 300px;
        margin-bottom: 10px;
        overflow: hidden;
        width: 100%;
      }

      .image img {
        display: block;
        height: 100%;
        width: 100%;
      }

      .stats {
        font-size: 18px;
        margin: 10px 0 0;
      }

      .stat-label {
        font-weight: bold;
      }
    </style>

"""
html_template = """ 
<!DOCTYPE html>
<html>
  <head>
    <title>Character Card</title>
    {style}
  </head>
  <body>
    <!-- Create the character card using HTML -->
    <div class="card">
      <div class="name">{name}</div>
      <div class="image"><img src={image}></div>
      <div class="stats">
        <span class="stat-label">Power:</span>{power}<br>
        <span class="stat-label">Intelligence:</span>{intelligence}<br>
        <span class="stat-label">Strength:</span>{strength}<br>
        <span class="stat-label">Speed:</span>{speed}<br>
        <span class="stat-label">Durability:</span>{durability}<br>
        <span class="stat-label">Combat:</span>{combat}<br>
      </div>
    </div>
    
  </body>
</html> 
"""


def get_character_card(name:str) -> str:
    data = get_character_stats(name=name)

    return html_template.format(style=css_style, **data)
