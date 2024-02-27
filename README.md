## Image gallery project using Django + AWS S3 + Tailwind

### Installation
##### start tailwind watcher 
``` npx tailwindcss -i ./staticfiles/src/input.css -o ./staticfiles/src/output.css --watch ```

##### Start server

``` python3 manage.py runserver ```

##### Deployment
create .env file at the root of theproject and add following values from aws s3
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=

##### Deployment
databse is postgres, you can change it to sqlite3