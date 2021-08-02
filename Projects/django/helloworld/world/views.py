# # from django.shortcuts import render
#
# # Create your views here.
#
# # returning a simple hello world
# # returning view with taking req and responsing with view
# from django.http import HttpResponse
#
# def home(request):
#
#     #using more feature like adding html string
#     html_content = """
#     <html>
#     <body>
#
#       <h1>Hello world from django.</h1>
#       <p>This is my first web application in django.</p>
#
#     </body>
#     </html>
#     """
#     response = HttpResponse()
#     response.content = "Hello world"
#     return response
#     return HttpResponse(html_content)

# importing django urls amd importing path

# creating our views here
#
# from django.http import HttpResponse
# here we must add http response not found error handling
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

#creating hom function with always fst parameter request


def home(request):
    html_content = """
    <html>
    <style>
       h1{
       text-align: center;
       color: green;
       }
    </style>
    <body>
        <h1>hello and welcome! this is main section page!</h1>
    </body>
    </html>
    """
    return HttpResponse(html_content)
    return HttpResponse("")

def profile(request, name):
    data = {
        'peter': 'Peter Pan',
        'roberto': 'roberto robert',
        'hari':  'hari parsad',
    }

    #full_name = data[name]
    full_name = data.get(name)

    # Handling the cases where request has came asking the user which is not in database
    # applying conditions
    if not full_name:
        # return HttpResponseNotFound("This username does not exits!")
        return HttpResponseNotFound("This username does not exits!", status=404)

    string_data = f"Your Full Name is: {full_name}"
    return HttpResponse(string_data)
    # string_data = "Your name in profile is : {}".format(name)
    # return HttpResponse("This is a profile section of dilli!")
    # created profile function and now assigning the function to urls.py

# if client wants response in json form
def profile_json(r, name):
    data = {
        'peter': 'Peter Pan',
        'roberto': 'roberto robert',
        'hari': 'hari parsad',
    }

    full_name = data.get(name)

    if not full_name:
        return HttpResponseNotFound("This username no longer exits!", status=404)

    # here we create dictionary object for returning it in json format
    # full_name is variable full_name
    dict_data = {
        'full_name': full_name
    }
    print(dict_data)
    print(type(dict_data))
    #returning the httpresponse
    #return HttpResponse(dict_data)
    # updating this line
    return JsonResponse(dict_data)

# creating new function for path converting str to int
# def int_converter_view(r, *args, **kwargs):
def int_converter_view(r, int_data):
    print("int data is:", int_data)
    print(type(int_data))
    try:
        # converted_int_data = int(int_data)
        # since converted_int_data is not use we can pass _ underscore
        _ = int(int_data)
    except ValueError:
        return  HttpResponse("Something went wrong", status=404)

    return HttpResponse("okay path converter for str to int and int is ready")
# His block of code will show exception error if string is found in path
