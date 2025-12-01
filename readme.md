## Django Rest API

---

1. Start a new app API, in the main app folder

```
python manage.py startapp api
```

ts api app will contain our all end points, models, etc. It will contain evrything

2. Tell Django, the new installed framework and the new API app, go to settings.py
   add 'rest_framework','api'

3. Inorder to create a rest API, we will need some data, make a CRUD.

4. Over here we are making a usertype project API, where we will have user to write our data

5. Define how our data should look like, in manage.py of 'api'
   |\_ ts step is defined in models.py of api

6. Now make migrations, for now we are using sqlite as the db, which is simple django provided db

```
python manage.py makemigrations
```

```
python manage.py migrate
```

7. Creating Serializers
