import json
import os

def lambda_handler(event, context):
    path = event.get('path', '')
    
    # Servir el archivo YAML
    if path.endswith('openapi.yaml'):
        try:
            with open('openapi.yaml', 'r') as f:
                content = f.read()
            return {
                'statusCode': 200,
                'body': content,
                'headers': {'Content-Type': 'text/yaml'}
            }
        except Exception as e:
            return {'statusCode': 500, 'body': str(e)}

    # Servir Swagger UI HTML
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Swagger UI</title>
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.11.0/swagger-ui.css" >
        <style>
            html { box-sizing: border-box; overflow: -moz-scrollbars-vertical; overflow-y: scroll; }
            *, *:before, *:after { box-sizing: inherit; }
            body { margin:0; background: #fafafa; }
        </style>
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.11.0/swagger-ui-bundle.js"> </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.11.0/swagger-ui-standalone-preset.js"> </script>
        <script>
        window.onload = function() {
          const ui = SwaggerUIBundle({
            url: "openapi.yaml",
            dom_id: '#swagger-ui',
            deepLinking: true,
            presets: [
              SwaggerUIBundle.presets.apis,
              SwaggerUIStandalonePreset
            ],
            plugins: [
              SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "StandaloneLayout"
          })
          window.ui = ui
        }
      </script>
    </body>
    </html>
    """
    return {
        'statusCode': 200,
        'body': html_content,
        'headers': {'Content-Type': 'text/html'}
    }
