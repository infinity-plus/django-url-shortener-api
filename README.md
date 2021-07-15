# Django URL Shortener API

A simple Postgres backed URL Shortener API made using Django REST Framework.

## Environment Variables

| Variable | Required | Default | Description |
| :------: | :------: | ------- | ----------- |
| SECRET_KEY | &#9745; | None | This value is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values. |
| DATABASE_URL | &#9745; | None | The valid Postgres Connection URI |
| HOSTS | &#9744; |None | A space-separated list of hosts supported by the Django App. |
| DISABLE_COLLECTSTATIC | &#9744; | None | Set to 1 to disable collectstatic. |
