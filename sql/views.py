from django.shortcuts import render
from django.db import connection
from django.db.utils import OperationalError, IntegrityError


def index(request):
    query = request.GET.get('query','')

    if query:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except (IntegrityError, OperationalError) as e:
            err = str(e)

    return render(request, "sql/index.html", locals())
