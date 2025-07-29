from boltiotai import openai #type:ignore
from apikey import OPENAI_API_KEY
from flask import Flask,render_template_string,request #type:ignore

openai.api_key=OPENAI_API_KEY

def generate_image(components):

    response=openai.Images.create(
        prompt=components,
        model="dall-e-3",
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']  # Return the image URL


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():

    output=""
    if(request.method=="POST"):
        components=request.form['components']
        output=generate_image(components)

    return render_template_string('''

    <!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AI Image Generator | DALL·E 3</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <nav class="navbar navbar-expand-lg" style="background-color: #1f3c50; height: 70px;" data-bs-theme="dark">
        <div class="container">
            <a class="navbar-brand" href="/">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>

            </div>
        </div>
    </nav>

    <div class="container my-5">
        <h1 class="mb-4">Generate Stunning Images with AI</h1>
        <form class="container mt-4 bg-light p-4" method="POST" action="/">
            <div class="mb-3">
                <span class="fs-5">Enter your image prompt:</span>
                <input type="text" class="form-control" name="components" placeholder="e.g. A cat astronaut in space"
                    required>
            </div>
            <div class="mb-3">
                <input type="submit" class="btn btn-secondary" value="generate image" style="background-color: #1f3c50;" data-bs-theme="light">
            </div>

            <div class="mt-5">
    <label for="image" class="form-label"><b>Image:</b></label>
    <div class="input-group">
        <img src="{{output}}" alt="Generated Image" class="img-fluid rounded" style="max-width: 50%; height: auto;">
    </div>
</div>


        </form>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q"
            crossorigin="anonymous"></script>
        <script src="main.js"></script>
</body>

</html>

    ''',output=output)

app.run(debug=True)