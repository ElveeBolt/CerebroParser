### Main info of JSON
```json
{
  "name": ["Sergio Ramos", "Сергио Рамос"],
  "sex": 0,
  "birth_date": "14.20.1996",
  "birth_place": "Russia, Moscow",
  "country": "Russia",
  "address": "",
  "relationship": 0,
  "childrens": 3,
  "phones": ["38050625478", "6587946354"],
  "emails": ["emails@mail.com", "someemail@gmail.com"]
}
```
<kbd>name</kbd> - name in other languages

<kbd>sex</kbd> - sex
* 0 - female
* 1 - male

<kbd>birth_date</kbd> - date of birth

<kbd>birth_place</kbd> - place of birth

<kbd>country</kbd> - country

<kbd>address</kbd> - address

<kbd>relationship</kbd> - relationship
* 0 - Замужем / Женат
* 1 - Вдова / Вдовец
* 2 - Разведена / Разведён
* 3 - Помолвлена / Помолвлен
* 4 - В активном поиске

<kbd>childrens</kbd> - count childrens

<kbd>phones</kbd> - list of phones

<kbd>emails</kbd> - list of emails

### Socials
```json
{
  "socials": [
    {
      "title": "Telegram",
      "id": "546876878",
      "link": "link",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - name of social link.

For example: 
* Telegram
* Instagram
* Vk
* Facebook
* etc.

<kbd>id</kbd> - user id

<kbd>link</kbd> - username of profile

<kbd>comment</kbd> - some comments

### Educations
```json
{
  "educations": [
    {
      "title": "NAU",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - name of school, university or college

<kbd>comment</kbd> - some comments

### Works
```json
{
  "works": [
    {
      "post": "Barmen",
      "date": "14.20.2020 - 20.20.2020",
      "company": "KavaComp",
      "address": "Ukraine, Lviv",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>post</kbd> - name of post

<kbd>date</kbd> - works date

<kbd>company</kbd> - company name

<kbd>address</kbd> - work address

<kbd>comment</kbd> - some comments

### Documents
```json
{
  "documents": [
    {
      "title": "Passport",
      "country": "Poland",
      "serial": "456784354",
      "date": "17.10.2022",
      "authority": "authority",
      "status": 0,
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - name of document

<kbd>country</kbd> - document country

<kbd>serial</kbd> - serial number. Example: BP494520, 7985423655548

<kbd>status</kbd> - document status
* 0 - Не Действительный
* 1 - Действительный

<kbd>comment</kbd> - some comments

### Cars
```json
{
  "cars_status": true,
  "cars": [
    {
      "model": "Tesla Model B",
      "year": 2021,
      "color": "Red",
      "number": "AO4598AA",
      "vin": "5689745431",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>cars_status</kbd> - if has car
* true
* false

<kbd>model</kbd> - car model

<kbd>year</kbd> - year of issue

<kbd>color</kbd> - car color

<kbd>number</kbd> - car numbers

<kbd>vin</kbd> - vehicle identification number

<kbd>comment</kbd> - some comments

### Banks
```json
{
  "banks": [
    {
      "title": "Alfa-Bank",
      "card_number": "5498 6897 5487 4578",
      "login": "380506254896",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - name of bank

<kbd>card_number</kbd> - card number or payment number

<kbd>login</kbd> - if have login username or number

<kbd>comment</kbd> - some comments


### Ownerships
```json
{
  "ownerships": [
    {
      "title": "House",
      "date": "10.11.2022",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - name ownership

<kbd>date</kbd> - date of ownership

<kbd>comment</kbd> - some comments

### Links
```json
{
  "links": [
    {
      "title": "Profile in OLX",
      "link": "https://olx.com/fsdfsdf",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - title

<kbd>link</kbd> - link

<kbd>comment</kbd> - some comments

### Accounts
```json
{
  "accounts": [
    {
      "title": "title",
      "link": "link",
      "login": "Login",
      "password": "Password",
      "comment": "Some comments"
    }
  ]
}
```
<kbd>title</kbd> - title

<kbd>login</kbd> - login

<kbd>password</kbd> - password

<kbd>comment</kbd> - some comments

### Other
```json
{
  "ip": ["192.168.20.20", "127.0.0.1"],
  "coordinates": ["41.25487 69.8754", "47.45666 89.56897"],
  "comment": "Some comment",
  "database": "Database",
  "status": 0,
  "category": 0,
  "tags": ["Soldier", "Politics"],
  "date": "14.20.1995 14:50"
}
```
<kbd>ip</kbd> - ip addresses

<kbd>coordinates</kbd> - coordinates

<kbd>comment</kbd> - some comments

<kbd>database</kbd> - name of database

<kbd>status</kbd> - status
* 0 - Not verify profile
* 1 - Verify profile

<kbd>category</kbd> - document category
* 0 - People
* 1 - Social Profile
* 2 - Politic
* 3 - Soldier

<kbd>tags</kbd> - tags of object.

For example:
* Politic
* Soldier

<kbd>date</kbd> - date parse