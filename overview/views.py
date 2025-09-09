from django.shortcuts import render


def index(request):
    # Get the telescope ID from the query string
    telescope_id = int(request.GET.get("telescope_id", 1))

    # Make sure the ID is within the range
    if telescope_id < 1:
        telescope_id = 1
    else:
        telescope_id = (telescope_id - 1) % 4 + 1

    return render(request, "overview/index.html", { "telescope_id": telescope_id })