from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # * return HttpResponse("Home")
    dict = {"name": "Piyush", "class": 12}
    return render(request, "index.html")

def analyze(request):
    punclist = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    usertext = request.POST.get("text", "none")
    rm = request.POST.get("rumpunc", "off")
    fullcaps = request.POST.get("UPPERCASE", "off")
    newlinerem = request.POST.get("newlinerem", "off")
    extraspacekill = request.POST.get("extraspacekill", "off")
    charcount = request.POST.get("charcount", "off")
    print(usertext)
    print(rm)
    analyzed = ""

    #* check box reader
    if rm == "on":
        for char in usertext:
            if char not in punclist:
                analyzed = analyzed + char

        diction = {"purpose": "Removed Punctuations", "analyzedtext": analyzed}
        # return render(request, "analyze.html", diction)
        usertext = analyzed

    if fullcaps == "on":
        analyzed = ""
        analyzed = usertext.upper()
        diction = {"purpose": "Uppercassed Characters", "analyzedtext": analyzed}
        # return render(request, "analyze.html", diction)
        usertext = analyzed

    if newlinerem == "on":
        analyzed = ""
        for char in usertext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        diction = {"purpose": "Newline Remove", "analyzedtext": analyzed}
        # return render(request, "analyze.html", diction)
        usertext = analyzed

    if extraspacekill == "on":
        analyzed = ""
        for index, char in enumerate(usertext):
            if not (usertext[index] == " " and usertext[index + 1] == " "):
                analyzed = analyzed + char

        diction = {"purpose": "ExtraSpace Remove", "analyzedtext": analyzed}
        # return render(request, "analyze.html", diction)
        usertext = analyzed

    if charcount == "on":
        analyzed = int()
        analyzed += len(usertext)

        diction = {"purpose": "Character counter", "analyzedtext": analyzed}
        usertext = analyzed
        return HttpResponse(
            f"""<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>r3alix01 - Home</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="/"><strong>r3alix01</strong></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll"
                aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarScroll">
                <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/">Blogs</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/">About</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarScrollingDropdown" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Link
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
    <div class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Success!</strong> Your text has been analyzed.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <h2>Character's Count:<br> <h3>{ analyzed }</h3>"""
        )
    #* If none is checked return Error
    if (
        fullcaps != "on"
        and extraspacekill != "on"
        and charcount != "on"
        and rm != "on"
        and newlinerem != "on"
    ):
        return HttpResponse("<h2>Error!</h2>")

    return render(request, "analyze.html", diction)
