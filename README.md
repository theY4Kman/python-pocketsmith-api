# pocketsmith-api
[Pocketsmith](https://pocketsmith.com) API client, automatically generated with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) from a [manicured version](https://github.com/theY4Kman/pocketsmith-api-spec) of the [official OpenAPI spec](https://github.com/pocketsmith/api)


# Installation
```bash
pip install pocketsmith-api
```


# Usage
```pycon
>>> import pocketsmith
>>> client = pocketsmith.PocketsmithClient('my-api-key')
>>> client.users.get_me()
{'always_show_base_currency': False,
 'avatar_url': 'https://secure.gravatar.com/avatar/73e4f4549e97ad9d53e11b8e987f4b90?d=404',
 'base_currency_code': 'usd',
 'beta_user': True,
 'created_at': datetime.datetime(2016, 10, 17, 6, 22, 44, tzinfo=tzutc()),
 'email': 'yak@y4k.dev',
 'id': 1234565,
 'last_activity_at': datetime.datetime(2020, 10, 3, 6, 57, 44, tzinfo=tzutc()),
 'last_logged_in_at': datetime.datetime(2020, 10, 3, 4, 58, 35, tzinfo=tzutc()),
 'login': 'yamsandwich',
 'name': 'Yam S Andwich',
 'time_zone': 'Eastern Time (US & Canada)',
 'updated_at': datetime.datetime(2020, 10, 3, 6, 57, 44, tzinfo=tzutc()),
 'using_multiple_currencies': False,
 'week_start_day': 0}
```


# Generating the library
The [`@openapitools/openapi-generator-cli`](https://github.com/OpenAPITools/openapi-generator-cli) npm package is used for generation. This package will automatically download the latest OpenAPI Generator .jar. To install, run:
```bash
npm install -g @openapitools/openapi-generator-cli
```

Then, run the following to generate the library from spec, and add a few customizations on top (like the `PocketsmithClient` class)
```bash
./generate-pocketsmith-library.sh
```
