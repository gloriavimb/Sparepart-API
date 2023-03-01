# Sparepart-API

## List of requests and their paramaters

### GET /parts
#### Parameters
| Parameter | Value | Example | Description | Notes | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| page | Integer of page number | /parts?page=6 | returns sixth page | Default value is 0. Attempting to view page that doesn't exist returns 404 |
| page_size | Integer of results per page | /parts?page_size=10 | Returns 10 responses per page | Maximum integer limit is 20, default is 5 |
| search_by | String of the search category | /parts?search_by=name | Searches category "Name" for search | If empty returns all parts. Valid values are name, serial, manufacturer |
| search | String of the keyword for the search | /parts?search=engine | Returns everything that includes engine in its name | If empty returns all parts |
| sort_by | String of the sorting category  | /parts?sort_by=name  | Sorts the field by the category | Default value is name |
| decending | Boolean  | /part?decending=True | Reverses the sort | Default value is false |

#### Examples

##### Default
        http://localhost:3030/parts
Response:
```json
[
    {
        "id": 3284,
        "serial": "10860370",
        "name": " ",
        "storage_1": 0.0,
        "storage_2": 0.0,
        "storage_3": 0.0,
        "storage_4": 0.0,
        "storage_5": 9.0,
        "sus_1": 0.0,
        "sus_2": 1.27,
        "manufacturer": "FIAT",
        "price": 1.52
    },
    //...
]
```

##### With parameters
        http://127.0.0.1:5000/parts?page=6&page_size=10&search_by=name&search=engine&sort_by=name&decending=True
Response:
```json
[
    {
        "id": 3324,
        "serial": "11000415407",
        "name": "Rmfd engine",
        "storage_1": 0.0,
        "storage_2": 0.0,
        "storage_3": 0.0,
        "storage_4": 0.0,
        "storage_5": 0.0,
        "sus_1": 0.0,
        "sus_2": 9030.944,
        "manufacturer": "B",
        "price": 10837.13
    },
    //...
]
```
